import random
from datetime import datetime,timedelta
from demographics.demographics import income_per_age

def calculate_months_since_creation(created_at_str):
    current_date = datetime.now()
    creation_date = datetime.strptime(created_at_str, "%Y-%m-%d")
    months_since_creation = (current_date.year - creation_date.year) * 12 + current_date.month - creation_date.month
    return months_since_creation


def createIncome(user_id, age_group, created_at, income_data_list):

    # Convert created_at datetime to string
    created_at_str = created_at.strftime("%Y-%m-%d")

    # pay day is between 1 and 20
    if not 0 > created_at.day > 21:
        new_month = created_at.month + 1
        new_year = created_at.year + (new_month - 1) // 12
        new_month = (new_month - 1) % 12 + 1
        new_day = random.randint(1, 20)
        created_at = created_at.replace(day=new_day, month=new_month, year=new_year)

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

    # Preserve the day of the month while updating the month and year
    for _ in range(months_since_creation):

        # Calculate the new month and year while keeping the same day
        new_month = created_at.month + 1
        new_year = created_at.year + (new_month - 1) // 12
        new_month = (new_month - 1) % 12 + 1

        income = age_income_list[new_year - 2020] 
        income += random.uniform(-500, 500) 
        total_amount += income

        # Update created_at with the new month and year while preserving the day
        created_at = created_at.replace(month=new_month, year=new_year)

        income_data_list.append((user_id, income, monthly, income_type, created_at))

    return total_amount
