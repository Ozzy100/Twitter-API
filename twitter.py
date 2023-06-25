import os
import tweepy
from dotenv import load_dotenv

consumer_key = os.environ["TWITTER_API_KEY"]
consumer_secret = os.environ["TWITTER_API_KEY_SECRET"]
access_token = os.environ["TWITTER_TOKEN"]
access_token_secret = os.environ["TWITTER_TOKEN_SECRET"]

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
 
api = tweepy.API(auth)
 
try:
    api.verify_credentials()
    print('Successful Authentication')
except:
    print('Failed authentication')

me = api.verify_credentials() # Store user as a variable
 
data = me.json()

print(data)


# Get user Twitter statistics
print(f"my.followers_count: {me.followers_count}")
print(f"my.listed_count: {me.listed_count}")
print(f"my.statuses_count: {me.statuses_count}")




print(me.followers_count)

