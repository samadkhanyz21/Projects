# Load Packages
import re
import time
import logging
from pymongo import MongoClient
from sqlalchemy import create_engine
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

#                               ***** EXTRACT *****

def mongodb_storage():
    """
    Conencts to mongodb twitter database
    """
    # Establish connection to mongodb
    client = MongoClient(host='mongodb', port=27017)

    # Connect to twitter database
    db = client.twitter

    return db

def extract(db, num_tweets):
    """
    Extracts tweets from the mongodb
    """
    # connect to the tweets collection
    tweets = db.tweets
    
    # pull out tweets with filter
    extract_tweets = tweets.find(limit=num_tweets)

    return extract_tweets

#                             ***** TRANSFORM *****

regex = [
    '@[A-Za-z0-9]+',  # Mentions
    '#',              # Hashtag
    'RT\s',           # Retweet
    'https?:\/\/\S+'  # URLs
    ]

def clean_tweets(t):
    """
    gets the text of a tweet and cleans it up 
    """
    # get tweet text
    text = t['text'] 

    # Remove regex
    for reg in regex:
        text = re.sub(reg, '', text)  
    
    return text

# Instantiate sentiment analyzer
sen_analyzer = SentimentIntensityAnalyzer()

def sentiment_score(text):
    """
    Gives sentiment score of a text
    """
    # Calculate's polarity scores 
    sentiment = sen_analyzer.polarity_scores(text)
    
    # Choose compound polarity score
    score = sentiment['compound'] 

    return score

def transform(t):
    """
    transforms extracted tweet: text cleaning and sentiment analysis
    """
    text = clean_tweets(t)
    score = sentiment_score(text)

    return text, score

#                              ***** LOAD *****

def postgres_storage():
    """
    Establish connection to postgres database
    """
    # Create postgres query engine
    pg_engine = create_engine('postgresql://postgres:1234@postgresdb:5432/tweets', echo=True)

    return pg_engine

def load(pg_engine, trans_data):
    """
    Loads tweet text and score into postgresql database
    """
    # Create a table schema
    pg_engine.execute(
        """
        CREATE TABLE IF NOT EXISTS tweet_sentiment (
        tweet_text VARCHAR(500),
        sentiment_score NUMERIC
        );
        """)

    # postgresql query for inserting text and score data
    query = "INSERT INTO tweet_sentiment VALUES (%s, %s);"
    
    # Insert new recods into the table
    for data in trans_data:
        text,score = data
        pg_engine.execute(query, (text,score))

#                           ***** ETL *****

# Give's mongodb some seconds to start
mongo_db = mongodb_storage()
time.sleep(20)

# Extract tweets from mongodb
extracted_tweets = extract(mongo_db, num_tweets=20)
logging.warning('\n***** Tweets already extracted from MongoDB *****\n')

# Transform data
transformed_data = [transform(tweet) for tweet in extracted_tweets]
logging.warning('\n***** Transformed data already generated *****\n')

# Postgresql connection
pg_engine = postgres_storage()

# Load data into postgresql
load(pg_engine, transformed_data)
logging.warning('\n***** Data already loaded into Postgres *****\n')