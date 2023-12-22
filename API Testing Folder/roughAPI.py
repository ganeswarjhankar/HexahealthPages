import tweepy
import configparser



#read alll teh file from config file

config = configparser.ConfigParser()
config.read('config.ini')

CONSUMER_KEY = config['twitter']['CONSUMER_KEY']
CONSUMER_SECRET =  config['twitter']['CONSUMER_SECRET']
ACCESS_TOKEN = config['twitter']['ACCESS_TOKEN']
ACCESS_TOKEN_SECRET = config['twitter']['ACCESS_TOKEN_SECRET']



auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

try:
    api = tweepy.API(auth)
    public_tweets = api.home_timeline()

    for tweet in public_tweets:
        print(tweet.text)

except tweepy.TweepError as e:
    print(f"Error: {e}")