# Deployment Checklist

## Current Status
✅ All code fixes applied locally
❌ Production server needs redeployment

## Issues Fixed in This Update

1. ✅ Backend Dockerfile - Correct port (8000)
2. ✅ Database URL - Uses 'db' service name for Docker
3. ✅ SECRET_KEY - Loads from environment variables
4. ✅ Email validation - Uses EmailStr with proper validation
5. ✅ Password validation - 6-72 character limit
6. ✅ Password hashing - Handles bcrypt 72-byte limit
7. ✅ Unique constraints - Added to username and email
8. ✅ Error handling - Comprehensive logging and error messages
9. ✅ Duplicate checks - Prevents duplicate users/emails

## To Deploy to Production (Render.com)

### Step 1: Commit and Push Changes
```bash
git add .
git commit -m "Fix authentication, validation, and database issues"
git push origin main
```

### Step 2: Clear Production Database
**Option A: Via Render Dashboard**
1. Go to https://dashboard.render.com
2. Select your PostgreSQL database
3. Click "Delete" and recreate, OR
4. Use the Shell to run: `DROP TABLE emp;`

**Option B: Via SQL Client**
```sql
DROP TABLE IF EXISTS emp CASCADE;
```

### Step 3: Redeploy Application
1. Go to your backend service on Render
2. Click "Manual Deploy" → "Deploy latest commit"
3. Wait for deployment to complete (check logs)

### Step 4: Verify Deployment
Test the API with a valid request:
```bash
curl -X POST https://your-app.onrender.com/users \
  -H "Content-Type: application/json" \
  -d '{
    "name": "testuser",
    "email": "test@example.com",
    "password": "test123"
  }'
```

Expected response (200):
```json
{
  "id": 1,
  "name": "testuser",
  "email": "test@example.com"
}
```

## For Local Docker Testing

```bash
# Stop and remove everything
docker-compose down -v

# Rebuild and start
docker-compose up --build

# Test the API
curl -X POST http://localhost:8000/users \
  -H "Content-Type: application/json" \
  -d '{
    "name": "testuser",
    "email": "test@example.com",
    "password": "test123"
  }'
```

## Common Errors After Deployment

### 422 Validation Error
- **Cause**: Invalid email format
- **Fix**: Use format like `user@example.com`

### 400 "Username already exists"
- **Cause**: User already registered
- **Fix**: Use different username or email

### 401 "Invalid credentials"
- **Cause**: Wrong username/password during login
- **Fix**: Check credentials or register new user

### 500 "Database error"
- **Cause**: Old database schema or corrupted data
- **Fix**: Clear database and redeploy

## Testing the Full Flow

1. **Register a user**
   ```bash
   POST /users
   {
     "name": "john",
     "email": "john@example.com",
     "password": "john123"
   }
   ```

2. **Login**
   ```bash
   POST /token
   Form data:
   - username: john
   - password: john123
   ```
   
   Response: `{"access_token": "...", "token_type": "bearer"}`

3. **Get profile**
   ```bash
   GET /users/me
   Headers:
   - Authorization: Bearer <access_token>
   ```

4. **Update profile**
   ```bash
   PATCH /users/me
   Headers:
   - Authorization: Bearer <access_token>
   Body:
   {
     "name": "John Doe",
     "email": "johndoe@example.com"
   }
   ```

## Files Changed
- `backend/.env` - Fixed DATABASE_URL and added SECRET_KEY
- `backend/Dockerfile` - Fixed exposed port
- `backend/main.py` - Added logging
- `backend/models.py` - Added unique constraints
- `backend/schema.py` - Added email and password validation
- `backend/auth.py` - Load SECRET_KEY from env
- `backend/dependencies.py` - Load SECRET_KEY from env
- `backend/crud.py` - Added duplicate checks and error handling
- `backend/utils.py` - Fixed password hashing with bcrypt limits
- `backend/requirements.txt` - Added pydantic[email]

## New Files
- `backend/migrate_db.py` - Database migration script
- `backend/DEPLOYMENT_NOTES.md` - Detailed deployment guide
- `DEPLOYMENT_CHECKLIST.md` - This file
