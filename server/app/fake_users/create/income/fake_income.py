import random
from datetime import datetime,timedelta
from ...demographics.demographics import income_per_age,rent_per_age_year

def calculate_months_since_creation(created_at_str):
    current_date = datetime.now()
    creation_date = datetime.strptime(created_at_str, "%Y-%m-%d")
    months_since_creation = (current_date.year - creation_date.year) * 12 + current_date.month - creation_date.month
    return months_since_creation


def generate_expenses(created_at, user_id, rent, expense_data_list):

    # List of mandatory and optional expense categories
    expense_categories = ["Rent", "Groceries", "Utilities", "Entertainment"]
    expense_category_weights = [1.0, 1.0, 0.4, 0.2]  # Adjust weights as needed
    total_expense = 0

    # Simulate expenses for mandatory categories
    for category in ["Rent", "Groceries"]:
        if not category == "Rent":
            expense = random.uniform(300, 600)  # Adjust the range as needed
            total_expense += expense
        else:
            expense = rent
            total_expense += expense
        expense_data_list.append((user_id, category, expense, created_at))

    # Simulate expenses for optional categories
    optional_categories = random.choices(expense_categories[2:], expense_category_weights[2:], k=random.randint(0, 2))
    for category in optional_categories:
        expense = random.uniform(10, 200)  # Adjust the range as needed
        total_expense += expense
        expense_data_list.append((user_id, category, expense, created_at))
    # Update created_at with the new month and year while preserving the day

    return total_expense




def createIncomeAndExpense(user_id, age_group, created_at, income_data_list, expense_data_list):

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
    age_rent_list = rent_per_age_year[age_group]
    rent_off_set = random.uniform(-500, 500) 

    # Preserve the day of the month while updating the month and year
    for _ in range(months_since_creation):

        # Calculate the new month and year while keeping the same day
        new_month = created_at.month + 1
        new_year = created_at.year + (new_month - 1) // 12
        new_month = (new_month - 1) % 12 + 1

        income = age_income_list[new_year - 2020] 
        rent = age_rent_list[new_year - 2020] 
        income += random.uniform(-500, 500) 
        rent = rent + rent_off_set
        total_amount += income - rent

        # Update created_at with the new month and year while preserving the day
        created_at = created_at.replace(month=new_month, year=new_year)

        generate_expenses(created_at, user_id, rent, expense_data_list)

        income_data_list.append((user_id, income, monthly, income_type, created_at))

    return total_amount

