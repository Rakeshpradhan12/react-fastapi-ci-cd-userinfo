# Deployment Notes

## Recent Changes

### Database Schema Updates
- Added `unique=True` constraint to `name` and `email` columns in the `Emp` model
- Made `email` field `nullable=False`

### New Dependencies
- Added `pydantic[email]` for email validation

### Validation Improvements
- Email addresses are now validated using `EmailStr`
- Password must be between 6-72 characters (bcrypt limit)
- Name cannot be empty
- Improved password hashing with proper byte handling

### Bug Fixes
- Fixed bcrypt 72-byte password limit handling
- Added robust error handling for password hashing
- Fixed typo in `verify_password` function parameter name

## Deployment Steps

### For Render.com or Production Deployment:

**IMPORTANT: You must redeploy your application for these fixes to take effect!**

1. **Clear Existing Database** (Recommended if you have test data)
   - On Render.com dashboard, go to your PostgreSQL database
   - Delete and recreate the database, OR
   - Run: `DROP TABLE emp;` to clear the table

2. **Redeploy the Application**
   - Push changes to your git repository
   - Render will automatically redeploy
   - OR manually trigger a deploy from Render dashboard

3. **Verify Dependencies are Installed**
   ```bash
   pip install -r requirements.txt
   ```

### Alternative: Migrate Existing Data

If you need to keep existing data:

1. **Run Database Migration**
   ```bash
   python migrate_db.py
   ```
   This will:
   - Remove duplicate usernames and emails
   - Add unique constraints
   - Fix NULL email values

2. **Restart the Application**

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
