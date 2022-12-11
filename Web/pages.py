from flask import Blueprint, render_template, request, redirect 
import os 
pages = Blueprint('pages', __name__)

@pages.route("/", methods = ["GET","POST"])
def home():
    return render_template("index.html")