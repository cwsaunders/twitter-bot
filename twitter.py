import tweepy
import time

# Tweepy documentation: http://docs.tweepy.org/en/latest/

# Add in your Twitter developer keys in the four strings listed 'key'

auth = tweepy.OAuthHandler('key','key')
auth.set_access_token('key','key')

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

user=api.me()

search = 'Python'
numberoftweets = 500

for tweet in tweepy.Cursor(api.search, search).items(numberoftweets):
    try:
        print('Tweet Liked')
        tweet.favorite()
        # For retweet use:
        # tweet.retweet()
        time.sleep(10)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
