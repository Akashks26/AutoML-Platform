import joblib
import os
import json

MODEL_PATH = "models/model.pkl"
METADATA_PATH = "models/metadata.json"


def save_model(model, model_name, metrics):
    os.makedirs("models", exist_ok=True)

    joblib.dump(model, MODEL_PATH)

    metadata = {
        "model_name": model_name,
        "metrics": metrics
    }

    with open(METADATA_PATH, "w") as f:
        json.dump(metadata, f, indent=4)

    return {"message": f"Model '{model_name}' saved successfully"}


def load_model():
    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError(
            "No trained model found. Please train the model before making predictions."
        )

    model = joblib.load(MODEL_PATH)
    return model