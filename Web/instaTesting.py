from instaloader import *  
import pandas as pd 
from IPython.display import display
user = "chrisgx21"

L = instaloader.Instaloader() 
L.load_session_from_file(user)

posts = Profile.from_username(L.context, 'chrisgx21').get_posts()

postDf = pd.DataFrame()
for post in posts:
    for comment in post.get_comments(): 
        text = getattr(comment,"text")
        id = getattr(comment,"id")
        tempdf = {"ID": id,"Text": text}

        postDf = postDf.append(tempdf, ignore_index = True)
postDf.to_csv("Web\postData.csv")

