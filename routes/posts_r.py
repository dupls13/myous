# routes/posts.py
""" Routes for posts """


from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session 

from database import get_db
from schemas.posts_s import PostBase, PostCreate, PostOut 
from models.posts_m import Post as modelp


router = APIRouter(
    prefix= '/posts', 
    tags=['Posts']
)

# Get
@router.get('/', response_model = PostOut)
def get_all_posts(db: Session = Depends(get_db)):
    all_posts = db.query(modelp).all()
    
    return all_posts

@router.get("/{id}", response_model = PostOut)
def get_specific_post(post: PostOut):
    pass 



# Create 
@router.post("/", response_model = PostCreate)
def create_post(post: PostCreate): 
    pass 
        

# Update 
@router.put("/{id}}", response_model= PostOut)
def update_post(id: int, updated_post: PostCreate):
    pass

# Delete 
@router.delete("/{id}")
def delete_specific_post(id: int):
    pass 