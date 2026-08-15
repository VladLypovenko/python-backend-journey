
class Category:
    next_id = 1

    def __init__(self, name):
        self.c_id = Category.next_id
        Category.next_id += 1

        self.name = name

    def __str__(self):
        return f"""
    ID:{self.c_id}
    Name:{self.name}
    """