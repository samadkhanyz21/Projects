import os
import json
import time
import requests
import pandas as pd
import sqlalchemy as db
from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv()

# URL for slackbot App
webhook_url = os.getenv("Webhook_url") 
time.sleep(20)

def postgres_storage():
    """
    Establish connection to postgresdb
    """
    # create sql query engine
    pg_engine = create_engine('postgresql://postgres:1234@postgresdb:5432/tweets', echo=True)
    
    return pg_engine

pg = postgres_storage()

# Query for operations in postgres
query ='''SELECT tweet_text, sentiment_score 
FROM tweet_sentiment 
ORDER BY sentiment_score ASC;
'''

# Collecting info from postgres & storing it in the pandas dataframe
df_tweets = pd.read_sql_query("SELECT * FROM tweet_sentiment", pg)

# Printing score in slackbot App after analysis
for i in range(len(df_tweets)):
	tweet =df_tweets['tweet_text'].iloc[i] 
	score = df_tweets['sentiment_score'].iloc[i] 
	text_ = f"Tweet_{i}: '{tweet}' and the corresponding score: '{score}'"
	requests.post(url=webhook_url, json={'text':text_})
	time.sleep(1)