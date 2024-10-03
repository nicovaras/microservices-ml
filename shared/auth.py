from jose import JWTError, jwt

from fastapi import HTTPException, Security
from fastapi.security import HTTPBearer
import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"
security = HTTPBearer()

def verify_jwt_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = payload.get("sub")
        if user_id is None:
            raise HTTPException(status_code=403, detail="User not found in token")
        return {"user_id": user_id, "token": token}        
    except:
        raise HTTPException(status_code=403, detail="Invalid or expired token")

def get_current_user(token: str = Security(security)):
    payload = verify_jwt_token(token.credentials)
    return payload
