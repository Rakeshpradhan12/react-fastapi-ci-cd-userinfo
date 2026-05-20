from pydantic import BaseModel, EmailStr, field_validator
from typing import Optional

class UserCreate(BaseModel):
  name: str
  email: EmailStr
  password: str
  
  @field_validator('name')
  @classmethod
  def name_must_not_be_empty(cls, v):
    if not v or not v.strip():
      raise ValueError('Name cannot be empty')
    return v.strip()
  
  @field_validator('password')
  @classmethod
  def password_must_be_strong(cls, v):
    if len(v) < 6:
      raise ValueError('Password must be at least 6 characters long')
    return v

class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    
    @field_validator('name')
    @classmethod
    def name_must_not_be_empty(cls, v):
      if v is not None and (not v or not v.strip()):
        raise ValueError('Name cannot be empty')
      return v.strip() if v else v

class UserResponse(BaseModel):
  id: int
  name: str
  email: str

  class Config:
    from_attributes=True