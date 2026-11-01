import json
import numpy as np
import pandas as pd
import joblib
import os


def init():
    global model
    model_path = os.path.join(os.getenv('AZUREML_MODEL_DIR'), 'mgh_best_model.pkl')
    model = joblib.load(model_path)


def run(raw_data):
    try:
        # Parse the incoming JSON
        data = json.loads(raw_data)
        data_df = pd.DataFrame(data['data'])

        # Make the prediction
        result = model.predict(data_df)

        return json.dumps({
            "prediction": result.tolist(),
            "probability": model.predict_proba(data_df).tolist()
        })
    except Exception as e:
        return json.dumps({"error": str(e)})
