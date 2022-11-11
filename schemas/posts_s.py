from pydantic import BaseModel, EmailStr
from datetime import datetime 
from typing import Optional 


class PostBase(BaseModel): 
    id: int
    title: str 
    content: str 


class Post(PostBase): 
    id: int 
    #create_at: datetime
    
    #owner_id: int 
    
    class Config: 
        pass 
    
class PostCreate(BaseModel):
    title: str 
    content: str 
    
    class Config: 
        orm_mode = True

class PostOut(BaseModel): 
    id: int 
    title: str 
    content: str
    
    class Config: 
        orm_mode = True
    
