# routes/users.py
""" Route paths for users """


from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from typing import List

# Ugly locations 
from schemas.users_s import UserCreate, UserLogin, UserOut, User
from database import get_db
from models.users_m import User as modelu

# Creating base router to connect to main.py
# Gives prefix: part of html ie www.blah/<prefix>/
# Tags: where organized in html/docs
router = APIRouter(
    prefix='/users', 
    tags = ['Users']
)

template = Jinja2Templates(directory="templates")

# Get Users (admin)
# Router path for '/' when searched using router.get
# Response model: gives user reply back
# List[UserOut]: going from batabse to user, 
#   needs to convert to list, following schemas.users_s schema
@router.get('/', response_model = List[UserOut], response_class=HTMLResponse)
# Creating function, need to make Session(orm) 
# Depends: dependency injection: ???
def get_users(db: Session = Depends(get_db)):
    # Grabs all data, from modelu(database)
    all_users = db.query(modelu).all()
    return all_users
    return templates.TemplateResponse("create_user.html")
    
# Get specific user based on username

@router.get('/{username}', response_model = UserOut, response_class=HTMLResponse)
# username: str: needs to compare to modelu
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
    return templates.TemplateResponse("create_user.html", {"request": request, "username": username})
     

# Create User
# post function 
# status code for successful user creation
@router.post('/create', status_code=status.HTTP_201_CREATED, response_model= UserCreate)
def create_user(user: User, db: Session = Depends(get_db)):
    
    # Create new user based on the model, automatically organize
    new_user = modelu(**user.dict())
    
    # Update db 
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return new_user



