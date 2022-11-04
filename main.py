from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
import uvicorn 

from .routes import users, posts

# Initialize 
app = FastAPI()

# Connect routers
app.include_router(users.router)
app.include_router(posts.router)


def root(): 
    return {
        "message": "Welcome to myous" 
    }


# Start by "python main.py"
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port = 8080, reload = True)
