# add
# delete
# edit
# list single book
# list all the books
from fastapi import APIRouter

router = APIRouter()
@router.get("/")
def display_books():
    return {"message": "Display all the books"}
