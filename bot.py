import configparser, os
import tweepy

# load the configuration from the config file
# another common way to do this is using environment variables
config = configparser.ConfigParser()
# read the file in the same directory
config.read_file('config.ini')

# load the key and secrets from the config file
# be careful with these, they grant anyone access to your account
consumer_key = config['Twitter']['consumer_key']
consumer_secret = config['Twitter']['consumer_secret']


auth = tweepy.OAuthHandler()