from twython import Twython
import sys
sys.path.insert(0, sys.path[0]+'//Sensitive')
from credentials import *

_DEBUG = True
_SEND_TWEET = False

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
twitter.verify_credentials()
TweetMessage = 'Hello World!'

if _SEND_TWEET:
    twitter.update_status(status=TweetMessage)
