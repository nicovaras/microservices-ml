from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class PredictionCreate(BaseModel):
    user_id: int
    input_data: List[float]
    prediction: int
    probabilities: List[float]

class PredictionResponse(BaseModel):
    id: int
    user_id: int
    input_data: List[float]
    prediction: int
    probabilities: List[float]
    created_at: datetime

    class Config:
        orm_mode = True
