
import sqlite3
import pandas as pd

# STEP 1A: Import SQL Library and Pandas

# STEP 1B: Connect to the database
conn = sqlite3.connect("data.sqlite")

# Reference: Display all employees
employee_data = pd.read_sql(
    "SELECT * FROM employees",
    conn
)

print("---------------------Employee Data---------------------")
print(employee_data)
print("-------------------End Employee Data-------------------")


# STEP 2: Employee number followed by last name
df_first_five = pd.read_sql("""
    SELECT employeeNumber, lastName
    FROM employees;
""", conn)


# STEP 3: Last name followed by employee number
df_five_reverse = pd.read_sql("""
    SELECT lastName, employeeNumber
    FROM employees;
""", conn)


# STEP 4: Rename employeeNumber to ID
df_alias = pd.read_sql("""
    SELECT lastName, employeeNumber AS ID
    FROM employees;
""", conn)


# STEP 5: Categorize employees by role
df_executive = pd.read_sql("""
    SELECT
        CASE
            WHEN jobTitle IN ('President', 'VP Sales', 'VP Marketing')
            THEN 'Executive'
            ELSE 'Not Executive'
        END AS role
    FROM employees;
""", conn)


# STEP 6: Find the length of each last name
df_name_length = pd.read_sql("""
    SELECT LENGTH(lastName) AS name_length
    FROM employees;
""", conn)


# STEP 7: Return the first two letters of each job title
df_short_title = pd.read_sql("""
    SELECT SUBSTR(jobTitle, 1, 2) AS short_title
    FROM employees;
""", conn)


# Reference: Display all order details
order_details = pd.read_sql(
    "SELECT * FROM orderDetails;",
    conn
)

print("------------------Order Details Data------------------")
print(order_details)
print("----------------End Order Details Data----------------")


# STEP 8: Round each order line price, then calculate the sum
sum_total_price = pd.read_sql("""
    SELECT ROUND(priceEach * quantityOrdered) AS total_price
    FROM orderDetails;
""", conn).sum()


# STEP 9: Extract day, month, and year from orderDate
df_day_month_year = pd.read_sql("""
    SELECT
        orderDate,
        SUBSTR(orderDate, 9, 2) AS day,
        SUBSTR(orderDate, 6, 2) AS month,
        SUBSTR(orderDate, 1, 4) AS year
    FROM orders;
""", conn)


# Close the connection as required by the README
conn.close()
