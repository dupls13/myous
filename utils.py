# utils.py
""" Used to hash passwords for users using passlib """

from passlib.context import CryptContext

# Encryption method 
pw_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Function for hashing password that will be used in routers
def hash(password: str): 
    return pw_context.hash(password)