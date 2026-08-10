from app.exceptions.exceptions import DuplicateProductError, ProductNotFoundError, DuplicateCategoryError, \
    CategoryNotFoundError, SupplierNotFoundError, DuplicateSupplierError
from app.models.category import Category
from app.models.inventory import Inventory
from app.models.product import Product
from app.models.supplier import Supplier


class InventoryService:
    def __init__(self, inventory: Inventory):
        self.inventory = inventory

    def add_product(self, product: Product):
        if self.find_product(product.p_id) is not None:
            raise DuplicateProductError(f"Product with {product.p_id} already exists")

        self.inventory.add_product(product)

    def remove_product(self, p_id: int):
        if self.find_product(p_id) is None:
            raise ProductNotFoundError(f"Product with {p_id} is not found")

        self.inventory.remove_product(p_id)

    def update_product(self, product: Product):
        r_product = self.find_product(product.p_id)
        if r_product is None:
            raise ProductNotFoundError(f"Product with {product.p_id} not found")

        self.inventory.Products[r_product.p_id] = product

    def find_product(self, p_id: int) :
        return self.inventory.get_product(p_id)

    def search_product(self, name: str):
        return [product for product in self.inventory.Products.values() if name.lower() in product.name.lower()]




    def add_category(self, category: Category):
        if self.inventory.get_category(category.c_id) is not None:
            raise DuplicateCategoryError(f"Category with {category.c_id} already exists")

        self.inventory.add_category(category)

    def remove_category(self, c_id: int):
        if self.inventory.get_category(c_id) is None:
            raise CategoryNotFoundError(f"Category with {c_id} not found")

        self.inventory.remove_category(c_id)





    def add_supplier(self, supplier: Supplier):
        if self.inventory.get_supplier(supplier.s_id) is not None:
            raise DuplicateSupplierError(f"Supplier with {supplier.s_id} already exists")

        self.inventory.add_supplier(supplier)


    def remove_supplier(self, s_id: int):
        if self.inventory.get_supplier(s_id) is None:
            raise SupplierNotFoundError(f"Supplier with {s_id} not found")

        self.inventory.remove_supplier(s_id)



    def restock_product(self,p_id,amount: int):
        r_product = self.find_product(p_id)
        if r_product is None:
            raise ProductNotFoundError(f"Product with {p_id} is not found")

        r_product.increase_stock(amount)

    def sell_product(self,p_id,amount: int):
        r_product = self.find_product(p_id)
        if r_product is None:
            raise ProductNotFoundError(f"Product with {p_id} is not found")

        r_product.decrease_stock(amount)


    def total_products(self):
        return len(self.inventory.Products)


    def total_stock(self):
        return sum(product.quantity for product in self.inventory.Products.values())

    def low_stock_products(self):
        low_stock = 5

        low_stock_products = [product for product in self.inventory.Products.values() if product.quantity <= low_stock]

        return low_stock_products
