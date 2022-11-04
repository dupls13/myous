from pydantic import BaseModel, EmailStr 
from datetime import datetime 
from users import UserOut


class PostBase(BaseModel): 
    title: str 
    content: str 
    id: int 

class Post(PostBase): 
    id: int 
    create_at: datetime
    
    owner_id: int 
    owner: UserOut 
    
    class Config: 
        pass 
    
class PostCreate(PostBase):
    title: str 
    content: str 

class PostOut(BaseModel): 
    Post: Post 
    votes: int 
    
    class Config: 
        pass 
    
