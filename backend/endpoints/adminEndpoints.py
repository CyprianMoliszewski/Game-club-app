from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import jwt
from datetime import datetime, timedelta
from database.databaseHandler import verify_login

router = APIRouter()

SECRET_KEY = "54FJI149Fmmbm3t30KC39R39JVKVMWIDMVIAEJIRJT0if013jvncij1939ij)J)(j4v4n2)"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 15

class LoginData(BaseModel):
    username: str
    password: str

@router.post("/login")
def login(data: LoginData):
    user = verify_login(data.username, data.password)
    
    if not user:
        raise HTTPException(status_code=401, detail="Nieprawidłowy login lub hasło")

    expire = datetime.now() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    payload = {
        "sub": data.username,
        "role": user["user_role"],
        "exp": expire
    }
    encoded_jwt = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    
    return {"access_token": encoded_jwt, "token_type": "bearer"}
