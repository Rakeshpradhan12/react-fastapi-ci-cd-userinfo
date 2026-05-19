from passlib.context import CryptContext

pwd_context= CryptContext(schemes=['bcrypt'], deprecated='auto')

def verify_password(plain_password, hashes_password):
  return pwd_context.verify(plain_password, hashes_password)
def get_hashed_password(plain_password):
  return pwd_context.hash(plain_password)