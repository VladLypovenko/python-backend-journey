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

def average_price():
    print("\nTenth Function: Avarage Price\n")
    cursor.execute("""SELECT AVG(price) FROM products""")
    average = cursor.fetchone()
    print(f"Average Price: {average[0]}")

def products_count():
    print("\nEleventh Function: Product Count\n")
    cursor.execute("""SELECT COUNT(*) FROM products""")
    count = cursor.fetchone()
    print(f"Total amount of products: {count[0]}")

def higher_than_average():
    print("\nTwelfth Function: Higher Than Average\n")
    cursor.execute("""SELECT product_name,price FROM products WHERE price > (SELECT AVG(price) FROM products)""")
    products = cursor.fetchall()


    first = True
    for product in products:
        if not first:
            print("-" * 20)
        else:
            print(f"Higher than average: \n")
            first = False
        print(f"Product Name: {product[0]}")
        print(f"Price: {product[1]}")

def products_above_category_average():
    print("Products above category average")
    category = input("Enter Category Name: ")
    cursor.execute("""SELECT product_name,price,category_name FROM products AS p
                      INNER JOIN categories 
                      ON p.category_id = categories.category_id
                      WHERE category_name = ? AND price > (SELECT AVG(price) FROM products AS subp
                                                            WHERE p.category_id = subp.category_id)""",(category,))
    products = cursor.fetchall()

    cursor.execute("""SELECT AVG(price) FROM products 
                      INNER JOIN categories 
                      ON products.category_id = categories.category_id
                      WHERE category_name = ?""",(category,))
    average = cursor.fetchone()
    first = True
    for product in products:
        if not first:
            print("-" * 20)
        else:
            print(f"Higher than average: \n")
            first = False
        print(f"\nAverage Price: {average[0]}\n")
        print(f"Product Name: {product[0]}")
        print(f"Price: {product[1]}")
        print(f"Category Name: {product[2]}")

def second_expensive_product():
    print("\nSecond Expensive Product\n")
    cursor.execute("""SELECT product_name, price
        FROM products
        ORDER BY price DESC
        LIMIT 1 OFFSET 1""")
    product = cursor.fetchone()
    print(f"Product Name: {product[0]}")
    print(f"Price: {product[1]}")

def expensive_product_of_each_category():
    print("\nexpensive product of each category\n")
    cursor.execute("""SELECT product_name, category_name, price
    FROM (
    SELECT 
        p.product_name,
        c.category_name,
        p.price,
        ROW_NUMBER() OVER (
            PARTITION BY p.category_id
            ORDER BY p.price DESC
        ) AS row_num
    FROM products AS p
    INNER JOIN categories AS c
        ON p.category_id = c.category_id
    )
    WHERE row_num <= 3;
    """)
    result = cursor.fetchall()
    print(result)

def  suppliers_with_higher_avarage_than_the_overall_average():
    print("\nSuppliers with higher avarage than the overall average\n")
    cursor.execute("""SELECT company_name,
                      AVG(price) AS avg_price,
                      COUNT(*) AS prod_count
                      FROM products
                      INNER JOIN suppliers ON suppliers.supplier_id = products.supplier_id
                      GROUP BY suppliers.supplier_id, suppliers.company_name
                      HAVING AVG(price) > (SELECT AVG(price) FROM products)
                      ORDER BY avg_price DESC""")
    result = cursor.fetchall()
    print(f"Company: {result[0][0]}")
    print(f"Avarage Price: {result[0][1]}")
    print(f"Prod Count: {result[0][2]}")


def easiest_windows():
    print("\nEasiest Windows\n")
    cursor.execute("""SELECT product_name,
                supplier_id,
                price,
                ROW_NUMBER() OVER(
                PARTITION BY supplier_id
                ORDER BY price DESC)
                FROM products AS p""")
    result = cursor.fetchall()
    for row in result:
        print(f"Product Name: {row[0]}")
        print(f"Supplier ID: {row[1]}")
        print(f"Price: {row[2]}")
        print(f"Row Number: {row[3]}")
        print()

easiest_windows()





