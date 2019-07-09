# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# API Authentication 

# Importing TWEEPY Library
import tweepy

from textblob import TextBlob

import nltk
nltk.download()

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

access_token = "713422271528964096-R9Jg8MDbcQdQ4zv5nfsmke0cBUie0FF"
access_token_secret = "FhQMCTLauSNeGONM7lMU1rY22zfoVgnt5BeEQGxQ46Khu"
consumer_key = "V6Rp0SDqzQxI0EGTMlcCE6wX5"
consumer_secret = "0wnO5LPfEW6uSpiMPlpL5YxXYXyAfs0zazSt5IoR8N7PXWGogI"

# Creating the authentication object
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# Setting your access token and secret
auth.set_access_token(access_token, access_token_secret)
# Creating the API object while passing in auth information
api = tweepy.API(auth) 

# Using the API object to get tweets from your timeline, and storing it in a variable called public_tweets
public_tweets = api.search('Salesforce')
# foreach through all tweets pulled
for tweet in public_tweets:
   # printing the text stored inside the tweet object
   print (tweet.text)
   analysis = TextBlob(tweet.text)
   print(analysis.sentiment)
   print(analysis.subjectivity)

filename = 'metamorphosis_clean.txt'
file = open(filename, 'rt')
text = file.read()
file.close()
# split into words
from nltk.tokenize import word_tokenize
tokens = word_tokenize(text)
# convert to lower case
tokens = [w.lower() for w in tokens]
# remove punctuation from each word
import string
table = str.maketrans('', '', string.punctuation)
stripped = [w.translate(table) for w in tokens]
# remove remaining tokens that are not alphabetic
words = [word for word in stripped if word.isalpha()]
# filter out stop words
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))
words = [w for w in words if not w in stop_words]
print(words[:100])