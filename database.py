""" connect to database with sqlalchemy """


from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


import psycopg2
# Used to get column name and values
from psycopg2.extras import RealDictCursor
from datetime import time 


"""
# Psycopg2
def connect_database():
    while True:
        try:
            conn = psycopg2.connect(
                host = '', 
                database = '', 
                user = '', 
                password = '',
                cursor_factory= RealDictCursor)

            cursor = conn.cursor()
            print("Connected")
            break
        except Exception as error: 
            print("Connection error ")
"""


# SQLAlchemy 
"""
SQLALCHEMY_DATABASE_URL = 'postgresql://<username>:<password>@<ipaddress/hostname>/<databasename>'
"""

# From SQLAlchemy
# Credentials for database collection 
# Should be hidden
SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:3875@localhost:5432/myous'
  

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit= False, autoflush= False, bind= engine)

Base = declarative_base()



def get_db(): 
    db = SessionLocal()
    try: 
        yield db 
    finally: 
        db.close()