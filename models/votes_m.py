# models/votes.py
""" sqlalchemy (ORM) for votes table """

from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text 
from sqlalchemy.orm import relationship 

from database import Base 

class Votes(Base):
    __tablename__ = 'votes'
    user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'), primary_key = True)
    post_id = Column(Integer, ForeignKey("posts.id", ondelete = 'CASCADE'), primary_key = True)