from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.prediction import PredictionRecord
from app.schemas.prediction import PredictionCreate, PredictionResponse
from app.database.database import get_db
from typing import List, Optional
import json
from auth import get_current_user

router = APIRouter()

@router.post("/save", response_model=PredictionResponse)
def save_prediction(prediction: PredictionCreate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    db_prediction = PredictionRecord(
        user_id=prediction.user_id,
        input_data=json.dumps(prediction.input_data),
        prediction=prediction.prediction,
        probabilities=json.dumps(prediction.probabilities)
    )
    db.add(db_prediction)
    db.commit()
    db.refresh(db_prediction)

    db_prediction.input_data = json.loads(db_prediction.input_data)
    db_prediction.probabilities = json.loads(db_prediction.probabilities)
     
    return db_prediction

@router.get("/history/{user_id}", response_model=List[PredictionResponse])
def get_user_predictions(user_id: int, db: Session = Depends(get_db), user=Depends(get_current_user)):
    predictions = db.query(PredictionRecord).filter(PredictionRecord.user_id == user_id).all()
    for prediction in predictions:
        prediction.input_data = json.loads(prediction.input_data)
        prediction.probabilities = json.loads(prediction.probabilities)
            
    return predictions
