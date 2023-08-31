from flask import Blueprint, jsonify
from app.utils.database_utils import execute_query,insert_fake_users,create_tables

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