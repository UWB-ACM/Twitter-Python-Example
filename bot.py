"""
Twitter Python Example

Barebones example of using the Tweepy library for Python
Logs into the service as a specific user, and gets their username.

More examples can be found on the official documentation:
http://docs.tweepy.org/en/v3.6.0/getting_started.html

Usage:

python3 bot.py /path/to/config.ini
"""

# use the configparser util for ez config files
import configparser, sys
# tweepy library, install this using the requirements.txt file
import tweepy

if __name__ == '__main__':

    # check the number of args
    config_file_path = ''

    if len(sys.argv) > 1:
        config_file_path = sys.argv[1]
    else:
        print('Usage: %s config.ini' % (sys.argv[0],))
        sys.exit()

    # load the configuration from the config file
    # another common way to do this is using environment variables
    config = configparser.ConfigParser()

    # print for debugging
    print('Using config file located at: ', sys.argv[1])

    # read the config file and use it for the config parser
    with open(config_file_path, 'r') as f:
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
    # logged into the service, get the username
    # after now, should be able to mess with the api
    logged_in_user = api.me()
    print('connected to api as user', logged_in_user.name)
