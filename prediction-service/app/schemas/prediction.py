from pydantic import BaseModel
from typing import List

class PredictionInput(BaseModel):
    features: List[float]
    
class PredictionResponse(BaseModel):
    prediction: int
    probabilities: List[float]
