import mysql.connector
from app.fake_users.create.create_tables import create_tables
from app.fake_users.create.fake_user_creater import fake_user_creater

def execute_query(query, params=None):
    db_config = {
        "user": "root",
        "password": "123456",
        "host": "localhost",
        "database": "personal_finance_management_system"
    }

    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()

    if params:
        cursor.execute(query, params)
    else:
        cursor.execute(query)

    result = None
    if query.lower().startswith('select'):
        result = cursor.fetchall()

    connection.commit()
    cursor.close()
    connection.close()

    return result



def insert_fake_users(num_users):
    db_config = {
        "user": "root",
        "password": "123456",
        "host": "localhost",
    }

    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()

    # Create database if not exists
    create_tables(cursor)

    # Call the function to create the specified number of random users
    fake_user_creater(cursor, connection, num_users)

    cursor.close()
    connection.close()



def create_tables():
    db_config = {
        "user": "root",
        "password": "123456",
        "host": "localhost",
    }

    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()

    create_tables(cursor)

    cursor.close()
    connection.close()

