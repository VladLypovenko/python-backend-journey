class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = {}

    def __str__(self):
        borrowed_books = ", ".join(self.borrowed_books)
        return f'Member: {self.name} \nID: {self.member_id} \nBorrowed: {borrowed_books}'

