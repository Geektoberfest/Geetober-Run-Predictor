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

The interactive Streamlit interface is planned for a future contribution.

Once `app.py` has been implemented, the intended launch command is:

```bash
streamlit run app.py
```

Until then, the command may not produce a functional application.

## Model Evaluation

Model performance should be assessed on data that was not used to train the model.

Recommended regression metrics include:

- **Mean Absolute Error (MAE):** Average absolute prediction error.
- **Root Mean Squared Error (RMSE):** Penalizes larger prediction errors more heavily.
- **R² score:** Measures the model's fit relative to a baseline predictor.

Actual performance metrics should be added here after evaluating the existing model. Do not report unverified accuracy claims.

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
