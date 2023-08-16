from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY']  = 'java is just bad'

    return app