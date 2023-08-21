
import random
import faker
import datetime

# Define age groups and their probabilities
age_groups = ["18-29", "30-39", "40-49", "50-59", "60-69", "70-79", "80-90"]
age_preferences = [0.4, 0.2, 0.15, 0.1, 0.08, 0.06, 0.01]

# Create a Faker generator
fake = faker.Faker()

# Generate a random age based on age preferences
def generate_age():
    age_group = random.choices(age_groups, weights=age_preferences)[0]
    age_range = age_group.split("-")
    return random.randint(int(age_range[0]), int(age_range[1]))

# Calculate balance based on age
def calculate_balance(age):
    # Replace this with your own balance calculation logic
    return random.randint(1000, 10000)

# Create a random date that decreases over the years
def generate_created_at(year):
    current_year = datetime.datetime.now().year
    years_passed = current_year - year
    random_days = random.randint(0, 365 * years_passed)
    return datetime.datetime(year, 1, 1) + datetime.timedelta(days=random_days)

# Create user data
def generate_user_data():
    age = generate_age()
    created_at = generate_created_at(random.randint(2000, 2023))
    balance = calculate_balance(age)
    username = fake.user_name()
    email = fake.email()
    first_name = fake.first_name()
    last_name = fake.last_name()
    updated_at = datetime.datetime.now()

    return age, created_at, balance, username, email, first_name, last_name, updated_at

# Insert user data into the database
def insert_user_data(cursor, age, created_at, balance, username, email, first_name, last_name, updated_at):
    insert_user_query = """
    INSERT INTO users (username, age, email, firstName, lastName, createdAt, updatedAt, startBalance)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """
    user_data = (username, email, first_name, last_name, created_at, updated_at, balance)
    cursor.execute(insert_user_query, user_data)

# Example of how to use the functions
def main():
    # Assume you have a database connection named "cursor"
    for _ in range(100):  # Generate 100 users
        age, created_at, balance, username, email, first_name, last_name, updated_at = generate_user_data()
        insert_user_data(cursor, age, created_at, balance, username, email, first_name, last_name, updated_at)
        # Get the user's ID from the database and call related functions
        user_id = cursor.lastrowid
        createIncome(user_id, age, created_at)
        createExpenses(user_id, age, created_at)
        createSavingsGoal(user_id, age, created_at)

if __name__ == "__main__":
    main()


# create ages 
# loop in ages in each do:
# create time of joining 
# start balnce: in each groupe of ages have a likely balnce 
# 
# for each user create in each month from the starting date to today:
# Income:salary rare freelace and part time
# 
# Expenses:Rent,Groceries,Utilities
# 
# Savings:goals? the problem is the random how to do ?
# 
# end blance get calculator + income -  Expenses - Savings

