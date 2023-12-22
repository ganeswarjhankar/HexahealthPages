import tweepy
import configparser




CONSUMER_KEY = 'MvGIkFkhMVGduBCkpQmkkohWh'
CONSUMER_SECRET = 'KIKE81uc3vEkO07gFEEMNx1acH7vekrPaZx5f2BvqV8fiKg18p'
ACCESS_TOKEN = '1713819606408949760-yyVqWoRpnCcrofk9rcAbfnKEAz3PRu'
ACCESS_TOKEN_SECRET = 't9TFIPXFP3U4L3ZASvhfhl7624o6J4CZDMqkna8f7AWPj'




# Authenticate to Twitter
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

# Create API object
api = tweepy.API(auth)

#public tweets
public_tweets = api.home_timeline()
print(public_tweets)
