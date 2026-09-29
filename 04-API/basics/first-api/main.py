from fastapi import FastAPI
from fastapi.exceptions import HTTPException

app = FastAPI()

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

@app.post("/books/")
def create_book(title: str, author: str):
    books.append({"id": len(books) + 1, "title": title, "author": author})
def add_book(book: dict):
    return book
