from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime
from app.database.database import Base

class PredictionRecord(Base):
    __tablename__ = "predictions"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, index=True) 
    input_data = Column(String, index=True)
    prediction = Column(Integer)
    probabilities = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
