from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException
import  models, schema
from utils import get_hashed_password

def create_user(db:Session , emp:schema.UserCreate):
  # Check if user already exists
  existing_user = db.query(models.Emp).filter(models.Emp.name == emp.name).first()
  if existing_user:
    raise HTTPException(status_code=400, detail='Username already exists')
  
  existing_email = db.query(models.Emp).filter(models.Emp.email == emp.email).first()
  if existing_email:
    raise HTTPException(status_code=400, detail='Email already exists')

  hashed_pwd = get_hashed_password(emp.password)
  db_user= models.Emp(name = emp.name, email=emp.email, password=hashed_pwd)
  db.add(db_user)
  try:
    db.commit()
    db.refresh(db_user)
  except IntegrityError:
    db.rollback()
    raise HTTPException(status_code=500, detail='Failed to create user')
  return db_user


def get_users(db:Session):
  return db.query(models.Emp).all()


def get_user(db:Session, username:str):
  return db.query(models.Emp).filter(models.Emp.name==username).first()

def update_user(db:Session, user:models.Emp, user_update:schema.UserUpdate):
  if user_update.name is not None and user_update.name.strip():
    user.name = user_update.name
  if user_update.email is not None and user_update.email.strip():
    user.email = user_update.email
  db.commit()
  db.refresh(user)
  return user