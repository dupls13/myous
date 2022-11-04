""" connect to database with sqlalchemy """


from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
#import psycopg2
from datetime import time 

# Connect to database 
SQLALCHEMY_DATABASE_URL = 1234 

# Create engine, establish connection 
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Make session 
SessionLocal = sessionmaker(autocommit = False, autoflush = False, bind = engine)

# Base class 
Base = declarative_base()

def get_db(): 
    db = SessionLocal
    try: 
        yield db 
    finally: 
        db.close()