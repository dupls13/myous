# routes/users.py
""" Route paths for users """


from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from typing import List

from schemas.users_s import UserCreate, UserLogin, UserOut, User
from database import get_db
from models.users_m import User as modelu

router = APIRouter(
    prefix='/users', 
    tags = ['Users']
)

# Get Users (admin)
@router.get('/', response_model = List[UserOut])
def get_users(db: Session = Depends(get_db)):
    all_users = db.query(modelu).all()
    return all_users
    
# Get specific user
@router.get('/{username}', response_model = UserOut)
def get_specific_user(username: str, db: Session = Depends(get_db)):
    
    # Filter through models db, match username  
    user = db.query(modelu).filter(modelu.username == username).first()
    
    # Raise error
    if not user: 
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"User with username {username} does not exist"
        )
    
    return user 
     

# Create User
@router.post('/create', response_model= UserCreate)
def create_user(user: User, db: Session = Depends(get_db)):
    
    # Create new user based on the model, automatically organize 
    new_user = modelu(**user.dict())
    
    # Update db 
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return new_user



