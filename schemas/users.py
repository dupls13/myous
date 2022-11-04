# schemas/users.py
""" Pydantic models (schemas) for Users """


from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import test 


from pydantic import BaseModel, EmailStr 
from datetime import datetime 


class UserCreate(BaseModel):
    email: EmailStr
    username: str
    password: str
    
class UserLogin(BaseModel): 
    email: EmailStr
    password: str
    
class UserOut(BaseModel): 
    id: int 
    email: EmailStr
    created_at: datetime 
    
    class Config: 
        pass
    
    
    
    
