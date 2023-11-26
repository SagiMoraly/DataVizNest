from flask import Blueprint, jsonify
from app.utils.database_utils import execute_query,insert_fake_users,create_tables
# from graphql import graphql
import json
from .querys.query import (
    query_patch_hard_reset,
    query_get_users,
    query_get_count_sources,
    query_get_income_sources,
    query_get_expenses,
    query_get_savings_goals,
    query_get_users_pie_chart,
    query_get_users_scatter_plot,
    query_get_users_box_plot,
    query_get_users_bar_chart,
    query_get_users_line_chart,
    query_get_users_heatmap
)

data_routes = Blueprint('data_routes', __name__)

@data_routes.route('/reset_and_create_tables', methods=['patch'])
def reset_and_create_tables():
    try:
        query = query_patch_hard_reset
        result = execute_query(query)
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)})

@data_routes.route('/get_users', methods=['GET'])
def get_users():
    try:
        query = query_get_users
        data = execute_query(query)
        return jsonify(data)
    except Exception as e:
        return jsonify({'error': str(e)})

@data_routes.route('/get_sum_users', methods=['GET'])
def get_sum_users():
    try:
        query = query_get_count_sources
        data = execute_query(query)
        return jsonify(data)
    except Exception as e:
        return jsonify({'error': str(e)})

@data_routes.route('/get_income_sources', methods=['GET'])
def get_income_sources():
    try:
        query = query_get_income_sources
        data = execute_query(query)
        return jsonify(data)
    except Exception as e:
        return jsonify({'error': str(e)})

@data_routes.route('/get_expenses', methods=['GET'])
def get_expenses():
    try:
        query = query_get_expenses
        data = execute_query(query)
        return jsonify(data)
    except Exception as e:
        return jsonify({'error': str(e)})

@data_routes.route('/get_savings_goals', methods=['GET'])
def get_savings_goals():
    try:
        query = query_get_savings_goals
        data = execute_query(query)
        return jsonify(data)
    except Exception as e:
        return jsonify({'error': str(e)})

@data_routes.route('/create_fake_users/<int:num_users>', methods=['POST'])
def create_fake_users(num_users):
    try:
        # Call your data insertion function with the provided number of     users
        insert_fake_users(num_users)

        response = {'message': f'{num_users} fake users created     successfully'}
        return jsonify(response), 201
    except Exception as e:
        return jsonify({'error': str(e)})

@data_routes.route('/get_users_pie_chart', methods=['GET'])
def get_users_pie_chart():
    try:
        query = query_get_users_pie_chart
        data = execute_query(query)
        data = [{'age': row[0], 'number_of_users': row[1]} for row in   data]
        return jsonify(data)
    except Exception as e:
        return jsonify({'error': str(e)})


@data_routes.route('/get_users_scatter_plot', methods=['GET'])
def get_users_scatter_plot():
    try:
        query = query_get_users_scatter_plot
        data = execute_query(query)
        return jsonify(data)
    except Exception as e:
        return jsonify({'error': str(e)})

@data_routes.route('/get_users_box_plot', methods=['GET'])
def get_users_box_plot():
    try:
        query = query_get_users_box_plot
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
    except Exception as e:
        return jsonify({'error': str(e)})


@data_routes.route('/get_users_bar_chart', methods=['GET'])
def get_users_bar_chart():
    try:
        query = query_get_users_bar_chart
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
    except Exception as e:
        return jsonify({'error': str(e)})

@data_routes.route('/get_users_line_chart', methods=['GET'])
def get_users_line_chart():
    query = query_get_users_line_chart
    age_group_colors = {
    "18-29": "tokens('dark').blueAccent[300]",
    "30-39": "tokens('dark').redAccent[200]",
    "40-49": "tokens('dark').greenAccent[400]",
    "50-59": "tokens('dark').yellowAccent[700]",
    "60-69": "tokens('dark').orangeAccent[500]",
    "70-79": "tokens('dark').purpleAccent[300]",
    "80-90": "tokens('dark').pinkAccent[200]",
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
                'color': age_group_colors.get(age_group, 'black'), 
                'data': formatted_data  
            })
        return jsonify(result)

    except Exception as e:
        return jsonify({'error': str(e)})
    
@data_routes.route('/get_users_heatmap', methods=['GET'])
def get_users_heatmap():
    try:
        query = query_get_users_heatmap
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
    except Exception as e:
        return jsonify({'error': str(e)})

