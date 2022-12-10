from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "hello"

    @app.route("/")
    def home():
        return "<h1>Hello Me</h1>"

    @app.route("/pop")
    def pop():
        return "<h1>Yes Lord!</h1>"

    return app