from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from fastapi import Depends, HTTPException
import crud
from database import get_db
from dotenv import load_dotenv
import os

load_dotenv()

oauth2_scheme=OAuth2PasswordBearer(tokenUrl='/token')

SECRET_KEY = os.getenv('SECRET_KEY', 'my_s')
ALGORITHM = 'HS256'
def get_current_user(token:str=Depends(oauth2_scheme), db=Depends(get_db)):
  try:
    payload=jwt.decode(token , SECRET_KEY, algorithms=[ALGORITHM])
    username=payload['sub']
    if not username:
      raise HTTPException(status_code=401, detail='invalid token')
  except JWTError:
    raise HTTPException(status_code=401, detail='invalid token')

  user = crud.get_user(db, username)
  if not user:
    raise HTTPException(status_code=401, detail='invalid token')
  return user