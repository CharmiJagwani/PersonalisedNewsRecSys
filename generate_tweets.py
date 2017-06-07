import tweepy
import json
import sys
from tweepy import OAuthHandler
from tweepy import Cursor
from tweepy.parsers import JSONParser


consumer_key = 'ReHPeb66aev3y6Q1dmjrvVyfo'
consumer_secret = 'U30CEWoqJp23Wtcy4puOOxOEsiWKhxb7yzclP838loGnwY5q15'
access_token = '391435560-Xe6wHCADJu6YUOBAauIdnoMS7qyBcdRgw1fGxjy5'
access_secret ='wfEp0Bl4WgLYZ38RvtpDaU8Fh8GD4FT6C68Ky1Rsike4p'



auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)
def usage():
    print("Usage:")
    print("python {} <username>".format(sys.argv[0]))

if __name__ == '__main__':
    if len(sys.argv) != 2:
        usage()
        sys.exit(1)
    user = sys.argv[1]

    fname = "twitter_tweets.json".format(user)
    with open(fname, 'w') as f:
        for page in Cursor(api.user_timeline, screen_name=user, count=50).pages(3):
            for status in page:
                f.write(json.dumps(status._json)+"\n")
