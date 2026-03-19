# AutoML Platform 🤖

A modular Machine Learning platform that automates the loan approval prediction process using trained ML models. Built as part of the AIML Internship at LearnDepth.

---

## 📌 Project Overview

The AutoML Platform provides an end-to-end pipeline for:

- Saving and loading trained ML models via a Model Registry
- Running predictions on new applicant data
- Returning human-readable decisions with confidence scores
- Explaining key factors behind each loan decision

---

## 📁 Project Structure

```
AutoML-Platform/
├── ml_engine/
│   ├── __init__.py
│   ├── predict.py
│   └── registry.py
├── models/
│   └── metadata.json
├── test.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ⚙️ How to Set Up

### Step 1 — Clone the Repository

```
git clone https://github.com/Akashks26/AutoML-Platform.git
cd AutoML-Platform
```

### Step 2 — Create a Virtual Environment

```
python -m venv .venv
```

### Step 3 — Activate the Virtual Environment

On Windows:
```
.venv\Scripts\Activate.ps1
```

### Step 4 — Install Required Libraries

```
pip install -r requirements.txt
```

---

## 🚀 How to Run

```
python test.py
```

---

## 📊 Sample Output

```
========================================
       LOAN PREDICTION RESULT
========================================

  Decision    : Loan Approved
  Confidence  : 98.0%

  Key Factors:
    - Strong income ($55,000)
    - Good credit score (720)
    - Stable work experience (6 years)

  Applicant Profile:
    Age            : 34
    Salary         : $55,000
    Experience     : 6 years
    Credit Score   : 720

========================================
```

---

## 🧠 Module Breakdown

### registry.py — Model Registry

| Function | Description |
|---|---|
| `save_model()` | Saves trained model and metadata to disk |
| `load_model()` | Loads saved model from disk with error handling |

### predict.py — Prediction Engine

| Function | Description |
|---|---|
| `predict()` | Takes applicant data and returns loan decision |
| `_explain_decision()` | Returns key factors behind the decision |

### __init__.py — Package Initializer

Exposes `predict`, `save_model`, and `load_model` for clean imports across the project.

---

## 📥 Input Format

```python
input_data = {
    "age"         : 34,
    "salary"      : 55000,
    "experience"  : 6,
    "credit_score": 720
}
```

| Field | Type | Description |
|---|---|---|
| age | int | Applicant age in years |
| salary | int | Annual salary in USD |
| experience | int | Work experience in years |
| credit_score | int | Credit score between 300 and 850 |

---

## 🛡️ Error Handling

| Scenario | Response |
|---|---|
| Model not trained yet | "No trained model found. Please train the model first." |
| Missing input fields | "Invalid input. Required fields: age, salary, experience, credit_score" |
| Unexpected errors | "Prediction failed: error details" |

---

## 🛠️ Tools and Technologies

* Python 3.11
* Scikit-learn
* Pandas
* Joblib
* NumPy
* SciPy

---


