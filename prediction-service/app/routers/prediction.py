from fastapi import APIRouter, Depends, HTTPException
from app.schemas.prediction import PredictionInput, PredictionResponse
from app.utils.predict import make_prediction
from auth import get_current_user
import requests
import json

#change with docker networks...
DATA_SERVICE_URL = "http://data-service:8000/predictions/save"

router = APIRouter()

@router.post("/predict", response_model=PredictionResponse)
def predict(input_data: PredictionInput, user=Depends(get_current_user)):
    try:
        prediction, probabilities = make_prediction(input_data.features)
        headers = {"Authorization": f"Bearer {user['token']}"}
        save_data = {
            "user_id": user["user_id"],
            "input_data": input_data.features,
            "prediction": prediction,
            "probabilities": probabilities,
        }

        try:
            response = requests.post(DATA_SERVICE_URL, json=save_data, headers=headers)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            raise HTTPException(status_code=500, detail=f"Error saving prediction: {str(e)}")
        return {"prediction": prediction, "probabilities": probabilities}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
