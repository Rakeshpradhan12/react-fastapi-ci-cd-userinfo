from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException
import  models, schema
from utils import get_hashed_password
import logging

logger = logging.getLogger(__name__)

def create_user(db: Session, emp: schema.UserCreate):
  try:
    # Check if user already exists
    existing_user = db.query(models.Emp).filter(models.Emp.name == emp.name).first()
    if existing_user:
      raise HTTPException(status_code=400, detail='Username already exists')
    
    existing_email = db.query(models.Emp).filter(models.Emp.email == emp.email).first()
    if existing_email:
      raise HTTPException(status_code=400, detail='Email already exists')

    # Hash the password
    try:
      hashed_pwd = get_hashed_password(emp.password)
    except ValueError as e:
      raise HTTPException(status_code=400, detail=str(e))
    
    db_user = models.Emp(name=emp.name, email=emp.email, password=hashed_pwd)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
  except HTTPException:
    raise
  except IntegrityError as e:
    db.rollback()
    logger.error(f"IntegrityError creating user: {str(e)}")
    raise HTTPException(status_code=400, detail='Username or email already exists')
  except Exception as e:
    db.rollback()
    logger.error(f"Error creating user: {str(e)}")
    raise HTTPException(status_code=500, detail=f'Database error: {str(e)}')


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