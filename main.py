import tweepy
import os
import schedule
import time

# Load keys from environment
BEARER_TOKEN = os.getenv("BEARER_TOKEN")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_SECRET = os.getenv("ACCESS_SECRET")
API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")

# Authenticate
auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

def post_tweet():
    tweet = "🚀 Stock/Crypto Update: #BTC +2.5% | #ETH +1.8% | $AAPL +1.2% 📈"
    api.update_status(tweet)
    print("Tweet posted:", tweet)

# Schedule a tweet every 3 hours
schedule.every(3).hours.do(post_tweet)

if __name__ == "__main__":
    while True:
        schedule.run_pending()
        time.sleep(60)