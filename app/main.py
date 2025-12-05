from fastapi import FastAPI
from app.api import users, books
from sqlmodel import SQLModel, Session
from app.models.tables import User,Book


app = FastAPI(title="BookBound")

app.include_router(users.router, prefix="/users")
app.include_router(books.router, prefix="/books")

@app.get("/")
def root():
    return {"message": "Book API is running!"}