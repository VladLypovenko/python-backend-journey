# E-commerce Analytics

A small SQLite database project created to practice SQL and relational database concepts.

## Goal

The goal of this project is to gain practical experience with SQL by working with an e-commerce database and writing queries for different types of data analysis.

## Database Structure

The database contains the following entities:

- Customers — store customers and their registration information
- Categories — product categories
- Suppliers — product suppliers
- Products — products available in the store
- Orders — customer orders
- Order Items — products, quantities and prices belonging to each order

### Relationships

- Customer → Orders
- Category → Products
- Supplier → Products
- Order → Order Items
- Product → Order Items

## Technologies

- Python
- SQLite
- SQL

Python is used only to connect to the SQLite database and execute SQL queries.

## SQL Topics

The project is used to practice:

- SELECT
- WHERE
- ORDER BY
- LIMIT
- DISTINCT
- INSERT
- UPDATE
- DELETE
- AND / OR / NOT
- IN
- BETWEEN
- LIKE
- Aggregate functions
- GROUP BY
- HAVING
- JOINs
- Subqueries
- CASE
- CTEs
- Window functions

## Project Status

Currently working on basic SELECT queries and JOINs.

More advanced SQL queries will be added as the project progresses.