import time
import tweepy

# Twitter account keys
key = 'API_KEY'
secret_key = 'API_INSERT_KEY'
secret_token = 'SECRET_TOKEN'
token = 'TOKEN'

auth = tweepy.OAuthHandler(key, secret_key)

auth.set_access_token(token, secret_token)

# API for retweet functionality
api = tweepy.API(auth, wait_on_rate_limit=True)

# retweet functionality with 100 tweets every 600 seconds
for tweet in tweepy.Cursor(api.search_tweets, q = 'The Sims 4',lang='en').items(100):
    try:
        tweet.retweet()
        print("Tweet has been retweeted")
        time.sleep(600)
    except tweepy.TweepyException as e:
        print(e)
    except StopIteration:
        break
