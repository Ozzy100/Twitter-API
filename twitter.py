import requests
import os
from pytwitter import Api
import base64

BEARER_TOKEN = os.environ.get('TWITTER_BEARER_TOKEN')
API_KEY = os.environ.get('TWITTER_API_KEY')
API_KEY_SECRET = os.environ.get('TWITTER_API_KEY_SECRET')
ACCESS_TOKEN = os.environ.get('TWITTER_TOKEN')
ACCESS_SECRET = os.environ.get('TWITTER_TOKEN_SECRET')

CLIENT_ID = os.environ.get('CLIENT_ID')
CLIENT_SECRET = os.environ.get('CLIENT_SECRET')

#api = Api(bearer_token=BEARER_TOKEN)

# api = Api(
#   consumer_key=API_KEY,
#   consumer_secret=API_KEY_SECRET,
#   access_token=ACCESS_TOKEN,
#   access_secret=ACCESS_SECRET
# )

base_url = 'https://api.twitter.com/'
auth_url = 'https://api.twitter.com/oauth2/token'









#response = requests.get(AUTH_URL, data=payload, )
# print(response.json())




# if response.status_code == 200:
#     # Request was successful
#     print('POST request successful!')
#     print(response.json())
# else:
#     # Request failed
#     print('POST request failed. Status code:', response.status_code)


#https://developer.twitter.com/en/portal/projects/1672815275652022272/apps/27370138/settings
