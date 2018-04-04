import configparser, sys
import tweepy

# load the configuration from the config file
# another common way to do this is using environment variables
config = configparser.ConfigParser()

print('Using config file located at: ', sys.argv[1])

# read the file specified as first arg
with open(sys.argv[1], 'r') as f:
    config.read_file(f)

# load the key and secrets from the config file
# be careful with these, they grant anyone access to your account
consumer_key = config['Twitter']['consumer_key']
consumer_secret = config['Twitter']['consumer_secret']

access_token = config['Twitter']['access_token']
access_token_secret = config['Twitter']['access_token_secret']

# logs in using the user authorized
# using demo from http://tweepy.readthedocs.io/en/v3.6.0/getting_started.html
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# get the api w/ the auth specified
api = tweepy.API(auth)

# print some debug stuff
print('tweepy version ' + tweepy.__version__)
logged_in_user = api.me()
print('connected to api as user', logged_in_user.name)

