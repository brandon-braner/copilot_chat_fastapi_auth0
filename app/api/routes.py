from fastapi import APIRouter, Depends, HTTPException, status
from .auth import get_current_user
from ..models.user import User

router = APIRouter()

@router.get("/")
def read_root():
    return {"Hello": "World"}

@router.get("/users/me")
def read_user_me(current_user: User = Depends(get_current_user)):
    return current_user

@router.get("/users/{user_id}")
def read_user(user_id: str):
    if user_id != "me":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Not a valid user.")
    return {"user_id": user_id}