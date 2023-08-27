

def create_tables(cursor):
    # Create database if not exists
    database_name = "personal_finance_management_system"
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database_name}")
    cursor.execute(f"USE {database_name}")

    # Create users table if not exist
    create_users_table_query = """
    CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        username VARCHAR(50) NOT NULL,
        age INT NOT NULL,
        email VARCHAR(100) NOT NULL,
        firstName VARCHAR(50),
        lastName VARCHAR(50),
        createdAt DATETIME,
        updatedAt DATETIME,
        startBalance DECIMAL(10, 2)
    )
    """
    cursor.execute(create_users_table_query)

    # Create income table if not exist
    create_income_sources_table_query = """
    CREATE TABLE IF NOT EXISTS income (
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
