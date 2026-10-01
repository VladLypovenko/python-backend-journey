import sqlite3

from models import Book

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
    return result

def get_a_book_by_title(title):
    cur.execute("""SELECT * FROM books WHERE title = ?""", (title,))
    result = cur.fetchone()
    return result

def get_all_books():
    cur.execute("""SELECT * FROM books""")
    result = cur.fetchall()
    return result

def create_a_book(title, author):
    new_book = Book(title=title, author=author,
                    created_at=datetime.now(),
                    updated_at=datetime.now())

    cur.execute("""INSERT INTO books (title, author, created_at , updated_at ) VALUES (?, ?, ?, ?)""",
                (new_book.title, new_book.author, new_book.created_at, new_book.updated_at))

    conn.commit()

def update_a_book(book_id, new_title, new_author):
    cur.execute("""SELECT * FROM books WHERE id = ?""", (book_id,))

    result = cur.fetchone()

    if result:

        cur.execute("""UPDATE books SET title = ?, author = ?, updated_at = ? WHERE id = ?""",
                    (new_title,new_author,datetime.now(),book_id,))
        conn.commit()
        return {"message: " f"{result[0]} is updated successfully"}

    return None

def delete_a_book(book_id):
    cur.execute("""SELECT * FROM books WHERE id = ?""", (book_id,))

    result = cur.fetchone()

    if result:
        cur.execute("""DELETE FROM books WHERE id = ?""", (book_id,))
        conn.commit()
        return {"message": f"{result[0]} is deleted successfully"}

    return None