from flask import Blueprint, render_template, request, redirect, url_for
import os 
import getFirefoxSession
from instaloader import *
import pandas as pd  
import machineLearn

pages = Blueprint('pages', __name__)

@pages.route("/", methods = ["GET","POST"])
def index():
    #If the user has submitted their username, send them over to other page 
    if request.method == "POST": 
        return redirect(url_for('pages.showBaseData'))
    else: 
        return render_template("index.html")


@pages.route("/showBaseData", methods = ["GET", "POST"])
def showBaseData():
    #Checking to see if recieved post data
    if request.method == "POST": 
        usr = request.form["username"]

        #Load session from Firefox Cookies 
        getFirefoxSession.runFireScript()
        L = instaloader.Instaloader() 

        #Logging in via session data
        L.load_session_from_file(usr)

        #getting posts from profile 
        posts = Profile.from_username(L.context, usr).get_posts()
        
        #Getting all posts on Account and then going through each comment on post, grabbing text and id 
        postDf = pd.DataFrame()
        for post in posts:
            for comment in post.get_comments(): 
                text = getattr(comment,"text")
                id = getattr(comment,"id")

                tempDf = {"User ID": id,"Message": text}
                postDf = postDf.append(tempDf, ignore_index = True)
                postDf.to_csv("Web\postData.csv") 
        data = postDf.values  

        return render_template("showBaseData.html", data = data) 
    else:
        return f"<h1>Oh no! Something went wrong!<h1>"


@pages.route("/results")
def results():
    #Basically need to run the machinie learning algo and then with each row, calculate if spam or not

    outcomeDf = pd.DataFrame()
    machineLearn.main()
    postDf = pd.read_csv("ML_Prediction.csv")

    data = postDf.values
    return render_template("results.html", data = data)
