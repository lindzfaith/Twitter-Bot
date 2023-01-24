import os
import tweepy
import json
import time


def lambda_handler(event, context):
    consumer_key = os.getenv("key")
    consumer_secret = os.getenv("secret_key")
    access_token = os.getenv("token")
    access_token_secret = os.getenv("secret_token")

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    for tweet in tweepy.Cursor(api.search, q = 'Sims 4', lang='en').items(2):
      try:
         tweet.retweet()
      except tweepy.TweepyException as e:
         print(e)
      except StopIteration:
          break
    return {"statusCode": 200}
