from instaloader import *  
#import pandas as pd 
user = "chrisgx21"

L = instaloader.Instaloader() 
L.load_session_from_file(user)

posts = Profile.from_username(L.context, 'chrisgx21').get_posts()

for post in posts:
    for comment in post.get_comments(): 
        print(comment)
        
