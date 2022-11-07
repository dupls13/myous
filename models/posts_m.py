# models/posts.py
""" sqlalchemy (ORM) models for posts """

from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text 
from sqlalchemy.orm import relationship 

from database import Base 
from . import users_m

class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key = True, nullable = False)
    title = Column(String, nullable = False)
    content = Column(String, nullable = False)
    
    user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'), nullable = False)
    
    owner = relationship("User")