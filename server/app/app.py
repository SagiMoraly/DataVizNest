from flask import Flask
from flask_cors import CORS
from routes.data_routes import data_routes  
# from .routes.data_routes import data_routes

app = Flask( __name__)

CORS(app)
# app.register_blueprint(data_routes)  

print("Flask server is up and running!")

if __name__ == '__main__':
    app.run(debug=True)




# from flask import Flask
# from flask_cors import CORS
# from .routes.data_routes import data_routes  # Import data-related routes

# app = Flask(__name__)
# CORS(app)  # Allow Cross-Origin Resource Sharing

# # Register your blueprints (subapps)
# app.register_blueprint(data_routes, url_prefix='/data')  # Prefix for data-related routes

# print("Flask server is up and running!")

# # Main application entry point
# if __name__ == '__main__':
#     app.run(debug=True)
