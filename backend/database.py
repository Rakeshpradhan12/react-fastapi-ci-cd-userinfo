from dotenv import load_dotenv
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from fastapi import HTTPException
import time
from sqlalchemy.exc import OperationalError

load_dotenv()

def get_db():
  db=SessionLocal()
  try:
    yield db
  except ConnectionError:
    raise HTTPException(status_code=500, detail='internal server error')
  finally:
    db.close()




DATABASE_URL=os.getenv('DATABASE_URL')

for i in range(10):
    try:
        engine = create_engine(DATABASE_URL)
        connection = engine.connect()
        print("Database connected")
        connection.close()
        break
    except OperationalError:
        print("Database not ready, retrying...")
        time.sleep(5)
        
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

Base=declarative_base()


# print(engine)
# with engine.connect() as con:
#   print('connected ')