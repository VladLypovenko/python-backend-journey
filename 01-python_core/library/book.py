class Book:
    def __init__(self,isbn,title,author):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = True

    def __str__(self):
        return(f"""Title: {self.title}
Author: {self.author}
ISBN: {self.isbn}
Availability: {self.is_available}
                """)