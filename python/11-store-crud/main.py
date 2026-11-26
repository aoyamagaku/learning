from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class CreateBook(BaseModel):
    title: str
    author: str

books = [
    {
        "id": 1,
        "title": "Асинк в Python",
        "author": "Мэттью",
    },
    {
        "id": 2,
        "title": "Backend разработка в Python",
        "author": "Данек",
    }
]

@app.get("/books", tags=["Книги"], summary="Получить все книги")
def show_books():
    return books

@app.get("/books/{id}", tags=["Книги"], summary="Получить книгу")
def show_book(id: int)->dict:
    for book in books:
        if book["id"] == id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")

@app.post("/books/create")
def create_book(book: CreateBook):
    new_book = {
        "id": len(books) + 1,
        "title": book.title,
        "author": book.author
    }
    books.append(new_book)
    return new_book

@app.put("/books/{id}")
def update_book(id: int, book: CreateBook):
    for existing_book in books:
        if existing_book["id"] == id:
            existing_book["title"] = book.title
            existing_book["author"] = book.author
            return existing_book

    raise HTTPException(status_code=404, detail="Book not found")

@app.delete("/books/{id}")
def delete_book(id: int):
    for book in books:
        if book["id"] == id:
            books.remove(book)
            return {"message": f"Вы удалили кингу {book}"}

    raise HTTPException(status_code=404, detail="Book not found")