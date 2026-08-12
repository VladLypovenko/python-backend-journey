from app.exceptions.exceptions import InsufficientStockError

class Product:
    next_id = 1
    def __init__(self, name, price, description = "", quantity = 0, category = None, supplier = None):
        self.p_id = Product.next_id
        Product.next_id += 1

        self.name = name
        self.price = price
        self.description = description
        self.quantity = quantity
        self.category = category
        self.supplier = supplier

    def update_price(self,new_price):
        if new_price < 0:
            raise ValueError("New price must be positive")
        else:
            self.price = new_price

    def increase_stock(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be greater than zero")

        self.quantity += amount

    def decrease_stock(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be greater than zero")

        if amount > self.quantity:
            raise InsufficientStockError(
                f"Cannot sell {amount} items. Only {self.quantity} available."
            )

        self.quantity -= amount

    def available(self):
        return self.quantity > 0

    def __str__(self):
        return f"""Name: {self.name}
        Price: {self.price}
        Description: {self.description}
        Quantity: {self.quantity}
        Category: {self.category}
        Supplier: {self.supplier}
"""
