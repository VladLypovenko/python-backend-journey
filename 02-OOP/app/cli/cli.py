from app.models.category import Category
from app.models.product import Product
from app.models.supplier import Supplier
from app.utils.validators import *

from app.models.inventory import Inventory
from app.services.inventory_service import InventoryService

inventory = Inventory()
inventory_service = InventoryService(inventory)

def show_menu():
    menu = {"1":"Add Product",
            "2":"Update Product",
            "3":"Delete Product",
            "4":"Add Category",
            "5":"Add Supplier",
            "6":"Restock Product",
            "7":"Sell Product",
            "8":"Search Product",
            "9":"Show All Products",
            "10":"Show Categories",
            "11":"Show Suppliers",
            "12":"Inventory Statistics",
            "0":"Exit"}

    print("========= Inventory Management =========")

    for key, value in menu.items():
        print(f"{key}: {value}")


def add_product():
    while True:
        print("Please enter the name of the product you want to add: ")
        name = input()
        try:
            name = validate_name(name)
        except ValueError as e:
            print(e)
            continue
        break

    while True:
        print("Please enter the price of the product you want to add: ")
        price = input()
        try:
            price = float(price)
            price = validate_positive_float(price)
        except ValueError as e:
            print(e)
            continue
        break

    print("Please enter the description of the product you want to add: ")
    description = input()

    while True:
        print("Please enter the quantity of the product you want to add: ")
        quantity = input()
        try:
            quantity = int(quantity)
            quantity = validate_positive_int(quantity)
        except ValueError as e:
            print(e)
            continue
        break

    categories = inventory_service.get_all_categories()

    while True:
        curr_category = None
        print("Choose a category or add a new one: ")

        for category in categories.values():
            print(f"{category.c_id}: {category.name}")

        print("0: New Category")
        choice = input()
        try:
            choice = int(choice)
        except ValueError as e:
            print(e)
            continue

        if choice == 0:
            print("Please enter the Name of Category: ")
            c_name = input()

            new_category = Category(c_name)

            inventory_service.add_category(new_category)
            curr_category = new_category
            break

        elif choice in categories:
            curr_category = categories.get(choice)
            break

        else:
            print("Invalid choice.")
            continue

    suppliers = inventory_service.get_all_suppliers()

    while True:
        curr_supplier = None
        print("Choose a category or add a new one: ")

        for supplier in suppliers.values():
            print(f"{supplier.s_id}: {supplier.company_name}")

        print("0: New Supplier")
        choice = input()
        try:
            choice = int(choice)
        except ValueError as e:
            print(e)
            continue

        if choice == 0:
            print("Please enter the Company_name of Supplier: ")
            s_name = input()

            print("Please enter Email Address of Supplier: ")
            email = input()

            print("Please enter Phone Number for Supplier: ")
            phone = input()

            new_supplier = Supplier(s_name,email,phone)

            inventory_service.add_supplier(new_supplier)
            curr_supplier = new_supplier
            break

        elif choice in suppliers:
            curr_supplier = suppliers.get(choice)
            break
        else:
            print("Invalid choice.")
            continue

    new_product = Product(name, price, description, quantity, curr_category, curr_supplier)
    inventory_service.add_product(new_product)



def update_product():
    products = inventory_service.get_all_products()

    product = None

    print("Which product do you want to update?")

    for product in products.values():
        print(f"{product.p_id}: {product.name}")

    while True:
        try:
            choice = int(input("Product ID: "))
        except ValueError:
            print("Please enter a valid ID.")
            continue

        product = products.get(choice)

        if product is None:
            print("Invalid product ID.")
            continue

        break

    while True:
        print("\nWhat do you want to update?")

        actions = {
            "1": "Change Name",
            "2": "Change Price",
            "3": "Change Description",
            "4": "Change Category",
            "5": "Change Supplier",
            "0": "Finish"
        }

        for key, value in actions.items():
            print(f"{key}: {value}")

        action = input("Choose an option: ")

        if action == "0":
            break

        elif action == "1":
            while True:
                try:
                    new_name = validate_name(input("New name: "))
                    product.name = new_name
                    break
                except ValueError as e:
                    print(e)

        elif action == "2":
            while True:
                try:
                    new_price = float(input("New price: "))
                    product.price = validate_positive_float(new_price)
                    break
                except ValueError as e:
                    print(e)

        elif action == "3":
            product.description = input("New description: ")

        elif action == "4":
            categories = inventory_service.get_all_categories()

            for category in categories.values():
                print(f"{category.c_id}: {category.name}")

            print("0: New Category")

            while True:
                try:
                    choice = int(input("Category ID: "))
                except ValueError:
                    print("Please enter a valid ID.")
                    continue

                if choice == 0:
                    name = input("Category name: ")
                    category = Category(name)
                    inventory_service.add_category(category)
                    product.category = category
                    break

                category = categories.get(choice)

                if category is None:
                    print("Invalid category ID.")
                    continue

                product.category = category
                break

        elif action == "5":
            suppliers = inventory_service.get_all_suppliers()

            for supplier in suppliers.values():
                print(f"{supplier.s_id}: {supplier.company_name}")

            print("0: New Supplier")

            while True:
                try:
                    choice = int(input("Supplier ID: "))
                except ValueError:
                    print("Please enter a valid ID.")
                    continue

                if choice == 0:
                    company_name = input("Company name: ")
                    email = input("Email: ")
                    phone = input("Phone: ")

                    supplier = Supplier(
                        company_name,
                        email,
                        phone
                    )

                    inventory_service.add_supplier(supplier)
                    product.supplier = supplier
                    break

                supplier = suppliers.get(choice)

                if supplier is None:
                    print("Invalid supplier ID.")
                    continue

                product.supplier = supplier
                break

        else:
            print("Invalid option.")

    inventory_service.update_product(product)
    print("Product updated successfully.")


def delete_product():
    ...


def add_category():
    ...


def add_supplier():
    ...


def restock_product():
    ...


def sell_product():
    ...


def search_products():
    ...


def show_all_products():
    ...


def show_categories():
    ...


def show_suppliers():
    ...


def show_statistics():
    ...


def run():
    ...
