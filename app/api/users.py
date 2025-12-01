# list user
# register
# login
from fastapi import APIRouter

router = APIRouter()
@router.get("/")
def display_user():
    return {"message": "This is the current user"}
