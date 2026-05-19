import crud
from sqlalchemy.orm import Session
from utils import verify_password
from jose import jwt
from datetime import timedelta, datetime, timezone
from dotenv import load_dotenv
import os

load_dotenv()


def find_user(username:str, db:Session):
  users = crud.get_users(db)
  for emp in users:
    if emp.name == username:
      return emp
  return None


def authenticate_user(username: str, password: str, db: Session):
    emp = find_user(username, db)
    if not emp:
        return False
    pwd = verify_password(password, emp.password)
    if not pwd:
        return False
    return emp


SECRET_KEY='my_s'
ALGORITHM='HS256'

def create_access_token(data:dict):
  to_encode=data.copy()
  expire=datetime.now(timezone.utc)+timedelta(minutes=20)
  to_encode.update({'exp':expire})
  return jwt.encode(to_encode, SECRET_KEY , algorithm=ALGORITHM)
