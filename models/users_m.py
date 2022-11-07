# models/users.py
""" sqlalchemy (ORM) models for database """
""" After database creation """

from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text 
from sqlalchemy.orm import relationship 

from database import Base 

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key= True, nullable = False)
    email = Column(String, nullable = False, unique = True)
    username = Column(String, nullable = False, unique = True)
    password = Column(String, nullable = False)
 