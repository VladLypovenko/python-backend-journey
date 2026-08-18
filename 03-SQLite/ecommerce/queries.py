from database import connection

cursor = connection.cursor()
def select_all_customers():
    print("First Function: Select all Customers with UI")

    #Select all Customers with UI

    cursor.execute("""SELECT * FROM customers""")
    customers = cursor.fetchall()
    first = True
    for customer in customers:
        if not first:
            print("-"*20)
        else:
            print("All Customers: \n")
            first = False
        print(f"First Name: {customer[1]}")
        print(f"Last Name: {customer[2]}")
        print(f"Email: {customer[3]}")
        print(f"Country: {customer[4]}")
        print(f"Registered: {customer[5]}")

#Select Products Info with Inner Join from Other Tables

def select_all_products():
    print("\nSecond Function: Select all Products with UI\n")

    cursor.execute("""SELECT product_name,category_name,company_name,price,stock
                    FROM products
                    INNER JOIN categories
                    ON products.category_id = categories.category_id
                    INNER JOIN suppliers
                    ON products.supplier_id = suppliers.supplier_id
                    """)
    products = cursor.fetchall()
    first = True
    for product in products:
        if not first:
            print("-"*20)
        else:
            print("All Products: \n")
            first = False
        print(f"Product Name: {product[0]}")
        print(f"Category: {product[1]}")
        print(f"Supplier: {product[2]}")
        print(f"Price: {product[3]}")
        print(f"Stock: {product[4]}")


