"""Compare run-prediction models using chronological validation.

Run from the repository root:
    python training/run_prediction_experiments.py

Every feature for an innings is built only from earlier innings, and each
validation fold trains on the past and tests on the future. The same
build_features() function is used for training and for predict_next_innings(),
so inference uses the same preprocessing as training.
"""

from pathlib import Path

import joblib
import numpy as np
import pandas as pd
from sklearn.base import clone
from sklearn.dummy import DummyRegressor
from sklearn.ensemble import GradientBoostingRegressor, RandomForestRegressor
from sklearn.linear_model import LinearRegression, RidgeCV
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import TimeSeriesSplit
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

ROOT = Path(__file__).resolve().parent.parent
DATA_PATH = ROOT / "data" / "virat_odi_data.csv"
MODEL_PATH = ROOT / "training" / "artifacts" / "best_model.joblib"

# Feature set used by the existing notebook model (training/model.ipynb).
EXISTING_FEATURES = ["pos", "inns", "prev_runs", "roll3", "roll10", "career_avg", "ground_avg"]


def load_matches():
    """Return completed innings in chronological order (DNB/TDNB rows removed)."""
    raw = pd.read_csv(DATA_PATH)
    raw = raw[raw["Runs"].str.match(r"^\d+\*?$")]
    matches = pd.DataFrame(
        {
            "date": pd.to_datetime(raw["Start Date"], format="%d %b %Y"),
            "runs": raw["Runs"].str.rstrip("*").astype(int),
            "sr": pd.to_numeric(raw["SR"], errors="coerce"),
            "pos": pd.to_numeric(raw["Pos"]),
            "inns": pd.to_numeric(raw["Inns"]),
            "opposition": raw["Opposition"],
            "ground": raw["Ground"],
        }
    )
    return matches.sort_values("date", kind="stable").reset_index(drop=True)


def build_features(matches):
    """Return pre-match features for every row of matches.

    Only earlier innings are used, so the last row can be an upcoming match
    whose runs are unknown (NaN).
    """
    runs_before = matches["runs"].shift(1)
    features = pd.DataFrame(index=matches.index)
    features["pos"] = matches["pos"]
    features["inns"] = matches["inns"]
    features["prev_runs"] = runs_before
    features["roll3"] = runs_before.rolling(3, min_periods=1).mean()
    features["roll5"] = runs_before.rolling(5, min_periods=1).mean()
    features["roll10"] = runs_before.rolling(10, min_periods=1).mean()
    features["roll5_std"] = runs_before.rolling(5, min_periods=2).std()
    features["form_sr5"] = matches["sr"].shift(1).rolling(5, min_periods=1).mean()
    features["career_avg"] = runs_before.expanding().mean()
    features["ground_avg"] = matches.groupby("ground")["runs"].transform(
        lambda runs: runs.shift(1).expanding().mean()
    )
    # First innings at a ground have no venue history, so fall back to career average.
    features["ground_avg"] = features["ground_avg"].fillna(features["career_avg"])
    dummies = pd.get_dummies(matches["opposition"], prefix="opp", dtype=float)
    return pd.concat([features, dummies], axis=1)


def candidate_models():
    """Return (name, estimator, feature names) for every model under comparison."""
    all_features = None  # None means every column from build_features()
    return [
        ("Mean of previous innings (baseline)", DummyRegressor(), all_features),
        ("Existing model: Linear Regression", LinearRegression(), EXISTING_FEATURES),
        ("Linear Regression", make_pipeline(StandardScaler(), LinearRegression()), all_features),
        (
            "Ridge Regression",
            make_pipeline(StandardScaler(), RidgeCV(alphas=np.logspace(-2, 3, 20))),
            all_features,
        ),
        (
            "Random Forest",
            RandomForestRegressor(n_estimators=300, min_samples_leaf=5, random_state=42),
            all_features,
        ),
        (
            "Gradient Boosting",
            GradientBoostingRegressor(
                n_estimators=200, learning_rate=0.03, max_depth=2, subsample=0.8, random_state=42
            ),
            all_features,
        ),
    ]


def cross_validate(estimator, X, y, columns):
    """Return mean and std of MAE, RMSE and R2 across chronological folds."""
    scores = {"MAE": [], "RMSE": [], "R2": []}
    X = X if columns is None else X[columns]
    for train_idx, test_idx in TimeSeriesSplit(n_splits=5).split(X):
        model = clone(estimator)
        model.fit(X.iloc[train_idx], y.iloc[train_idx])
        pred = model.predict(X.iloc[test_idx])
        scores["MAE"].append(mean_absolute_error(y.iloc[test_idx], pred))
        scores["RMSE"].append(np.sqrt(mean_squared_error(y.iloc[test_idx], pred)))
        scores["R2"].append(r2_score(y.iloc[test_idx], pred))
    return {name: (np.mean(values), np.std(values)) for name, values in scores.items()}


def predict_next_innings(bundle, opposition, ground, pos, inns):
    """Predict runs for an upcoming innings using the saved model bundle."""
    history = load_matches()
    upcoming = pd.DataFrame(
        [{"runs": np.nan, "sr": np.nan, "pos": pos, "inns": inns, "opposition": opposition, "ground": ground}]
    )
    matches = pd.concat([history, upcoming], ignore_index=True)
    X = build_features(matches).iloc[[-1]].reindex(columns=bundle["feature_columns"], fill_value=0)
    return float(bundle["model"].predict(X[bundle["model_columns"]])[0])


def main():
    matches = load_matches()
    features = build_features(matches)
    valid = features.notna().all(axis=1)
    data = features[valid]
    runs = matches["runs"][valid]

    candidates = candidate_models()
    results = {name: cross_validate(estimator, data, runs, columns) for name, estimator, columns in candidates}

    print(f"Chronological 5-fold validation on {len(data)} innings\n")
    print(f"{'Model':<40}{'MAE':>16}{'RMSE':>10}{'R2':>10}")
    for name, metrics in results.items():
        (mae, mae_std), (rmse, _), (r2, _) = metrics["MAE"], metrics["RMSE"], metrics["R2"]
        print(f"{name:<40}{mae:>8.2f} (+/-{mae_std:.2f}){rmse:>10.2f}{r2:>10.3f}")

    best_name, best_estimator, best_columns = min(
        candidates, key=lambda candidate: results[candidate[0]]["MAE"][0]
    )
    print(f"\nSelected model (lowest mean MAE): {best_name}")

    model_columns = list(data.columns) if best_columns is None else best_columns
    best_model = clone(best_estimator).fit(data[model_columns], runs)
    MODEL_PATH.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(
        {
            "name": best_name,
            "model": best_model,
            "feature_columns": list(data.columns),
            "model_columns": model_columns,
        },
        MODEL_PATH,
    )
    print(f"Saved to {MODEL_PATH.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
