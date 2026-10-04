from fastapi import FastAPI

from fastapi.exceptions import HTTPException

from models import BookCreate, BookUpdate,BookResponse

app = FastAPI()

from database import *

@app.get("/")
async def root():
    return ["Hi! You are on the main page"]

@app.get("/books")
def get_books():
    return get_all_books()

@app.get("/books/{book_id}", response_model=BookResponse)
def get_book_id(book_id: int):
    book = get_a_book_by_id(book_id)

    if book is None:
        raise HTTPException(
            status_code=404,
            detail="Book not found"
        )

    return book

@app.get("/books/title/{book_title}", response_model=BookResponse)
def get_book_title(book_title: str):
    book = get_a_book_by_title(book_title)

    if book is None:
        raise HTTPException(
            status_code=404,
            detail="Book not found"
        )

    return book

@app.post("/books", response_model=BookResponse)
def create_book(book: BookCreate):
    return create_a_book(book.title, book.author)

@app.put("/books/{book_id}", response_model=BookResponse)
def update_book(book_id: int, book: BookUpdate):
    book = update_a_book(book_id, book.title, book.author)

    if book is None:
        raise HTTPException(
            status_code=404,
            detail="Book not found"
        )

    return book

@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    result = delete_a_book(book_id)

    if result is None:
        raise HTTPException(
            status_code=404,
            detail="Book not found"
        )

    return result

