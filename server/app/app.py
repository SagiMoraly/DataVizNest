from flask import Flask
from flask_cors import CORS
from app.routes import data_routes  # Import data-related routes

app = Flask(__name__)
CORS(app)  # Allow Cross-Origin Resource Sharing

# Register your blueprints (subapps)
app.register_blueprint(data_routes.bp, url_prefix='/data')  # Prefix for data-related routes

# Main application entry point
if __name__ == '__main__':
    app.run(debug=True)
