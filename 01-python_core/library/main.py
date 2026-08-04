from book import Book
from member import Member
from library import Library
from exceptions import *

# -------------------------
# Create books
# -------------------------

book1 = Book("Harry Potter", "J. K. Rowling", "1")
book2 = Book("The Housemaid", "Freida McFadden", "2")
book3 = Book("Clean Code", "Robert C. Martin", "3")
book4 = Book("Python Crash Course", "Eric Matthes", "4")

# Duplicate ISBN
duplicate_book = Book("Another Book", "Someone", "1")

# -------------------------
# Create members
# -------------------------

member1 = Member("Vlad", "1211")
member2 = Member("Ivan", "1212")

duplicate_member = Member("Alex", "1211")

# -------------------------
# Create library
# -------------------------

library = Library()

print("\n=== ADD BOOKS ===")
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
library.add_book(book4)

print("\nDuplicate ISBN:")
try:
    library.add_book(duplicate_book)
except DuplicateError as e:
    print(e)

print("\n=== REGISTER MEMBERS ===")
library.register_member(member1)
library.register_member(member2)

print("\nDuplicate Member ID:")
library.register_member(duplicate_member)

print("\n=== FIND BOOK ===")
print(library.find_book("1"))

print("\nFind non-existing book:")
print(library.find_book("999"))

print("\n=== SEARCH BOOKS ===")
print(library.search_books(title="Harry"))
print(library.search_books(author="Martin"))

print("\n=== BORROW BOOK ===")
print(library.borrow_book(member1.member_id, book1.isbn))

print("\nBorrow the same book again:")
try:
    print(library.borrow_book(member1.member_id, book1.isbn))
except ValueError as e:
    print(e)

print("\n=== BORROW LIMIT ===")
library.borrow_book(member1.member_id, book2.isbn)
library.borrow_book(member1.member_id, book3.isbn)

print("Try to borrow the fourth book:")
try:
    print(library.borrow_book(member1.member_id, book4.isbn))
except ValueError as e:
    print(e)

print("\nCurrent borrowed books:")
for book in member1.borrowed_books:
    print(book)

print("\n=== RETURN BOOK ===")
print(library.return_book(member1.member_id, book1.isbn))

print("\nBorrowed books after return:")
for book in member1.borrowed_books:
    print(book)

print("\nReturn someone else's book:")
try:
    print(library.return_book(member1.member_id, book1.isbn))
except ItemNotFoundError as e:
    print(e)

print("\n=== REMOVE BOOK ===")

print("Try to remove borrowed book:")
try:
    library.remove_book(book1.isbn)
except ItemNotFoundError or ValueError or TypeError as e:
    print(e)

print("Return it first:")
try:
    print(library.return_book(member1.member_id, book2.isbn))
except ItemNotFoundError as e:
    print(e)

print("Remove again:")
print(library.remove_book(book2.isbn))

print("\n=== SEARCH MISSING BOOK ===")
print(library.search_books(title="Lord of the Rings"))