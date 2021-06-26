import tweepy
import time

consumer_key = '*****************'
consumer_secret = '*****************'
access_token = '*****************'
access_token_secret = '*****************'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
user = api.me()

def limit_handler(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(1000)
    except StopIteration:
        return

search = 'python'
numberOfTweets = 2
for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
    try:
        tweet.destroy_favorite()
        print('I liked that tweet')
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break








# Generous bot
# for follower in limit_handler(tweepy.Cursor(api.followers).items()):
#     print(follower.name)

