from flask import Blueprint, jsonify
from app.utils.database_utils import execute_query,insert_fake_users,create_tables
# from graphql import graphql
import json

data_routes = Blueprint('data_routes', __name__)

@data_routes.route('/create_tables', methods=['GET'])
def create_tables():
    query = create_tables()
    result = execute_query(query)
    return jsonify(result)

@data_routes.route('/get_users', methods=['GET'])
def get_users():
    query = "SELECT * FROM users"
    data = execute_query(query)
    return jsonify(data)

@data_routes.route('/get_income_sources', methods=['GET'])
def get_income_sources():
    query = "SELECT * FROM income"
    data = execute_query(query)
    return jsonify(data)

@data_routes.route('/get_expenses', methods=['GET'])
def get_expenses():
    query = "SELECT * FROM expenses"
    data = execute_query(query)
    return jsonify(data)

@data_routes.route('/get_savings_goals', methods=['GET'])
def get_savings_goals():
    query = "SELECT * FROM savings_goals"
    data = execute_query(query)
    return jsonify(data)

@data_routes.route('/create_fake_users/<int:num_users>', methods=['POST'])
def create_fake_users(num_users):
    # Call your data insertion function with the provided number of users
    insert_fake_users(num_users)
    
    response = {'message': f'{num_users} fake users created successfully'}
    return jsonify(response), 201

@data_routes.route('/get_users_pie_chart', methods=['GET'])
def get_users_pie_chart():
    query = """SELECT
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
    data = execute_query(query)
    data = [{'age': row[0], 'number_of_users': row[1]} for row in data]
    return jsonify(data)


@data_routes.route('/get_users_scatter_plot', methods=['GET'])
def get_users_scatter_plot():
    query = """SELECT
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
    AVG(startBalance) AS average_start_balance
    FROM users
    GROUP BY age_group;
    """
    data = execute_query(query)
    data = [{'age': row[0], 'average_start_balance': row[1]} for row in data]
    return jsonify(data)

@data_routes.route('/get_users_box_plot', methods=['GET'])
def get_users_box_plot():
    query = """SELECT
    age_group,
    'A' AS subgroup,
    AVG(amount) AS mu,
    STDDEV(amount) AS sd,
    COUNT(amount) AS n,
    (
        SELECT
            AVG(amount) AS median
        FROM (
            SELECT
                i.amount,
                ROW_NUMBER() OVER (ORDER BY i.amount) as row_num,
                COUNT(*) OVER () as total_rows
            FROM personal_finance_management_system.users u
            LEFT JOIN personal_finance_management_system.income i ON u.id = i.user_id
            WHERE
                CASE
                    WHEN u.age BETWEEN 18 AND 25 THEN '18-25'
                    WHEN u.age BETWEEN 26 AND 35 THEN '26-35'
                    WHEN u.age BETWEEN 36 AND 45 THEN '36-45'
                    WHEN u.age BETWEEN 46 AND 55 THEN '46-55'
                    WHEN u.age BETWEEN 56 AND 65 THEN '56-65'
                    WHEN u.age BETWEEN 66 AND 75 THEN '66-75'
                    WHEN u.age BETWEEN 76 AND 85 THEN '76-85'
                    ELSE 'Other'
                END = age_group
        ) AS ranked
        WHERE row_num IN (FLOOR((total_rows+1)/2), FLOOR((total_rows+2)/2))
    ) AS value
FROM (
    SELECT
        CASE
            WHEN u.age BETWEEN 18 AND 25 THEN '18-25'
            WHEN u.age BETWEEN 26 AND 35 THEN '26-35'
            WHEN u.age BETWEEN 36 AND 45 THEN '36-45'
            WHEN u.age BETWEEN 46 AND 55 THEN '46-55'
            WHEN u.age BETWEEN 56 AND 65 THEN '56-65'
            WHEN u.age BETWEEN 66 AND 75 THEN '66-75'
            WHEN u.age BETWEEN 76 AND 85 THEN '76-85'
            ELSE 'Other'
        END AS age_group,
        i.amount
    FROM personal_finance_management_system.users u
    LEFT JOIN personal_finance_management_system.income i ON u.id = i.user_id
) AS main
GROUP BY age_group;
    """
    data = execute_query(query)
    result = [
        {
            'group': row[0],
            'subgroup': row[1],
            'mu': row[2],
            'sd': row[3],
            'n': row[4],
            'value': row[5]
        }
        for row in data
    ]
    return jsonify(result)


@data_routes.route('/get_users_bar_chart', methods=['GET'])
def get_users_bar_chart():
    query = """SELECT
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
    data = execute_query(query)
    result = []
    for row in data:
        age_group = row[0]
        freelance = row[1]
        part_time = row[2]
        salary = row[3]
        
        freelance_color = "HSL(33, 100%, 50%)"
        part_time_color = "HSL(147, 50%, 50%)"
        salary_color = "HSL(225, 73%, 57%)"

        result.append({
            'country': age_group,
            'freelance': freelance,
            'freelanceColor': freelance_color,
            'part_time': part_time,
            'part_timeColor': part_time_color,
            'salary': salary,
            'salaryColor': salary_color
        })

    return jsonify(result)

@data_routes.route('/get_users_line_chart', methods=['GET'])
def get_users_line_chart():
    query = """  
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
    age_group_colors = {
        "18-29": "blue",
        "30-39": "red",
        # Define colors for other age groups here...
    }
    try:
        data = execute_query(query)
        result = []
        for row in data:
            age_group = row[0]
            income_data = row[1]
            income_data = json.loads(income_data)
            formatted_data = [{
                'x': str(item['x']),
                'y': item['y']
            } for item in income_data]

            result.append({
                'id': age_group,
                'color': age_group_colors.get(age_group, 'black'),  # Get color from the dictionary
                'data': formatted_data  
            })
        return jsonify(result)

    except Exception as e:
        return jsonify({'error': str(e)})
    
@data_routes.route('/get_users_heatmap', methods=['GET'])
def get_users_heatmap():
    query = """
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
        AVG(CASE WHEN e.name = 'Utilities' THEN e.amount ELSE 0 END) AS expenses_Utilities,
        AVG(CASE WHEN e.name = 'Rent' THEN e.amount ELSE 0 END) AS expenses_Rent,
        AVG(CASE WHEN e.name = 'Groceries' THEN e.amount ELSE 0 END) AS expenses_Groceries,
        AVG(CASE WHEN e.name = 'Entertainment' THEN e.amount ELSE 0 END) AS expenses_Entertainment,
        AVG(u.startBalance) AS start_balance,
        AVG(u.balance) AS balance
        -- Add other expense categories here if needed
    FROM users u
    LEFT JOIN income i ON u.id = i.user_id
    LEFT JOIN expenses e ON u.id = e.user_id
    GROUP BY age_group;
    """
    data = execute_query(query)
    result = []
    for row in data:
        age_group = row[0]
        result_data = [
            {'x': 'start_balance', 'y': row[1]},
            {'x': 'income_salary', 'y': row[2]},
            {'x': 'income_part_time', 'y': row[3]},
            {'x': 'income_freelance', 'y': row[4]},
            {'x': 'expenses_Utilities', 'y': -row[5]},
            {'x': 'expenses_Rent', 'y': -row[6]},
            {'x': 'expenses_Groceries', 'y': -row[7]},
            {'x': 'expenses_Entertainment', 'y': -row[8]},
            {'x': 'balance', 'y': row[9]}
        ]
        result.append({'id': age_group, 'data': result_data})
    
    return jsonify(result)

