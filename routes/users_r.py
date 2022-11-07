# routes/users.py
""" Route paths for users """


from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter

from schemas.users_s import UserCreate, UserLogin, UserOut

router = APIRouter(
    prefix='/users', 
    tags = ['Users']
)

# Get Users (admin)
@router.get('/', response_model = UserOut)
def get_users(id: int):
    pass
    
# Get specific user
@router.get('/{username}', response_model = UserOut)
def get_specific_user(username: str): 
    pass 

# Create User
@router.post('/create', response_model= UserCreate)
def create_user():
    pass 


