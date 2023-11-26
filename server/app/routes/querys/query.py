
query_get_users = """SELECT
	JSON_OBJECT('id',id, 'username', username, 'age',age,  'email',email, 'firstName',firstName, 'lastName',lastName, 'createdAt',createdAt, 'updatedAt',updatedAt, 'balance', balance, 'startBalance',startBalance)
    FROM users"""
query_patch_hard_reset = """
CREATE DATABASE IF NOT EXISTS personal_finance_management_system;

USE personal_finance_management_system;

DROP TABLE IF EXISTS expenses;
DROP TABLE IF EXISTS income;
DROP TABLE IF EXISTS savings_goals;
DROP TABLE IF EXISTS users;

    CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        username VARCHAR(50) NOT NULL,
        age INT NOT NULL,
        email VARCHAR(100) NOT NULL,
        firstName VARCHAR(50),
        lastName VARCHAR(50),
        createdAt DATETIME,
        updatedAt DATETIME,
        balance DECIMAL(10, 2),
        startBalance DECIMAL(10, 2)
    );
    CREATE TABLE IF NOT EXISTS income (
        id INT AUTO_INCREMENT PRIMARY KEY,
        user_id INT,
        name VARCHAR(100),
        amount DECIMAL(10, 2),
        frequency VARCHAR(50),
        createdAt DATETIME,
        FOREIGN KEY (user_id) REFERENCES users(id)
    );
    CREATE TABLE IF NOT EXISTS expenses (
        id INT AUTO_INCREMENT PRIMARY KEY,
        user_id INT,
        name VARCHAR(100),
        amount DECIMAL(10, 2),
        createdAt DATETIME,
        FOREIGN KEY (user_id) REFERENCES users(id)
    );
    CREATE TABLE IF NOT EXISTS savings_goals (
        id INT AUTO_INCREMENT PRIMARY KEY,
        user_id INT,
        name VARCHAR(100),
        targetAmount DECIMAL(10, 2),
        currentAmount DECIMAL(10, 2),
        targetDate DATE,
        createdAt DATETIME,
        FOREIGN KEY (user_id) REFERENCES users(id)
    );
"""
query_get_income_sources = "SELECT * FROM income"
query_get_count_sources = "select COUNT(id) from users"
query_get_expenses = "SELECT * FROM expenses"
query_get_savings_goals = "SELECT * FROM savings_goals"
query_get_users_pie_chart = """SELECT 
    CASE
        WHEN age BETWEEN 18 AND 29 THEN 'Age18-29'
        WHEN age BETWEEN 30 AND 39 THEN 'Age30-39'
        WHEN age BETWEEN 40 AND 49 THEN 'Age40-49'
        WHEN age BETWEEN 50 AND 59 THEN 'Age50-59'
        WHEN age BETWEEN 60 AND 69 THEN 'Age60-69'
        WHEN age BETWEEN 70 AND 79 THEN 'Age70-79'
        WHEN age BETWEEN 80 AND 90 THEN 'Age80-90'
    ELSE 'Other'
END AS age_group,
    COUNT(*) AS number_of_users
        FROM users
            GROUP BY age_group;
"""
query_get_users_scatter_plot = """SELECT
    JSON_OBJECT(
        'id', age_group,
        'data', JSON_ARRAYAGG(
            JSON_OBJECT(
                'x', age,
                'y', startBalance
            )
        )
    ) AS group_data
FROM (
    SELECT
        CASE
            WHEN age BETWEEN 18 AND 29 THEN 'Age18-29'
            WHEN age BETWEEN 30 AND 39 THEN 'Age30-39'
            WHEN age BETWEEN 40 AND 49 THEN 'Age40-49'
            WHEN age BETWEEN 50 AND 59 THEN 'Age50-59'
            WHEN age BETWEEN 60 AND 69 THEN 'Age60-69'
            WHEN age BETWEEN 70 AND 79 THEN 'Age70-79'
            WHEN age BETWEEN 80 AND 90 THEN 'Age80-90'
            ELSE 'Other'
        END AS age_group,
        age,
        startBalance
    FROM users
) AS subquery
GROUP BY age_group;
"""
query_get_users_box_plot = """SELECT
    age_group,
    'A' AS subgroup,
    AVG(amount) OVER (PARTITION BY age_group) AS mu,
    STDDEV(amount) OVER (PARTITION BY age_group) AS sd,
    COUNT(amount) OVER (PARTITION BY age_group) AS n,
    amount AS value
FROM (
    SELECT
        CASE
            WHEN u.age BETWEEN 18 AND 29 THEN 'Age18-29'
            WHEN u.age BETWEEN 30 AND 39 THEN 'Age30-39'
            WHEN u.age BETWEEN 40 AND 49 THEN 'Age40-49'
            WHEN u.age BETWEEN 50 AND 59 THEN 'Age50-59'
            WHEN u.age BETWEEN 60 AND 69 THEN 'Age60-69'
            WHEN u.age BETWEEN 70 AND 79 THEN 'Age70-79'
            WHEN u.age BETWEEN 80 AND 90 THEN 'Age80-90'
            ELSE 'Other'
        END AS age_group,
        i.amount
    FROM personal_finance_management_system.users u
    LEFT JOIN personal_finance_management_system.income i ON u.id = i.user_id
) AS main
ORDER BY age_group, subgroup, value;

    """

query_get_users_bar_chart = """SELECT
age_group,
    SUM(CASE WHEN name = 'freelance' THEN 1 ELSE 0 END) AS freelance,
    SUM(CASE WHEN name = 'part_time' THEN 1 ELSE 0 END) AS part_time,
    SUM(CASE WHEN name = 'salary' THEN 1 ELSE 0 END) AS salary
FROM (
    SELECT
        CASE
            WHEN u.age BETWEEN 18 AND 29 THEN '18-29'
            WHEN u.age BETWEEN 30 AND 39 THEN '30-39'
            WHEN u.age BETWEEN 40 AND 49 THEN '40-49'
            WHEN u.age BETWEEN 50 AND 59 THEN '50-59'
            WHEN u.age BETWEEN 60 AND 69 THEN '60-69'
            WHEN u.age BETWEEN 70 AND 79 THEN '70-79'
            WHEN u.age BETWEEN 80 AND 90 THEN '80-90'
            ELSE 'Other'
        END AS age_group,
        i.name
    FROM users u
    LEFT JOIN income i ON u.id = i.user_id
) AS income_data
GROUP BY age_group;
    """

query_get_users_line_chart = """  
    SELECT
    age_group,
    JSON_ARRAYAGG(
        JSON_OBJECT(
            'x', income_year,
            'y', total_income
        )
    ) AS data
FROM (
    SELECT
        CASE
            WHEN u.age BETWEEN 18 AND 29 THEN '18-29'
            WHEN u.age BETWEEN 30 AND 39 THEN '30-39'
            WHEN u.age BETWEEN 40 AND 49 THEN '40-49'
            WHEN u.age BETWEEN 50 AND 59 THEN '50-59'
            WHEN u.age BETWEEN 60 AND 69 THEN '60-69'
            WHEN u.age BETWEEN 70 AND 79 THEN '70-79'
            WHEN u.age BETWEEN 80 AND 90 THEN '80-90'
            ELSE 'Other'
        END AS age_group,
        YEAR(income.createdAt) AS income_year,
        SUM(income.amount) AS total_income
    FROM users u
    LEFT JOIN income ON u.id = income.user_id
    GROUP BY age_group, income_year
) AS income_data
GROUP BY age_group;
    """

query_get_users_heatmap = """
SELECT
    CASE
        WHEN u.age BETWEEN 18 AND 29 THEN '18-29'
        WHEN u.age BETWEEN 30 AND 39 THEN '30-39'
        WHEN u.age BETWEEN 40 AND 49 THEN '40-49'
        WHEN u.age BETWEEN 50 AND 59 THEN '50-59'
        WHEN u.age BETWEEN 60 AND 69 THEN '60-69'
        WHEN u.age BETWEEN 70 AND 79 THEN '70-79'
        WHEN u.age BETWEEN 80 AND 90 THEN '80-90'
        ELSE 'Other'
    END AS age_group,
    AVG(CASE WHEN i.name = 'salary' THEN i.amount ELSE 0 END) AS income_salary,
    AVG(CASE WHEN i.name = 'part_time' THEN i.amount ELSE 0 END) AS income_part_time,
    AVG(CASE WHEN i.name = 'freelance' THEN i.amount ELSE 0 END) AS income_freelance,
    AVG(CASE WHEN e.name = 'Utilities' THEN e.amount ELSE 0 END) ASexpenses_Utilities,
    AVG(CASE WHEN e.name = 'Rent' THEN e.amount ELSE 0 END) AS expenses_Rent,
    AVG(CASE WHEN e.name = 'Groceries' THEN e.amount ELSE 0 END) ASexpenses_Groceries,
    AVG(CASE WHEN e.name = 'Entertainment' THEN e.amount ELSE 0 END) ASexpenses_Entertainment,
    AVG(u.startBalance) AS start_balance,
    AVG(u.balance) AS balance
    -- Add other expense categories here if needed
FROM users u
LEFT JOIN income i ON u.id = i.user_id
LEFT JOIN expenses e ON u.id = e.user_id
GROUP BY age_group;
"""

