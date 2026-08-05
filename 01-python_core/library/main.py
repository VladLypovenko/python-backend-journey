from book import Book
from member import Member
from library import Library
from exceptions import *

working = True

menu = {
    "1": "Add a Book",
    "2": "Add a Member",
    "3": "Borrow a Book",
    "4": "Return the Book to Library",
    "5": "Delete a Book",
    "6": "Search for a Book",
    "7": "Show all Books",
    "8": "Borrowed Books",
    "0": "Exit"
}

library = Library()

def add_book():
    while True:
        print("Please enter the ISBN of the book: ")
        isbn = input()
        try:
            isbn = int(isbn)
            break
        except ValueError:
            continue

    while True:
        print("Please enter the Title of the book: ")
        title = input()

        if len(title) == 0:
            continue
        else:
            break

    while True:
        print("Please enter the Author of the book: ")
        author = input()

        if len(author) == 0:
            continue
        else:
            break

    title = input().strip()
    author = input().strip()

    new_book = Book(isbn, title, author)

    try:
        library.add_book(new_book)

    except DuplicateError as e:
        print(e)

def add_member():
    while True:
        print("Please enter a name of Member: ")
        name = input()
        if len(name) == 0:
            continue
        else:
            break

    while True:
        print("Please enter the member_id of the member: ")
        member_id = input()
        try:
            member_id = int(member_id)
            break
        except ValueError:
            continue

    new_member = Member(name,member_id)

    try:
        library.register_member(new_member)
    except ItemAlreadyExistsError as e:
        print(e)

def borrow_book():
    while True:
        print("Please enter your Member Id: ")
        member_id = input()
        if len(member_id) != 0:
            try:
                member_id = int(member_id)
                break
            except ValueError:
                continue
        else:
            continue

    while True:
        print("Please enter the ISBN of the book: ")
        isbn = input()
        try:
            isbn = int(isbn)
            break
        except ValueError:
            continue

    try:
        library.borrow_book(member_id, isbn)
    except (ItemNotFoundError, ValueError) as e:
        print(e)

def return_book():
    while True:
        print("Please enter your Member Id: ")
        member_id = input()
        if len(member_id) != 0:
            try:
                member_id = int(member_id)
                break
            except ValueError:
                continue
        else:
            continue

    while True:
        print("Please enter the ISBN of the book: ")
        isbn = input()
        try:
            isbn = int(isbn)
            break
        except ValueError:
            continue

    try:
        library.return_book(member_id,isbn)
    except (ItemNotFoundError, ValueError) as e:
        print(e)

def delete_book():
    while True:
        print("Please enter the ISBN of the book: ")
        isbn = input()
        try:
            isbn = int(isbn)
            break
        except ValueError:
            continue

    try:
        library.remove_book(isbn)
    except (ItemNotFoundError, ValueError) as e:
        print(e)

def search_book():
    print("Please enter the Title of the book: ")
    title = input()

    print("Please enter the Author of the book: ")
    author = input()

    result = library.search_books(title, author)

    if not result:
        print("Book not found")
        return False

    for book in result:
        print(book)
    return True

def show_all_books():
    for book in library.books.values():
        print(book)

def show_available_books():
    result = [book for book in library.books.values() if book.is_available]

    if not result:
        print("No books available")
        return

    for book in result:
        print(book)


while working:
    for keys, values in menu.items():
        print(f"{keys}. {values}")

    print("Please enter an action with number: ")

    action = input()

    if action == "1":
        add_book()

    elif action == "2":
        add_member()

    elif action == "3":
        borrow_book()

    elif action == "4":
        return_book()

    elif action == "5":
        delete_book()

    elif action == "6":
        search_book()

    elif action == "7":
        show_all_books()

    elif action == "8":
        show_available_books()

    elif action == "0":
        print("Goodbye!")
        working = False
