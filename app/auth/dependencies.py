import os
from typing import Union
from app.models.users import *
from app.database_connection.connection import *
from dotenv import load_dotenv
from jose import JWTError, jwt 
from app.models.users import User
from passlib.context import CryptContext
from fastapi import Depends, HTTPException
from datetime import datetime, timedelta, timezone
from fastapi.security import HTTPBearer,HTTPAuthorizationCredentials

load_dotenv()

key_DB = os.getenv('AES_DB_ECNRYPTION_KEY')
iv =  os.getenv('AES_IV_KEY').encode('utf-8')
SECRET_KEY = os.getenv('JWT_SECRET_KEY')
ALGORITHM = os.getenv("JWT_ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = 24 * 60
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = HTTPBearer()

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def hash_password(password):
    return pwd_context.hash(password)

def get_user(db, username: str):
    if username in db:
        user_dict = db[username]
        return User(**user_dict)

def authenticate_user(password):
    user_identity = password
    if user_identity is not None:
        if verify_password(password, user_identity):
            return user_identity
    return False

def create_access_token(data: dict, expires_delta: Union[timedelta, None] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def id_exists(user_id):
    try:
        id_ex = db.query(User).filter_by(id=user_id).first()
        return id_ex
    except:
        return None
 
async def get_current_user(auth_credentials: HTTPAuthorizationCredentials = Depends(oauth2_scheme)):
    try:
        if auth_credentials:
            token = auth_credentials.credentials
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            id: str = payload.get("sub")
            if id is None:
                raise HTTPException(
            status_code=401,
            detail={"message":"authorization_errors","errors":["Could not validate credentials"]}
        )
            if not id_exists(id):
                raise HTTPException(
            status_code=401,
            detail={"message":"authorization_errors","errors":["Could not validate credentials"]}
        )
            return id
    except JWTError:
        raise HTTPException(
            status_code=401,
            detail={"message":"authorization_errors","errors":["Could not validate credentials"]}
        )
    