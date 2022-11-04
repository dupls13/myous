# routes/posts.py
""" Routes for posts """


from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session 

from schemas.posts import PostBase, PostCreate, PostOut 

router = APIRouter(
    prefix= 'posts', 
    tags=['Posts']
)

# Get
@router.get('/', response_model = PostOut)
def get_all_posts(db):
    posts = 1
    return posts 

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