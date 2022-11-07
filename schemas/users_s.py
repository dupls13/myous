# schemas/users.py
""" Pydantic models (schemas) for Users """


#from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
#from sqlalchemy.sql.sqltypes import TIMESTAMP


from pydantic import BaseModel
from datetime import datetime 


class UserCreate(BaseModel):
    email: str
    username: str
    password: str
    
class UserLogin(BaseModel): 
    email: str
    password: str
    
class UserOut(BaseModel): 
    id: int 
    email: str
    created_at: datetime 
    
    class Config: 
        pass
    
    
    
    
