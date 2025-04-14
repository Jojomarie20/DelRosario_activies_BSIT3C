# First Project API Documentation

## Authentication Endpoints

### Register a New User

- **Method**: POST
- **URL**: `/api/users/register/`
- **Description**: Creates a new user account and returns a JWT token.
- **Request Body** (form-data):
  ```
  username: string (required)
  password: string (required)
  email: string (required, must be valid email)
  name: string (required)
  ```
- **Response**:
  - Success (200 OK):
    ```json
    {
      "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MiwidXNlcm5hbWUiOiJ0ZXN0dXNlciIsImV4cCI6MTY1MDEyMzQ1NiwiaWF0IjoxNjUwMDM3MDU2fQ.2jPYQIEgkYXHpSJr6jUp5MG72zRdQ3R7SzTd4YKR8bs"
    }
    ```
  - Error (400 Bad Request):
    ```json
    {
      "error": {
        "username": ["Username already exists"],
        "email": ["Email already exists"]
      }
    }
    ```

### User Login

- **Method**: POST
- **URL**: `/api/users/login/`
- **Description**: Authenticates a user and returns a JWT token.
- **Request Body** (form-data):
  ```
  username: string (required)
  password: string (required)
  ```
- **Response**:
  - Success (200 OK):
    ```json
    {
      "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MiwidXNlcm5hbWUiOiJ0ZXN0dXNlciIsImV4cCI6MTY1MDEyMzQ1NiwiaWF0IjoxNjUwMDM3MDU2fQ.2jPYQIEgkYXHpSJr6jUp5MG72zRdQ3R7SzTd4YKR8bs"
    }
    ```
  - Error (400 Bad Request):
    ```json
    {
      "error": {
        "__all__": ["User does not exist or incorrect password"]
      }
    }
    ```

### Access Protected Route

- **Method**: GET
- **URL**: `/api/users/protected/`
- **Description**: Returns user information for authenticated users.
- **Headers**:
  ```
  Authorization: Bearer <jwt_token>
  ```
- **Response**:
  - Success (200 OK):
    ```json
    {
      "message": "You accessed a protected route",
      "user": {
        "id": 1,
        "username": "testuser",
        "email": "test@example.com",
        "name": "Test User"
      }
    }
    ```
  - Error (401 Unauthorized):
    ```json
    {
      "error": "No token provided"
    }
    ```
    or
    ```json
    {
      "error": "Invalid or expired token"
    }
    ```
  - Error (404 Not Found):
    ```json
    {
      "error": "User not found"
    }
    ```

## Alternative Authentication Endpoints (v2)

The same authentication endpoints are also available under the v2 API:

- **Register**: `/api/v2/auth/register/`
- **Login**: `/api/v2/auth/login/`
- **Protected**: `/api/v2/auth/protected/`

These endpoints have the same request/response formats as their v1 counterparts.



