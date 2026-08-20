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

def unique_countries_customers():
    print("\nThird Function: Unique Countries with UI\n")
    cursor.execute("""SELECT DISTINCT country FROM customers""")
    countries = cursor.fetchall()
    first = True
    for country in countries:
        if not first:
            print("-"*20)
        print("Country: " + country[0])

def all_products_under_100():
    print("\nFourth Function: All Products Under 100\n")
    cursor.execute("""SELECT product_name, price FROM products WHERE price < 100""")
    products = cursor.fetchall()
    first = True
    for product in products:
        if not first:
            print("-" * 20)
        else:
            print("All Products: \n")
            first = False
        print(f"Product Name: {product[0]}")
        print(f"Price: {product[1]}")

def all_customers_from_poland():
    print("\nFifth Function: All Customers from Poland\n")
    cursor.execute("""SELECT first_name, last_name, country FROM customers WHERE country = 'Poland' """)
    customers = cursor.fetchall()
    first = True
    for customer in customers:
        if not first:
            print("-" * 20)
        else:
            print("All Customers: \n")
            first = False
        print(f"First Name: {customer[0]}")
        print(f"Last Name: {customer[1]}")
        print(f"Country: {customer[2]}")

def products_for_sale():
    print("\nSixth Function: Products For Sale\n")
    cursor.execute("""SELECT product_name, price , stock FROM products WHERE price < 50 AND stock > 20""")
    products = cursor.fetchall()
    first = True
    for product in products:
        if not first:
            print("-" * 20)
        else:
            print("All Products for Sale: \n")
            first = False
        print(f"Product Name: {product[0]}")
        print(f"Price: {product[1]}")
        print(f"Stock: {product[2]}")

def products_for_certain_category():
    print("\nSeventh Function: Products For Certain Category\n")
    search_categories = ["Toys", "Drugs", "Food"]
    while True:
        category = input("Please enter your category: ")
        search_categories.append(category)
        choice = input("Add one more? (Y/N): ")
        if choice.lower() != "y":
            break

    placeholders = ",".join("?" * len(search_categories))

    cursor.execute(f"""
                   SELECT product_name, price , category_name FROM products
                   INNER JOIN categories
                   ON products.category_id = categories.category_id
                   WHERE category_name IN ({placeholders})
                   """, tuple(search_categories))
    products = cursor.fetchall()
    first = True
    for product in products:
        if not first:
            print("-" * 20)
        else:
            print("All Products for Sale: \n")
            first = False
        print(f"Product Name: {product[0]}")
        print(f"Price: {product[1]}")
        print(f"Stock: {product[2]}")

def customers_for_period():
    print("\nEighth Function: Customers For Period\n")
    cursor.execute("""SELECT first_name, last_name, country, registered_at FROM customers
                    WHERE registered_at BETWEEN ? AND ? 
                    ORDER BY registered_at """,
                   ("2026-01-15 00:30:00","2026-04-15 23:30:00"))
    customers = cursor.fetchall()
    first = True
    for customer in customers:
        if not first:
            print("-" * 20)
        else:
            print("All Customers: \n")
            first = False
        print(f"First Name: {customer[0]}")
        print(f"Last Name: {customer[1]}")
        print(f"Country: {customer[2]}")
        print(f"Registered At: {customer[3]}")

def all_customers_from_mexico_and_poland_after_february():
    print("\nNinth Function: All Customers from Mexico and Poland\n")
    cursor.execute("""SELECT first_name, last_name, country, registered_at FROM customers 
                      WHERE country IN (?,?) AND registered_at > ? """, ("Poland","Mexico","2026-01-30 00:00:00",))
    customers = cursor.fetchall()
    first = True
    for customer in customers:
        if not first:
            print("-" * 20)
        else:
            print("All Customers: \n")
            first = False
        print(f"First Name: {customer[0]}")
        print(f"Last Name: {customer[1]}")
        print(f"Country: {customer[2]}")
        print(f"Registered At: {customer[3]}")

def most_expensive_product_for_category():
    print("\nTenth Function: Most Expensive Product for Category\n")
    cursor.execute("""SELECT product_name, price , category_name FROM products
                      INNER JOIN categories ON products.category_id = categories.category_id
                      WHERE category_name = ? 
                      ORDER BY price DESC 
                      LIMIT 3""", ("Technics",))
    products = cursor.fetchall()
    first = True
    for product in products:
        if not first:
            print("-" * 20)
        else:
            print(f"3 Most Expensive Products for {product[2]}: \n")
            first = False
        print(f"Product Name: {product[0]}")
        print(f"Price: {product[1]}")



