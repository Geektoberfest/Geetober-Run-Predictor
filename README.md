# Run Predictor

A machine learning project that predicts a cricket batter's runs using historical performance data and regression techniques.

The project explores cricket data, performs exploratory data analysis (EDA), and develops a regression-based prediction pipeline.

## Features

- Exploratory data analysis of cricket performance data.
- Data preprocessing and feature analysis.
- Regression-based run prediction.
- Model evaluation using appropriate regression metrics.
- Planned: an interactive Streamlit web interface.
- Planned: experiments to improve prediction accuracy and model generalization.

> **Note:** Features marked as planned may not be implemented yet.

## Tech Stack

- Python
- NumPy
- Pandas
- Matplotlib
- Seaborn
- Scikit-learn
- Jupyter Notebook
- Streamlit (for the planned web interface)

## Repository Structure

```text
Run-Predictor/
├── EDA/
├── data/
├── training/
├── app.py
├── requirements.txt
├── README.md
├── LICENSE
├── .gitignore
└── .github/
    ├── ISSUE_TEMPLATE/
    │   └── feature_request.md
    └── PULL_REQUEST_TEMPLATE.md
```

## Prerequisites

Install the following before running the project:

- Python 3.10 or a compatible version supported by the project's dependencies.
- Git.
- pip.

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/SarveshHardas/Run-Predictor.git
cd Run-Predictor
```

### 2. Create a virtual environment

**Windows:**

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

**Linux/macOS:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Running the Project

### Exploratory Data Analysis

Open the relevant notebook from the `EDA/` directory using Jupyter Notebook or JupyterLab.

```bash
jupyter notebook
```

Select the notebook you want to explore.

### Model Training

The model training code is located in the `training/` directory.

Inspect the available scripts or notebooks in that directory and execute the appropriate training entry point. Refer to the relevant files for required dataset paths and configuration.

### Streamlit Interface

The Streamlit app lets you enter an opposition, ground, batting position, and innings and see the predicted runs. It uses the saved model and the same preprocessing as the training script.

The app needs the saved model at `training/artifacts/best_model.joblib`. Create it first by running the training script from the repository root:

```bash
python training/run_prediction_experiments.py
```

Then start the app from the repository root:

```bash
streamlit run app.py
```

Open the URL that Streamlit prints, usually `http://localhost:8501`. If the model file is missing, the app shows the command to create it.

## Model Evaluation

Model performance should be assessed on data that was not used to train the model.

Recommended regression metrics include:

- **Mean Absolute Error (MAE):** Average absolute prediction error.
- **Root Mean Squared Error (RMSE):** Penalizes larger prediction errors more heavily.
- **R² score:** Measures the model's fit relative to a baseline predictor.

Run `python training/run_prediction_experiments.py` from the repository root to reproduce the comparison below. It builds every feature from earlier innings only and validates with 5 chronological folds, so each model is tested on matches that come after its training data.

| Model | MAE | RMSE | R² |
|---|---|---|---|
| Mean of previous innings (baseline) | 37.50 (±3.72) | 45.04 | -0.049 |
| Existing model: Linear Regression | 38.03 (±4.03) | 45.94 | -0.091 |
| Linear Regression (all features) | 40.81 (±3.42) | 49.08 | -0.248 |
| Ridge Regression | 37.63 (±3.68) | 45.09 | -0.051 |
| Random Forest | 39.02 (±4.32) | 47.29 | -0.157 |
| Gradient Boosting | 41.30 (±4.34) | 51.06 | -0.351 |

MAE is the mean across folds, with the fold standard deviation in brackets. The validation covers 297 innings.

None of the candidate models beat the baseline on this dataset. The script therefore saves the baseline to `training/artifacts/best_model.joblib`. Its R² is negative, so the current features do not explain the match-to-match variation in runs. Predictions should not be treated as reliable estimates of an individual innings.

## Contributing

Contributions are welcome.

1. Check the existing GitHub issues or open a new issue describing the proposed change.
2. Fork this repository.
3. Create a separate branch for your contribution.

```bash
git checkout -b feature/your-feature-name
```

4. Implement and test your changes.
5. Commit and push your branch.

```bash
git add .
git commit -m "feat: describe your changes"
git push origin feature/your-feature-name
```

6. Open a pull request against the original repository and link the related issue.

### Contribution Guidelines

- Keep changes focused on the issue being addressed.
- Avoid introducing data leakage into model training or evaluation.
- Preserve the existing project functionality.
- Document changes to model features, preprocessing, and evaluation.
- Do not commit virtual environments, credentials, or unnecessary generated files.
- Include reproducible evaluation results when proposing model improvements.

## Roadmap

- [ ] Establish a reproducible baseline for the existing regression model.
- [ ] Compare suitable regression algorithms and feature-engineering approaches.
- [ ] Evaluate improvements using appropriate validation metrics.
- [ ] Develop an interactive Streamlit interface.
- [ ] Document the complete training and inference workflow.

## License

This project is licensed under the MIT License.
See the [LICENSE](LICENSE) file for details.  
