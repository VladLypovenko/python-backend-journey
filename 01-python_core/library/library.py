
from book import *
from member import *
from exceptions import *

class Library:
    def __init__(self, books = None, members = None):

        if not books:
            self.books = {}
        else:
            self.books = books

        if not members:
            self.members = {}
        else:
            self.members = members

    def __str__(self):

        members = ", ".join(self.members)

        books = ", ".join(self.books)

        return f'Books: {self.books} \nMembers: {members}'

    def add_book(self, book: Book):
        if book.isbn not in self.books.keys():
            self.books[book.isbn] = book
        else:
            raise DuplicateError("Item already registered")
        return None

    def remove_book(self, isbn):
        book = self.find_book(isbn)

        if not book:
            raise ItemNotFoundError("Item not found")

        if book.is_available:
            return self.books.pop(book.isbn, None)

        else:
            raise ValueError("Item is not available")

    def register_member(self, member: Member):
        if member in self.members.keys():
            raise ItemAlreadyExistsError("Member already registered")
        self.members[member.member_id] = member
        return None

    def find_book(self, isbn):
        return self.books.get(isbn)

    def search_books(self, title = None, author = None):
        results = []
        title = title.lower() if title else None
        author = author.lower() if author else None

        for book in self.books.values():
            found = True
            if title:
                if title not in book.title.lower():
                    found = False

            if author:
                if author not in book.author.lower():
                    found = False
            if found:
                results.append(book)

        return results

    def found_member(self, member_id):
        return self.members.get(member_id)

    def borrow_book(self, member_id, isbn):
        member = self.found_member(member_id)

        if not member:
            raise ItemNotFoundError("Item not found")
        if len(member.borrowed_books) > 2:
            raise ValueError("Cannot borrow more than 3 books")

        book = self.find_book(isbn)

        if not book:
            raise ItemNotFoundError("Item not found")
        if not book.is_available:
            raise ValueError("Book is not available")

        member.borrowed_books[book.isbn] = book
        book.is_available = False
        return None

    def return_book(self, member_id, isbn):
        member = self.found_member(member_id)

        if not member:
            raise ItemNotFoundError("Item not found")

        book = member.borrowed_books.get(isbn)

        if not book:
            raise ItemNotFoundError("Item not found")

        member.borrowed_books.pop(isbn)

        book.is_available = True

        return None






