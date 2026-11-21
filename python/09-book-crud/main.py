from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field, field_validator

app = FastAPI()

BOOKS = {}
next_id = 1

class CreateBook(BaseModel):
    title: str = Field(..., min_length=1, max_length=100)
    author: str = Field(..., min_length=1, max_length=100)
    year: int = Field(ge = 1, le = 2026)

    @field_validator('title')
    @classmethod
    def title_strip(cls, value):
        if value.strip() == "":
            raise ValueError("имя не может состоять только из пробелов")
        return value

@app.get("/books")
def show_books():
    return list(BOOKS.values())

@app.get("/books/{book_id}")
def show_book(book_id: int):
    if book_id not in BOOKS:
        raise HTTPException(
            status_code=404,
            detail=f"Book {book_id} not found"
        )
    return BOOKS[book_id]

@app.post("/books", status_code =201)
def create_book(book: CreateBook):
    global next_id
    book_dict = {
        "id": next_id,
        "title": book.title,
        "author": book.author,
        "year": book.year
    }
    BOOKS[next_id] = book_dict
    next_id += 1
    return book_dict

@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    if book_id not in BOOKS:
        raise HTTPException(
            status_code=404,
            detail=f"Book {book_id} not found"
        )
    book = BOOKS.pop(book_id)
    return book