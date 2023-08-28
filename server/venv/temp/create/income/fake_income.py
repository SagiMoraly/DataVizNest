import random
from datetime import datetime,timedelta
from demographics.demographics import income_per_age

def calculate_months_since_creation(created_at_str):
    current_date = datetime.now()
    creation_date = datetime.strptime(created_at_str, "%Y-%m-%d")
    months_since_creation = (current_date.year - creation_date.year) * 12 + current_date.month - creation_date.month
    return months_since_creation


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
    income_index = min(income_index, len(age_income_list) - 1)

    return age_income_list[income_index]


def createIncome(user_id, age_group, created_at, income_data_list):

    # Convert created_at datetime to string
    created_at_str = created_at.strftime("%Y-%m-%d")

    # Calculate months since user creation
    months_since_creation = calculate_months_since_creation(created_at_str)
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

        created_at += timedelta(days=30)

    return total_amount

