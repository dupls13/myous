# schemas/users.py
""" Pydantic models (schemas) for Users """


#from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
#from sqlalchemy.sql.sqltypes import TIMESTAMP


from pydantic import BaseModel
from datetime import datetime 


class User(BaseModel):
    email: str
    username: str 
    password: str 

class UserCreate(BaseModel):
    username: str
    password: str
    
    # Needed in order to return this back to Postman
    # Without this, it would add to database, but give "Internal Error"
    # According to documentation, orm_mode will tell Pydantic model to return even if not a dict 
    class Config:
        orm_mode = True
    
class UserLogin(BaseModel): 
    email: str
    password: str
    
class UserOut(BaseModel):
    id: int 
    email: str
    username: str
    
    class Config:
        orm_mode = True
    
    
    
    
