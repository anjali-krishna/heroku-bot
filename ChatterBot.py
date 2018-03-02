# Dependencies
import tweepy
import json
import time

# Twitter API Keys
consumer_key = '8bAqZRDz1AAJIbe8VxKNBHoYe'
consumer_secret = 'HwJwkC6bxWsciPmIvRlxfXylJtklemjWlxdfLk7aONjSgVOImX'
access_token = '258311993-xS77BMv8jxFtGHFSUFCLGN0TXitNZmzrFz1dDars'
access_token_secret = '7IyFNBVcxMcJKGaz1TyzjY8fORIqvt53a4uyYPgVJcwoT'

# Setup Tweepy API Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())


# Create a function that tweets
def TweetOut(tweet_number):
    tweet_text = "Can't stop. Won't stop. Chatting! This is Tweet #{}!".format(tweet_number)
    try:
        api.update_status(tweet_text)
    except Exception as e:
        print(e)
        print("Attempted to tweet: {}".format(tweet_text))


# Create a function that calls the TweetOut function every minute
counter = 0

# Infinitely loop
while(True):

    # Call the TweetQuotes function and specify the tweet number
    TweetOut(counter)

    # Once tweeted, wait 60 seconds before doing anything else
    time.sleep(10)

    # Add 1 to the counter prior to re-running the loop
    counter = counter + 1
