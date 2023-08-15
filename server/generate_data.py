import mysql.connector
from random import randint, uniform
from datetime import datetime, timedelta
from faker import Faker

# Configure database connection
db_config = {
    "user": "root",
    "password": "123456",
    "host": "localhost",
}

# Create a connection
connection = mysql.connector.connect(**db_config)
cursor = connection.cursor()

# Create database if not exists
database_name = "personal_finance_management_system"
cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database_name}")
cursor.execute(f"USE {database_name}")

# Create users table if not exist
create_users_table_query = """
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL,
    firstName VARCHAR(50),
    lastName VARCHAR(50),
    createdAt DATETIME,
    updatedAt DATETIME,
    startBalance DECIMAL(10, 2)
)
"""
cursor.execute(create_users_table_query)

# Create income_sources table if not exist
create_income_sources_table_query = """
CREATE TABLE IF NOT EXISTS income_sources (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    name VARCHAR(100),
    amount DECIMAL(10, 2),
    frequency VARCHAR(50),
    createdAt DATETIME,
    FOREIGN KEY (user_id) REFERENCES users(id)
)
"""
cursor.execute(create_income_sources_table_query)

# Create expenses table if not exist
create_expenses_table_query = """
CREATE TABLE IF NOT EXISTS expenses (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    name VARCHAR(100),
    amount DECIMAL(10, 2),
    category VARCHAR(50),
    date DATE,
    createdAt DATETIME,
    FOREIGN KEY (user_id) REFERENCES users(id)
)
"""
cursor.execute(create_expenses_table_query)

# Create savings_goals table if not exist
create_savings_goals_table_query = """
CREATE TABLE IF NOT EXISTS savings_goals (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    name VARCHAR(100),
    targetAmount DECIMAL(10, 2),
    currentAmount DECIMAL(10, 2),
    targetDate DATE,
    createdAt DATETIME,
    FOREIGN KEY (user_id) REFERENCES users(id)
)
"""
cursor.execute(create_savings_goals_table_query)

# Generate and insert data

def create_random_users(num_users):

    # Initialize Faker instance
    fake = Faker()

    for _ in range(num_users):
        username = fake.user_name()
        email = fake.email()
        first_name = fake.first_name()
        last_name = fake.last_name()
        created_at = datetime.now() - timedelta(days=_)
        updated_at = datetime.now() - timedelta(days=_)
        start_balance = round(uniform(0, 10000), 2)

        # Insert user
        insert_user_query = """
        INSERT INTO users (username, email, firstName, lastName, createdAt, updatedAt, startBalance)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        user_data = (username, email, first_name, last_name, created_at, updated_at, start_balance)
        cursor.execute(insert_user_query, user_data)

# Call the function to create 100 random users
create_random_users(100)



# Commit changes and close connection
connection.commit()
cursor.close()
connection.close()
