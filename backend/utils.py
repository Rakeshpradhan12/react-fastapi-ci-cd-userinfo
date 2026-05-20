from passlib.context import CryptContext

pwd_context= CryptContext(schemes=['bcrypt'], deprecated='auto')

def verify_password(plain_password, hashed_password):
  return pwd_context.verify(plain_password, hashed_password)

def get_hashed_password(plain_password):
  # Bcrypt has a 72 byte limit, truncate if necessary
  if len(plain_password.encode('utf-8')) > 72:
    plain_password = plain_password[:72]
  return pwd_context.hash(plain_password)