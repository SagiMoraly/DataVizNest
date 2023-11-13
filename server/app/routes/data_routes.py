from flask import Blueprint, jsonify
from app.utils.database_utils import execute_query,insert_fake_users,create_tables
# from graphql import graphql

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
        CASE
            WHEN u.age BETWEEN 18 AND 25 THEN '18-25'
            WHEN u.age BETWEEN 26 AND 35 THEN '26-35'
            WHEN u.age BETWEEN 36 AND 45 THEN '36-45'
            WHEN u.age BETWEEN 46 AND 55 THEN '46-55'
            WHEN u.age BETWEEN 56 AND 65 THEN '56-65'
            WHEN u.age BETWEEN 66 AND 75 THEN '66-75'
            WHEN u.age BETWEEN 76 AND 85 THEN '76-85'
            ELSE 'Other'
        END AS group,
        'A' AS subgroup,  -- You can modify this if you have subgroup information
        AVG(i.amount) AS mu,
        STDDEV(i.amount) AS sd,
        COUNT(i.amount) AS n,
        PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY i.amount) AS value
    FROM users u
    LEFT JOIN income i ON u.id = i.user_id
    GROUP BY group;
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