from passlib.context import CryptContext
import logging

logger = logging.getLogger(__name__)

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

def verify_password(plain_password, hashed_password):
  try:
    # Ensure password is within bcrypt limits
    if len(plain_password.encode('utf-8')) > 72:
      plain_password = plain_password[:72]
    return pwd_context.verify(plain_password, hashed_password)
  except Exception as e:
    logger.error(f"Error verifying password: {str(e)}")
    return False

def get_hashed_password(plain_password):
  try:
    # Bcrypt has a 72 byte limit, truncate if necessary
    password_bytes = plain_password.encode('utf-8')
    if len(password_bytes) > 72:
      # Truncate to 72 bytes, being careful with multi-byte characters
      plain_password = password_bytes[:72].decode('utf-8', errors='ignore')
    return pwd_context.hash(plain_password)
  except Exception as e:
    logger.error(f"Error hashing password: {str(e)}")
    raise ValueError(f"Failed to hash password: {str(e)}")