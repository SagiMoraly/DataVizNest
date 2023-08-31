from flask import Flask
from flask_cors import CORS
# from routes.data_routes import data_routes  
from app.routes.data_routes import data_routes
# from .routes.data_routes import data_routes

app = Flask( __name__)

CORS(app)
app.register_blueprint(data_routes)  

print("Flask server is up and running!")

if __name__ == '__main__':
    app.run(debug=True)



