
import random
import faker
import datetime

# Define age groups and their probabilities
age_groups = ["18-29", "30-39", "40-49", "50-59", "60-69", "70-79", "80-90"]
age_preferences = [0.4, 0.2, 0.15, 0.1, 0.08, 0.06, 0.01]

# Create a Faker generator
fake = faker.Faker()

# Generate a random age based on age preferences
def generate_age_group():
    age_group = random.choices(age_groups, weights=age_preferences)[0]
    return age_group

def calculate_months_since_creation(created_at):
    current_date = datetime.now()
    creation_date = datetime.strptime(created_at, "%Y-%m-%d")
    months_since_creation = (current_date.year - creation_date.year) * 12 + current_date.month - creation_date.month
    return months_since_creation

def split_age(age_group):
    age_range = age_group.split("-")
    return random.randint(int(age_range[0]), int(age_range[1]))

def get_income(months,age_income_list):
    current_month = datetime.now().month
    current_year = datetime.now().year

    income_index = current_year - 2020
    # Calculate the number of years beyond the initial year
    years_beyond = (current_month - months) // 12

    # Adjust the income index based on the years beyond
    income_index -= years_beyond

    # Ensure the income index doesn't go below 0
    income_index = max(income_index, 0)

    return age_income_list[income_index]

# Calculate balance based on age and created year
def calculate_balance(age_group, created_at):
    reference_year = 2020  # The starting year in the balance_per_age dictionary
    years_passed = created_at.year - reference_year
    if years_passed < 0:
        years_passed = 0
    
    balance_range = balance_per_age[age_group][years_passed]
    return round(random.uniform(balance_range[0], balance_range[1]), 2)

# Create a random date that decreases over the years
def generate_created_at(year):
    current_year = datetime.datetime.now().year
    years_passed = current_year - year
    random_days = random.randint(0, 365 * years_passed)
    return datetime.datetime(year, 1, 1) + datetime.timedelta(days=random_days)

# Create user data
def generate_user_data():
    age_group = generate_age_group()
    created_at = generate_created_at(random.randint(2000, 2023))#to change so it will look real
    age = split_age(age_group)
    balance = calculate_balance(age_group,created_at)
    username = fake.user_name()
    email = fake.email()
    first_name = fake.first_name()
    last_name = fake.last_name()
    updated_at = datetime.datetime.now()

    return age, created_at, balance, username, email, first_name, last_name, updated_at, age_group

def createIncome(user_id, age_group, created_at, income_data_list):

    # Calculate months since user creation
    months_since_creation = calculate_months_since_creation(created_at)
    monthly = "Monthly"

    # Types of income with corresponding weights
    income_types = ["salary", "freelance", "part_time"]
    income_type_weights = [0.6, 0.25, 0.15]

    # Types of income
    income_type = random.choices(income_types, income_type_weights)[0]

    # total_amount
    total_amount = 0
    # getting the list by years
    age_income_list = income_per_age[age_group]
    for months in range(months_since_creation):
        
        income = get_income(months,age_income_list)
        total_amount += income
        income_data_list.append((user_id, income, monthly, income_type, created_at))

    return total_amount


# Insert user data into the database
def insert_user_data(cursor, user_data_list):
    insert_user_query = """
    INSERT INTO users (username, age, email, firstName, lastName, createdAt, updatedAt, startBalance)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """
    # user_data_list = (username, age, email, first_name, last_name, created_at, updated_at, balance)
    cursor.execute(insert_user_query, user_data_list)

# Insert user_income data into the database
def insert_income_data(cursor, income_data_list):
    insert_income_query = """
    INSERT INTO income (user_id, amount, months, type, createdAt)
    VALUES (%s, %s, %s, %s, %s)
    """
    # income_data_list = (user_id, amount, months, income_type, createdAt)
    cursor.execute(insert_income_query, income_data_list)





# Example of how to use the functions
def main():
    num_users = 100
    user_data_list = []
    income_data_list = []
    user_id = cursor.lastrowid + 1 #return 0 if there is none so we will start on 1 or one after last id

    for user_id in range(user_id + num_users - 1):
        age, created_at, balance, username, email, first_name, last_name, updated_at, age_group = generate_user_data()
        # Get the user's ID from the database and call related functions
        newBalance = createIncome(user_id, age_group, created_at, income_data_list)
        newBalance -= createExpenses(user_id, age_group, created_at)
        newBalance -= createSavingsGoal(user_id, age_group, created_at)

        user_data_list.append((username, age, email, first_name, last_name, created_at, updated_at, balance))



if __name__ == "__main__":
    main()


#v create ages 
#v loop in ages in each do:
#v create time of joining 
#v start balnce: in each groupe of ages have a likely balnce 
# 
#v for each user create in each month from the starting date to today:
#v Income:salary rare freelace and part time
# 
# Expenses:Rent,Groceries,Utilities
# 
# Savings:goals? the problem is the random how to do ?
# 
# end blance get calculator + income -  Expenses - Savings






# insert_data = [
#     (1, "Salary", 5000.00, "Monthly"),
#     (1, "Bonus", 1000.00, "Yearly"),
#     (2, "Freelance", 800.00, "Weekly")
# ]