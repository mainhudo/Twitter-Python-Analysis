# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# API Authentication 

# Importing TWEEPY Library
import tweepy

from textblob import TextBlob


class MyApp():
    def __init__(self, title=None, author="", date="" ):
         
           self.title =   title
           self.author =  author
           self.date = date


App = MyApp ("Realtime Tweet Display")

print(App.title)
print(App.author)
print(App.date)
yourName = input("Please enter your Twitter handle with @ : ")



# Store OAuth authentication credentials in relevant variables

access_token = "XXX"  #Confidential information only applies to my tweets
access_token_secret = "XXX"
consumer_key = "XXX"
consumer_secret = "XXX"

# Creating the authentication object
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# Setting your access token and secret
auth.set_access_token(access_token, access_token_secret)
# Creating the API object while passing in auth information
api = tweepy.API(auth) 

# Using the API object to get tweets from your timeline, and storing it in a variable called public_tweets
public_tweets = api.search('SGO48')  #You can use whatever hashtag you want, mine is a girlband
# foreach through all tweets pulled
for tweet in public_tweets:
   # printing the text stored inside the tweet object
   print (tweet.text)
   analysis = TextBlob(tweet.text)
   print(analysis.sentiment)
   print(analysis.subjectivity)

