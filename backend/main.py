from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
import models, schema , crud
from database import SessionLocal, engine, get_db
from auth import authenticate_user, create_access_token
from dependencies import get_current_user
from fastapi.middleware.cors import CORSMiddleware
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

models.Base.metadata.create_all(bind=engine)


app=FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"]
)


@app.get('/')
def home():
  return ('welcome to home page guys')


@app.post('/users', response_model=schema.UserResponse)
def create_user(emp:schema.UserCreate, db:Session=Depends(get_db)):
  try:
    return crud.create_user(db, emp)
  except HTTPException:
    raise
  except Exception as e:
    logger.error(f"Unexpected error in create_user: {str(e)}")
    raise HTTPException(status_code=500, detail=f'Failed to create user: {str(e)}')


@app.post('/token')
async def login(form_data:OAuth2PasswordRequestForm=Depends(), db:Session=Depends(get_db)):
  emp = authenticate_user(form_data.username, form_data.password, db)
  if not emp:
    raise HTTPException(status_code=401, detail='invalid credentials')
  token = create_access_token({'sub': emp.name})
  return {'access_token': token, 'token_type': 'bearer'}


@app.get('/users', response_model= list[schema.UserResponse])
def read_users(db:Session = Depends(get_db)):
  return crud.get_users(db)


@app.get('/users/me', response_model= schema.UserResponse)
def read_user(db:Session = Depends(get_db), user:models.Emp=Depends(get_current_user)):
  return crud.get_user(db, user.name)


@app.patch('/users/me', response_model=schema.UserResponse)
def update_user( user_update:schema.UserUpdate, db:Session=Depends(get_db), user:models.Emp=Depends(get_current_user)):
  return crud.update_user(db, user, user_update)