# routes/posts.py
""" Routes for posts """


from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session 
from typing import List

from database import get_db
from schemas.posts_s import Post, PostBase, PostCreate, PostOut 
from models.posts_m import Post as modelp


router = APIRouter(
    prefix= '/posts', 
    tags=['Posts']
)

# Get
@router.get('/', response_model = List[PostOut])
def get_all_posts(db: Session = Depends(get_db)):
    all_posts = db.query(modelp).all()
    
    return all_posts

@router.get("/{id}", response_model = PostOut)
def get_specific_post(post: PostOut):
    pass 



# Create 
@router.post("/create", response_model = PostCreate)
def create_post(post: PostCreate, db:Session = Depends(get_db)): 
    
    new_post = modelp(**post.dict())
    # Todo: match current user id to owner id to line above 
    
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post
        

# Update 
@router.put("/{id}}", response_model= PostOut)
def update_post(id: int, updated_post: PostCreate):
    pass

# Delete 
@router.delete("/{id}")
def delete_specific_post(id: int):
    pass 