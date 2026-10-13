# Contributing to Run Predictor

Thank you for your interest in contributing to **Run Predictor**! This document explains how to set up the project locally, understand its structure, contribute improvements, test changes, and submit pull requests.

All contributions, including bug fixes, model improvements, documentation updates, and the planned Streamlit interface, are welcome.

---

## 1. Project Overview & Architecture

Run Predictor is a Python-based machine learning project that predicts a cricket batter's runs using historical performance data and regression techniques.

The project focuses on exploratory data analysis, data preprocessing, model training, prediction, and evaluation.

### Repository Structure

```text
Run-Predictor/
├── EDA/                         # Exploratory data analysis
├── data/                        # Dataset files
├── training/                    # Model training and preprocessing
├── app.py                       # Streamlit application entry point
├── requirements.txt             # Python dependencies
├── README.md                    # Project documentation
├── LICENSE                      # Project license
├── .gitignore                   # Git exclusions
├── CONTRIBUTING.md              # Contribution guidelines
└── .github/
    ├── ISSUE_TEMPLATE/
    │   └── feature_request.md   # Feature request template
    └── PULL_REQUEST_TEMPLATE.md # Pull request template
```

This structure describes the intended layout. Contributors should preserve existing files and workflows when making changes.

---

## 2. Prerequisites & Supported Environment

Before contributing, install:

- **Python:** A version compatible with the project's dependencies.
- **Git:** For version control and branch management.
- **pip:** For installing Python packages.
- **Jupyter Notebook or JupyterLab:** For exploring existing notebooks.

A virtual environment is strongly recommended to keep dependencies isolated.

---

## 3. Forking & Cloning the Repository

1. Open the [Run Predictor repository](https://github.com/SarveshHardas/Run-Predictor).
2. Click **Fork** to create your own copy.
3. Clone your fork:

   ```bash
   git clone https://github.com/YOUR_USERNAME/Run-Predictor.git
   cd Run-Predictor
   ```

4. Add the original repository as the upstream remote:

   ```bash
   git remote add upstream https://github.com/SarveshHardas/Run-Predictor.git
   ```

5. Verify the configured remotes:

   ```bash
   git remote -v
   ```

Replace `YOUR_USERNAME` with your GitHub username.

---

## 4. Local Environment Setup

### Step 1: Create a virtual environment

**Windows PowerShell:**

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

**Linux/macOS:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Step 2: Install dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

If a dependency is missing, inspect the imports in the relevant source files before adding it to `requirements.txt`.

### Step 3: Verify the installation

```bash
python --version
pip list
```

Ensure that the installed packages are compatible with the project.

---

## 5. Understanding the Project Components

### Exploratory Data Analysis (`EDA/`)

This directory contains notebooks or scripts used to understand the dataset, examine distributions, identify relationships, and investigate data quality.

Contributions may include:
- Improving visualizations.
- Investigating missing values and outliers.
- Documenting feature distributions.
- Identifying potential sources of data leakage.

### Dataset (`data/`)

This directory contains the data used by the project.

Contributors should:
- Preserve the original dataset unless a change is necessary.
- Document any preprocessing or transformations.
- Avoid committing private, restricted, or unnecessarily large datasets.
- Verify dataset licenses and usage permissions before redistributing data.

### Model Training (`training/`)

This directory contains the training and preprocessing workflow.

Contributions may include:
- Comparing regression algorithms.
- Improving feature engineering.
- Evaluating model performance.
- Fixing preprocessing inconsistencies.
- Improving reproducibility.

Inspect the existing scripts and notebooks before modifying the training workflow.

### Streamlit Application (`app.py`)

The planned Streamlit application will provide an interface for entering supported model features and viewing predictions.

UI contributions should reuse the existing model and preprocessing pipeline instead of duplicating prediction logic.

---

## 6. Running the Project

### Exploratory Data Analysis

Launch Jupyter Notebook from the repository root:

```bash
jupyter notebook
```

Open a relevant notebook from `EDA/` and follow its execution order.

### Model Training

Inspect the contents of `training/` to identify the appropriate training script or notebook.

Execute the existing entry point with the required dataset paths and configuration. Do not assume a training command until the actual implementation has been verified.

### Streamlit Application

Once `app.py` is implemented, start the application using:

```bash
streamlit run app.py
```

The application should load the required model artifacts and preprocessing components according to the documented setup.

---

## 7. Improving Prediction Accuracy

Contributions aimed at improving prediction quality should be supported by reproducible experiments.

Recommended practices:

1. Establish a baseline using the existing model.
2. Compare suitable regression algorithms, such as Linear Regression, Ridge Regression, Random Forest, or Gradient Boosting, where appropriate.
3. Investigate useful features supported by the available dataset.
4. Use a validation strategy that reflects the intended prediction scenario.
5. Prevent data leakage, especially from future matches or information unavailable at prediction time.
6. Compare candidate models using consistent evaluation metrics.
7. Document the experimental setup and results.

### Recommended Evaluation Metrics

- **MAE:** Mean Absolute Error.
- **RMSE:** Root Mean Squared Error.
- **R²:** Coefficient of determination.

Do not claim that a model is more accurate based solely on training performance. Prefer validation or test results that represent unseen matches.

---

## 8. Testing & Validation

Before submitting a pull request, verify the affected functionality.

### For Machine Learning Changes

- [ ] Training completes without errors.
- [ ] Preprocessing is consistent between training and inference.
- [ ] Evaluation metrics are calculated correctly.
- [ ] Validation avoids data leakage.
- [ ] Results are reproducible using documented steps.

### For Streamlit Changes

- [ ] The application starts successfully.
- [ ] All required input features are available.
- [ ] Invalid inputs are handled appropriately.
- [ ] Predictions use the existing model and preprocessing.
- [ ] Missing model artifacts produce understandable errors.
- [ ] The layout remains usable across different screen sizes.

### For Documentation Changes

- [ ] Commands and file paths are accurate.
- [ ] Setup instructions are reproducible.
- [ ] No unverified performance claims are introduced.

Run relevant tests and validation scripts that exist in the repository. If automated tests have not yet been added, document the manual validation performed.

---

## 9. Branch Naming Conventions

Create a separate branch for each contribution.

Use lowercase names with descriptive prefixes:

- `feature/streamlit-dashboard`
- `feature/model-evaluation`
- `bugfix/preprocessing-error`
- `docs/contributing-guide`
- `refactor/training-pipeline`

Before starting, synchronize your fork with the upstream repository:

```bash
git fetch upstream
git checkout main
git merge upstream/main
```

Then create your feature branch:

```bash
git checkout -b feature/your-feature-name
```

If your default branch is not `main`, use the appropriate branch name.

---

## 10. Commit Message Guidelines

Use clear, descriptive commit messages. Conventional Commit prefixes are recommended:

- `feat: add Streamlit prediction dashboard`
- `fix: handle missing model artifacts`
- `perf: optimize feature preprocessing`
- `test: add regression evaluation tests`
- `docs: update local setup instructions`
- `refactor: simplify model inference pipeline`

Keep commits focused on a single logical change.

---

## 11. Submitting a Pull Request

1. Implement your changes on a dedicated branch.
2. Run the relevant tests and validation steps.
3. Review your changes:

   ```bash
   git status
   git diff
   ```

4. Stage and commit the intended files:

   ```bash
   git add .
   git commit -m "feat: describe your contribution"
   ```

5. Push your branch:

   ```bash
   git push origin feature/your-feature-name
   ```

6. Open a pull request against the original repository.
7. Link the related issue using `Closes #ISSUE_NUMBER` when appropriate.
8. Explain the implementation, testing performed, and any limitations.

Keep pull requests focused, reviewable, and consistent with the project's existing conventions.

---

## 12. Issue Assignment & Collaboration

Before implementing a feature:

- Review existing open issues to avoid duplicate work.
- Comment on the issue to discuss your intended approach.
- Wait for maintainer feedback or assignment where required.
- Follow the issue's acceptance criteria.
- Ask for clarification when requirements are ambiguous.

For this project, relevant contribution areas include:

- Regression model evaluation and improvement.
- Feature engineering and data preprocessing.
- Streamlit interface development.
- Testing and reproducibility.
- Documentation and setup improvements.

---

## 13. Definition of Done

A contribution is ready for review when:

1. The changes address the intended issue.
2. Existing functionality remains intact.
3. Relevant tests or validation have been completed.
4. Model changes include appropriate evaluation results.
5. Documentation is updated where necessary.
6. No secrets, unnecessary generated files, or restricted data are committed.
7. The pull request clearly explains the changes and testing performed.

---

## 14. Security & Data Handling

- Never commit API keys, credentials, passwords, or private environment files.
- Do not expose private datasets or sensitive information.
- Validate user inputs in the Streamlit application.
- Load trusted model artifacts and avoid unsafe deserialization of untrusted files.
- Do not silently download or execute external code as part of the prediction workflow.
- Respect the licenses and terms of use of datasets and third-party dependencies.

---

## 15. UI Contribution Guidelines

For the planned Streamlit interface:

- Keep the interface clear and easy to navigate.
- Use labels that explain the required inputs.
- Validate values before generating predictions.
- Display predicted runs prominently.
- Communicate errors and missing files clearly.
- Avoid presenting model predictions as guaranteed outcomes.
- Keep inference separate from training wherever practical.
- Include screenshots in pull requests when they help reviewers understand UI changes.

---

## 16. Reporting Bugs & Requesting Features

### Reporting Bugs

Include:
- A clear description of the problem.
- Steps to reproduce the issue.
- Expected and actual behavior.
- Relevant error messages or tracebacks.
- Python version and relevant dependency versions.

### Requesting Features

Include:
- The problem the feature aims to solve.
- The proposed implementation.
- Expected benefits.
- Acceptance criteria.
- Relevant examples or references.

Use the repository's GitHub issue templates when available.

---

## 17. License

By contributing to Run Predictor, you agree that your contributions may be distributed under the project's license, subject to the applicable terms.

Review the repository's `LICENSE` file before submitting contributions.

---

Thank you for helping improve Run Predictor through reproducible machine learning, maintainable code, and clear documentation.