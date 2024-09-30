from fastapi import APIRouter, HTTPException
from app.schemas.prediction import PredictionInput, PredictionResponse
from app.utils.predict import make_prediction

router = APIRouter()

@router.post("/predict", response_model=PredictionResponse)
def predict(input_data: PredictionInput):
    try:
        prediction, probabilities = make_prediction(input_data.features)
        return {"prediction": prediction, "probabilities": probabilities}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
