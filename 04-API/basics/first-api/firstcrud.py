from fastapi import FastAPI
from fastapi.exceptions import HTTPException
from pydantic import BaseModel

app = FastAPI()

class Book(BaseModel):
    title: str
    author: str

books = [
    {"id": 1, "title": "1984", "author": "George Orwell"},
    {"id": 2, "title": "The Hobbit", "author": "J.R.R. Tolkien"},
    {"id": 3, "title": "Dune", "author": "Frank Herbert"}
]

@app.get("/")
async def read_root():
    return {"message": "Your First API!"}

@app.get("/books")
async def get_all_books():
    return books

@app.get("/books/{book_id}")
async def get_book_id(book_id: int):
    for book in books:
        if book["id"] == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")

@app.get("/books/{book_id}/author")
async def get_book_authors(book_id: int):
    for book in books:
        if book["id"] == book_id:
            return book["author"]
    raise HTTPException(404, "Book not found")

@app.post("/books")
def create_book(book: Book):
    new_book = {
        "id": len(books) + 1,
        "title": book.title,
        "author": book.author
    }

    books.append(new_book)

    return new_book

@app.put("/books/{book_id}")
def update_book(book_id: int, book: Book):
    for old_book in books:
        if old_book["id"] == book_id:
            old_book["title"] = book.title
            old_book["author"] = book.author
            return book
    raise HTTPException(404, "Book not found")

@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            books.remove(book)
            return {"message": f"{book} is deleted"}
    raise HTTPException(404, "Book not found")
