
import json
import joblib
import numpy as np
from azureml.core.model import Model

def init():
    global model
    # Load the model
    model_path = Model.get_model_path("diabetes_model")
    model = joblib.load(model_path)

def run(raw_data):
    try:
        # Parse input data
        data = np.array(json.loads(raw_data)["data"])
        # Make predictions
        predictions = model.predict(data)
        # Return predictions as JSON
        return json.dumps(predictions.tolist())
    except Exception as e:
        error = str(e)
        return json.dumps({"error": error})