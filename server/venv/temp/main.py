import mysql.connector
from create.create_tables import create_tables
from create.fake_user_creater import fake_user_creater

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
create_tables(cursor)

# Call the function to create 100 random users
fake_user_creater(cursor, connection, 200)


# Commit changes and close connection
# connection.commit()
cursor.close()
connection.close()
