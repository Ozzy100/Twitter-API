import os
import tweepy
from dotenv import load_dotenv
import pandas as pd
import sqlalchemy as db

# Load environment variables
load_dotenv()

consumer_key = os.environ.get("TWITTER_API_KEY")
consumer_secret = os.environ.get("TWITTER_API_KEY_SECRET")
access_token = os.environ.get("TWITTER_TOKEN")
access_token_secret = os.environ.get("TWITTER_TOKEN_SECRET")

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

try:
    api.verify_credentials()
    print('Successful Authentication')
except Exception as e:
    print('Failed authentication:', str(e))

me = api.verify_credentials()  # Store user as a variable

data = {
    'screen_name': me.screen_name,
    'followers_count': me.followers_count,
    'listed_count': me.listed_count,
    'statuses_count': me.statuses_count
}

twitter_df = pd.DataFrame(data, index=[0])

# Create the engine object
engine = db.create_engine('sqlite:///twitter_df.db')

# Send DataFrame to SQL table
twitter_df.to_sql('tweet', con=engine, if_exists='replace', index=False)

with engine.connect() as connection:
    query_result = connection.execute(db.text("SELECT * FROM tweet;")).fetchall()
    print(pd.DataFrame(query_result))
