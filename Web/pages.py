from flask import Blueprint, render_template, request, redirect 
import os 
import getFirefoxSession
from instaloader import *  
pages = Blueprint('pages', __name__)

@pages.route("/", methods = ["GET","POST"])
def home():
    if request.method == "POST":
        if request.files:

            csv = request.files["csv"]
            csv.save(os.path.join("uploads", csv.filename))
            return redirect(request.url)
            
    return render_template("index.html")

@pages.route("/", methods = ["GET", "POST"])
def showBaseData(): 
    if request.method == "POST":
        # Login to the user's profile
        username = request.form.get('username')
        getFirefoxSession.runFireScript()
        L = instaloader.Instaloader() 
        L.load_session_from_file(username)
        posts = Profile.from_username(L.context, 'chrisgx21').get_posts()

        for post in posts:
            for comment in post.get_comments(): 
                print(comment)

    return render_template("showBaseData.html")
