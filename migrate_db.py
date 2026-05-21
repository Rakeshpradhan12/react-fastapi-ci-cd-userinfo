"""
Database migration script to add unique constraints to existing tables
Run this script to update your database schema without losing data
"""
from sqlalchemy import text
from database import engine
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def migrate_database():
    """Add unique constraints to name and email columns"""
    with engine.connect() as conn:
        try:
            # Check if table exists
            result = conn.execute(text(
                "SELECT EXISTS (SELECT FROM information_schema.tables WHERE table_name = 'emp')"
            ))
            table_exists = result.scalar()
            
            if not table_exists:
                logger.info("Table 'emp' does not exist yet. No migration needed.")
                return
            
            # Remove duplicate names (keep first occurrence)
            logger.info("Removing duplicate usernames...")
            conn.execute(text("""
                DELETE FROM emp a USING emp b
                WHERE a.id > b.id AND a.name = b.name
            """))
            
            # Remove duplicate emails (keep first occurrence)
            logger.info("Removing duplicate emails...")
            conn.execute(text("""
                DELETE FROM emp a USING emp b
                WHERE a.id > b.id AND a.email = b.email
            """))
            
            # Update NULL emails to a placeholder
            logger.info("Updating NULL emails...")
            conn.execute(text("""
                UPDATE emp SET email = CONCAT('user_', id, '@placeholder.com')
                WHERE email IS NULL OR email = ''
            """))
            
            # Add unique constraint to name if not exists
            logger.info("Adding unique constraint to name column...")
            try:
                conn.execute(text("""
                    ALTER TABLE emp ADD CONSTRAINT emp_name_key UNIQUE (name)
                """))
            except Exception as e:
                if "already exists" in str(e):
                    logger.info("Unique constraint on name already exists")
                else:
                    raise
            
            # Add unique constraint to email if not exists
            logger.info("Adding unique constraint to email column...")
            try:
                conn.execute(text("""
                    ALTER TABLE emp ADD CONSTRAINT emp_email_key UNIQUE (email)
                """))
            except Exception as e:
                if "already exists" in str(e):
                    logger.info("Unique constraint on email already exists")
                else:
                    raise
            
            # Make email NOT NULL if it isn't already
            logger.info("Making email column NOT NULL...")
            try:
                conn.execute(text("""
                    ALTER TABLE emp ALTER COLUMN email SET NOT NULL
                """))
            except Exception as e:
                logger.warning(f"Could not set email to NOT NULL: {e}")
            
            conn.commit()
            logger.info("Migration completed successfully!")
            
        except Exception as e:
            conn.rollback()
            logger.error(f"Migration failed: {str(e)}")
            raise

if __name__ == "__main__":
    migrate_database()
