import os
import time
import logging
#import config
import tweepy
from tweepy import API
from dotenv import load_dotenv
from pymongo import MongoClient

# take environment variables from .env
load_dotenv() 

def mongodb_storage():
    """
    Connects to mongodb and creates tweets collection in twitter database
    """
    # establish connection to mongodb container
    client = MongoClient(host='mongodb', port=27017)

    # create twitter database
    db = client.twitter
    # equivalent of CREATE DATABASE twitter;

    # define the collection
    collection = db.tweets
    # equivalent of CREATE TABLE tweets;

    return collection

# define the collection
COLLECTION = mongodb_storage()

BEARER_TOKEN = os.getenv("BEARER_TOKEN")
twitter_client = tweepy.Client(bearer_token=BEARER_TOKEN, wait_on_rate_limit=True)

response = twitter_client.get_user(username = 'guardian', 
                                    user_fields = ['created_at', 
                                                    'description',
                                                    'location', 
                                                    'public_metrics', 
                                                    'profile_image_url'])
    
user = response.data

cursor = tweepy.Paginator(method=twitter_client.get_users_tweets,
                            id=user.id,
                            exclude=['replies', 'retweets'],
                            tweet_fields=['author_id', 'created_at', 'public_metrics']).flatten(limit=50)

tweet_num = 1
for tweet in cursor:
    COLLECTION.insert_one(dict(tweet))
    logging.warning(f"\n*****Tweet {tweet_num} already inserted into MongoDB*****\n")
    tweet_num += 1
    time.sleep(1)