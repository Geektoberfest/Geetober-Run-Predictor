"""Streamlit interface for the Run Predictor model.

Launch from the repository root with:
    streamlit run app.py
"""

from pathlib import Path

import joblib
import streamlit as st

try:
    from training.run_prediction_experiments import MODEL_PATH, load_matches, predict_next_innings
except ImportError:
    st.error("`training/run_prediction_experiments.py` was not found. Run the app from the repository root.")
    st.stop()

MODEL_RELATIVE_PATH = Path("training") / "artifacts" / "best_model.joblib"
MAX_GROUND_LENGTH = 100


@st.cache_resource(show_spinner=False)
def load_model_bundle():
    return joblib.load(MODEL_PATH)


@st.cache_data(show_spinner=False)
def load_options():
    matches = load_matches()
    return sorted(matches["opposition"].unique()), sorted(matches["ground"].unique())


st.set_page_config(page_title="Run Predictor", page_icon="🏏", layout="centered")
st.title("Run Predictor")
st.write("Estimate how many runs a batter will score in their next ODI innings.")

if not MODEL_PATH.exists():
    st.error(
        f"Model file not found: `{MODEL_RELATIVE_PATH.as_posix()}`. "
        "Run `python training/run_prediction_experiments.py` from the repository root to create it."
    )
    st.stop()

try:
    bundle = load_model_bundle()
except Exception as error:  # joblib can raise several error types for a corrupt file
    st.error(f"Could not load the model file: {error}")
    st.stop()

oppositions, grounds = load_options()

with st.form("prediction_form"):
    opposition = st.selectbox("Opposition", oppositions)
    ground = st.text_input("Ground", placeholder="e.g. Colombo (RPS)", help="Venue name as it appears in the dataset.")
    col_position, col_innings = st.columns(2)
    position = col_position.number_input(
        "Batting position", min_value=1, max_value=11, value=3, step=1, help="Batting order, from 1 to 11."
    )
    innings = col_innings.selectbox("Innings", [1, 2], help="1 = batting first, 2 = batting second.")
    submitted = st.form_submit_button("Predict runs", type="primary")

if submitted:
    ground = ground.strip()
    errors = []
    if not ground:
        errors.append("Enter a ground name.")
    elif len(ground) > MAX_GROUND_LENGTH:
        errors.append(f"Ground name must be {MAX_GROUND_LENGTH} characters or fewer.")

    if errors:
        for message in errors:
            st.error(message)
    else:
        if ground not in grounds:
            st.warning(
                f"'{ground}' is not in the dataset, so the venue average uses the career average instead."
            )
        try:
            runs = predict_next_innings(bundle, opposition, ground, int(position), int(innings))
        except Exception as error:
            st.error(f"Prediction failed: {error}")
        else:
            st.subheader("Predicted runs")
            st.metric(label=f"Expected runs vs {opposition}", value=f"{runs:.0f}")
            if bundle["name"].startswith("Mean of"):
                st.info(
                    "The saved model predicts the average of past innings, so this result is the same "
                    "for every input. It is an estimate, not a guaranteed score."
                )
            else:
                st.caption(f"Model: {bundle['name']}. This is an estimate, not a guaranteed score.")
