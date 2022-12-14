from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from schemas.votes_s import Vote

router = APIRouter(
    prefix = "/vote", 
    tags = ['Vote']
)

# Vote logic 
@router.post('/')
def vote(vote: Vote):
    pass