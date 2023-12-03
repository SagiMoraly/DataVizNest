import faker
import random
import datetime
from ...demographics.demographics import balance_per_age 
# import balance_per_age from "../../demographics/demographics"

# Define age groups and their probabilities
age_groups = ["18-29", "30-39", "40-49", "50-59", "60-69", "70-79", "80-90"]
age_preferences = [0.4, 0.2, 0.15, 0.1, 0.08, 0.06, 0.01]

# Create a Faker generator
fake = faker.Faker()

# Generate a random age based on age preferences
def generate_age_group():
    age_group = random.choices(age_groups, weights=age_preferences)[0]
    return age_group

def split_age(age_group):
    age_range = age_group.split("-")
    return random.randint(int(age_range[0]), int(age_range[1]))


# Create a random date that decreases over the years
def generate_created_at(year):
    current_year = datetime.datetime.now().year
    years_passed = current_year - year
    random_days = random.randint(0, 365 * years_passed)
    return datetime.datetime(year, 1, 1) + datetime.timedelta(days=random_days)

# Calculate balance based on age and created year
def calculate_balance(age_group, created_at):
    reference_year = 2020  # The starting year in the balance_per_age dictionary
    years_passed = created_at.year - reference_year
    if years_passed < 0:
        years_passed = 0
    
    # balance_range = balance_per_age[age_group][years_passed]
    # return round(random.uniform(balance_range[0], balance_range[1]), 2)

    # Get the list of balance values associated with the age group
    balance_values = balance_per_age[age_group]

    # Calculate the index based on years_passed and the number of balance values
    index = min(years_passed, len(balance_values) - 1)

    # Get the corresponding balance value from the list
    base_balance = balance_values[index]

    # Generate a random variation around the base balance
    random_variation = random.uniform(-1000, 1000)  # Adjust the range as needed
    balance = base_balance + random_variation

    return round(balance, 2)

# Create user data
def generate_user_data():
    age_group = generate_age_group()
    created_at = generate_created_at(random.randint(2020, 2023))#to change so it will look real
    age = split_age(age_group)
    balance = calculate_balance(age_group,created_at)
    username = fake.user_name()
    email = fake.email()
    first_name = fake.first_name()
    last_name = fake.last_name()
    updated_at = datetime.datetime.now()
    
    return age, created_at, balance, username, email, first_name, last_name, updated_at, age_group
