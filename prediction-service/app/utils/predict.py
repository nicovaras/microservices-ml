import joblib
import os
import numpy as np

model_path = 'app/ml_models/iris_model.pkl'

model = joblib.load(model_path)

def make_prediction(features: list):
    prediction = model.predict([features])[0]
    probabilities = model.predict_proba([features])[0].tolist()
    return prediction, probabilities
