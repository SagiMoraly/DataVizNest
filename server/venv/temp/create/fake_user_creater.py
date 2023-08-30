from create.user.fake_user import generate_user_data
from create.income.fake_income import createIncomeAndExpense
from insert_data.fake_data_insert import *


# Example of how to use the functions
def fake_user_creater(cursor, connection,  num_users = 100):
    # num_users = 100
    user_data_list = []
    income_data_list = []
    expense_data_list = []
    # Execute a SELECT query to get the last inserted ID from the "users" table

    cursor.execute("SELECT MAX(id) FROM personal_finance_management_system.users;")
    user_id = cursor.fetchone()[0]
    if not user_id:
        user_id = 0
    user_id += 1
    # user_id = cursor.lastrowid + 1 #return 0 if there is none so we will start on 1 or one after last id

    for user_id in range(user_id, user_id + num_users):
        age, created_at, balance, username, email, first_name, last_name, updated_at, age_group = generate_user_data()
        # Get the user's ID from the database and call related functions
        newBalance = balance
        newBalance += createIncomeAndExpense(user_id, age_group, created_at, income_data_list,expense_data_list)

        # print(balance,newBalance)
        user_data_list.append((username, age, email, first_name, last_name, created_at, updated_at, newBalance, balance))

    # input the data 
    insert_user_data(cursor, connection, user_data_list)
    insert_income_data(cursor, connection, income_data_list)
    insert_expense_data(cursor, connection, expense_data_list)


# if __name__ == "__main__":
#     fake_user_creater()


#v create ages 
#v loop in ages in each do:
#v create time of joining 
#v start balnce: in each groupe of ages have a likely balnce 
# 
#v for each user create in each month from the starting date to today:
#v Income:salary rare freelace and part time
# 
#v Expenses:Rent,Groceries,Utilities
# 
# Savings:goals? the problem is the random how to do ?
# 
# end blance get calculator + income -  Expenses - Savings






# insert_data = [
#     (1, "Salary", 5000.00, "Monthly"),
#     (1, "Bonus", 1000.00, "Yearly"),
#     (2, "Freelance", 800.00, "Weekly")
# ]