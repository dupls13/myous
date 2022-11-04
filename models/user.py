# models/users.py
""" sqlalchemy models for database """

from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text 
from sqlalchemy.orm import relationship 

class User(): 
    pass 