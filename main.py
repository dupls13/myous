from fastapi import FastAPI, Request, Depends
from fastapi.templating import Jinja2Templates
import uvicorn
from passlib.context import CryptContext

from sqlalchemy.orm import Session 
from database import get_db
 

from routes import posts_r, users_r
from models import users_m, votes_m, posts_m
from database import engine 

#from database import connect_database


posts_m.Base.metadata.create_all(bind=engine)
users_m.Base.metadata.create_all(bind=engine)
votes_m.Base.metadata.create_all(bind=engine)


# Initialize 
app = FastAPI()

# Connect routers
app.include_router(users_r.router)
app.include_router(posts_r.router)


# Connect database 
# connect_database()


def root(): 
    return {
        "message": "Welcome to myous" 
    }
    
# test 
app.get("/test")
def test_post(db: Session = Depends(get_db)):
    return {
        "message": "Test"
    }


# Start by "python main.py"
if __name__ == "__main__":
    uvicorn.run("main:app", reload = True)
