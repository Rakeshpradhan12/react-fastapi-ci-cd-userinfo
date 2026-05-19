from sqlalchemy import Column, Integer, String
from database import Base

class Emp(Base):

  __tablename__='emp'

  id = Column(Integer, primary_key=True, index=True)
  name = Column(String, nullable=False)
  email=Column(String)
  password = Column(String, nullable=False)

#  print(Base.metadata.tables.keys())