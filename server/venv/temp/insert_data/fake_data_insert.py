

# Insert user data into the database
def insert_user_data(cursor, connection, user_data_list):
    insert_user_query = """
    INSERT INTO users (username, age, email, firstName, lastName, createdAt, updatedAt, balance, startBalance)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    # user_data_list = (username, age, email, first_name, last_name, created_at, updated_at, balance)
    cursor.executemany(insert_user_query, user_data_list)
    connection.commit()

# Insert user_income data into the database
def insert_income_data(cursor, connection, income_data_list):
    insert_income_query = """
    INSERT INTO income (user_id, amount, frequency, name, createdAt)
    VALUES (%s, %s, %s, %s, %s)
    """
    # income_data_list = (user_id, amount, months, income_type, createdAt)
    cursor.executemany(insert_income_query, income_data_list)
    connection.commit()


