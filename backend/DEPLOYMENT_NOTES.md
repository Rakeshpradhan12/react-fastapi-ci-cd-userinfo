# Deployment Notes

## Recent Changes

### Database Schema Updates
- Added `unique=True` constraint to `name` and `email` columns in the `Emp` model
- Made `email` field `nullable=False`

### New Dependencies
- Added `pydantic[email]` for email validation

### Validation Improvements
- Email addresses are now validated using `EmailStr`
- Password must be at least 6 characters
- Name cannot be empty

## Deployment Steps

### For Render.com or Production Deployment:

1. **Update Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run Database Migration** (if you have existing data)
   ```bash
   python migrate_db.py
   ```
   This will:
   - Remove duplicate usernames and emails
   - Add unique constraints
   - Fix NULL email values

3. **Restart the Application**
   - The application will automatically create tables with the new schema if starting fresh

### For Docker Deployment:

1. **Rebuild the containers**
   ```bash
   docker-compose down -v  # Remove volumes to start fresh
   docker-compose up --build
   ```

### Common Issues:

**500 Error on User Creation:**
- Cause: Existing database has duplicate emails/usernames or NULL emails
- Solution: Run `migrate_db.py` or drop and recreate the database

**422 Validation Error:**
- Cause: Invalid email format (e.g., "user.com" instead of "user@example.com")
- Solution: Use valid email addresses in requests

**400 Error "Username/Email already exists":**
- Cause: Trying to register with existing credentials
- Solution: Use different username or email

## Testing

Valid user creation request:
```json
{
  "name": "testuser",
  "email": "testuser@example.com",
  "password": "password123"
}
```

Invalid requests that will fail:
```json
// Invalid email
{"name": "user", "email": "user.com", "password": "pass123"}

// Password too short
{"name": "user", "email": "user@test.com", "password": "12345"}

// Empty name
{"name": "", "email": "user@test.com", "password": "pass123"}
```
