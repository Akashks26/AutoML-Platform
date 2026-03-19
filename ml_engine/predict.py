import pandas as pd
from ml_engine.registry import load_model

FEATURE_COLUMNS = ["age", "salary", "experience", "credit_score"]

SALARY_THRESHOLD     = 50_000
CREDIT_THRESHOLD     = 700
EXPERIENCE_THRESHOLD = 5


def predict(input_data: dict) -> dict:
    try:
        model = load_model()

        applicant_df = pd.DataFrame([input_data])
        applicant_df = applicant_df[FEATURE_COLUMNS]

        prediction  = model.predict(applicant_df)[0]
        probability = model.predict_proba(applicant_df)[0][prediction]

        decision    = "Loan Approved" if prediction == 1 else "Loan Rejected"
        key_factors = _explain_decision(input_data)

        return {
            "Decision"     : decision,
            "Confidence"   : f"{round(probability * 100, 2)}%",
            "Key Factors"  : key_factors,
            "Input Summary": {
                "Age"         : input_data["age"],
                "Salary"      : f"${input_data['salary']:,}",
                "Experience"  : f"{input_data['experience']} years",
                "Credit Score": input_data["credit_score"]
            }
        }

    except FileNotFoundError as e:
        return {"error": str(e)}

    except KeyError:
        return {"error": "Invalid input. Required fields: age, salary, experience, credit_score"}

    except Exception as e:
        return {"error": f"Prediction failed: {str(e)}"}


def _explain_decision(input_data: dict) -> list:
    reasons = []

    if input_data["salary"] > SALARY_THRESHOLD:
        reasons.append(f"Strong income (${input_data['salary']:,})")

    if input_data["credit_score"] > CREDIT_THRESHOLD:
        reasons.append(f"Good credit score ({input_data['credit_score']})")

    if input_data["experience"] > EXPERIENCE_THRESHOLD:
        reasons.append(f"Stable work experience ({input_data['experience']} years)")

    if not reasons:
        reasons.append("Limited financial strength based on the provided profile")

    return reasons