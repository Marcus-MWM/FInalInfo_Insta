from flask import Flask
from flask import Blueprint, render_template, request, redirect 

def create_app():
    app = Flask(__name__)

    @app.route("/", methods = ["GET", "POST"])
    def home():
        return render_template("init.html")