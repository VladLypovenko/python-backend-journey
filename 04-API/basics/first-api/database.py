import sqlite3

from models import BookCreate

from datetime import datetime

conn = sqlite3.connect("database.db", check_same_thread=False)
cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS books(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               title TEXT NOT NULL,
               author TEXT NOT NULL,
               created_at TEXT NOT NULL,
               updated_at TEXT NOT NULL
               )
               """)

conn.commit()

def get_a_book_by_id(book_id):
    cur.execute("""SELECT * FROM books WHERE id = ?""", (book_id,))
    result = cur.fetchone()
    book = {
    "id": result[0],
    "title": result[1],
    "author": result[2],
    "created_at": result[3],
    "updated_at": result[4]
    }
    return book

def get_a_book_by_title(title):
    cur.execute("""SELECT * FROM books WHERE title = ?""", (title,))
    result = cur.fetchone()
    book = {
        "id": result[0],
        "title": result[1],
        "author": result[2],
        "created_at": result[3],
        "updated_at": result[4]
    }
    return book

def get_all_books():
    cur.execute("""SELECT * FROM books""")
    result = cur.fetchall()
    return result

def create_a_book(title, author):
    new_book = BookCreate(title=title, author=author)

    cur.execute("""INSERT INTO books (title, author, created_at , updated_at ) VALUES (?, ?, ?, ?)""",
                (new_book.title, new_book.author, datetime.now(), datetime.now()))

    conn.commit()

    book_id = cur.lastrowid

    return get_a_book_by_id(book_id)

def update_a_book(book_id, new_title, new_author):
    cur.execute("""SELECT * FROM books WHERE id = ?""", (book_id,))

    result = cur.fetchone()

    if result:

        cur.execute("""UPDATE books SET title = ?, author = ?, updated_at = ? WHERE id = ?""",
                    (new_title,new_author,datetime.now(),book_id,))
        conn.commit()
        new_book = {
        "id": result[0],
        "title": result[1],
        "author": result[2],
        "created_at": result[3],
        "updated_at": result[4]
        }
        return new_book

    return None

def delete_a_book(book_id):
    cur.execute("""SELECT * FROM books WHERE id = ?""", (book_id,))

    result = cur.fetchone()

    if result:
        cur.execute("""DELETE FROM books WHERE id = ?""", (book_id,))
        conn.commit()
        return {"message": f"{result[0]} is deleted successfully"}

    return None