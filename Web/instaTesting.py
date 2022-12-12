from instaloader import *  
import pandas as pd 
from IPython.display import display
user = "chrisgx21"

L = instaloader.Instaloader() 
L.load_session_from_file(user)

posts = Profile.from_username(L.context, 'chrisgx21').get_posts()

rngDf = pd.DataFrame()
for post in posts:
    for comment in post.get_comments(): 
        text = getattr(comment,"text")
        id = getattr(comment,"id")
        tempdf = {"ID": id,"Text": text}

        rngDf = rngDf.append(tempdf, ignore_index = True)

display(rngDf)
