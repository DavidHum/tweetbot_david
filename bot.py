"""
 This module is the main function of our bot
 it will post nonsense from diferent text
 using markov-chain
 """

from secrets import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_SECRET
from markov import GAUCHO_MODEL
import tweepy
import re

# create an OAuthHandler instance
# Twitter requires all request to use OAuth for authentication

AUTH = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)

AUTH.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

# Construct the API nstance

API = tweepy.API(AUTH)

#PUBLIC_TWEETS = API.home_timeline()
#for tweet in PUBLIC_TWEETS:
#    print(tweet.text)

#USER = API.get_user('@DavidHumeau')
#for friend in USER.friends():
#    print(friend.screen_name)

MESSAGE = re.sub(r'\d', '', GAUCHO_MODEL.make_short_sentence(140))
API.update_status(status=MESSAGE)
print("Tweeted: {}".format(MESSAGE))
