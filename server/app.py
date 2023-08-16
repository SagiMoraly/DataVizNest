from flask import Flask, jsonify
from flask_cors import CORS  # Import the CORS extension

app = Flask(__name__)
CORS(app)  # Add this line to enable CORS for your app

print("hey there")
@app.route('/api/data')
def get_data():
    data = {'message': 'Hello from Python server!'}
    return jsonify(data)

if __name__ == '__main__':
    app.run()
