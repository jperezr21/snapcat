import os

import tweepy

consumer_key = os.environ['TWEEPY_CUSTOMER_KEY']
consumer_secret = os.environ['TWEEPY_CUSTOMER_SECTRET']
access_token = os.environ['TWEEPY_ACCESS_TOKEN']
access_token_secret = os.environ['TWEEPY_ACCESS_TOKEN_SECRET']


def upload_image(path):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    api.update_with_media(path, status="Eh gato!")
