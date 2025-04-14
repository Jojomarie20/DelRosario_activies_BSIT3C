import bcrypt

# Hash the password with bcrypt
def hash_password(password: str) -> str:
    salt = bcrypt.gensalt()  # Generates a salt
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)  # Hash the password with the salt
    return hashed.decode('utf-8')  # Return the hashed password as a string

# Verify the password against the hashed password
def verify_password(plain_password: str, hashed_password: str) -> bool:
    # Check if the password matches the stored hash
    return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))
