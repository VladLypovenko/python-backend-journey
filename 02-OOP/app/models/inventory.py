from app.models.product import Product
from app.models.category import Category
from app.models.supplier import Supplier


class Inventory:
    def __init__(self):
        self.Products = {}
        self.Categories = {}
        self.Suppliers = {}

    def add_product(self, product: Product):
        self.Products[product.p_id] = product

    def remove_product(self, p_id: int):
        self.Products.pop(p_id)

    def get_product(self, p_id: int):
        return self.Products.get(p_id)


    def add_category(self, category: Category):
        self.Categories[category.c_id] = category

    def remove_category(self, c_id: int):
        self.Categories.pop(c_id)

    def get_category(self, c_id: int):
        return self.Categories.get(c_id)


    def add_supplier(self, supplier: Supplier):
        self.Suppliers[supplier.s_id] = supplier

    def remove_supplier(self, s_id: int):
        self.Suppliers.pop(s_id)

    def get_supplier(self, s_id: int):
        return self.Suppliers.get(s_id)
