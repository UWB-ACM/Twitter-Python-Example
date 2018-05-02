# Twitter Python Example (Barebones)

A bot that demonstrates an example of the [Tweepy library][tweepy-lib] for Python.
Currently, this bot is a template that shows how to set up and log in to the
Twitter API with a bot that is connected to a user account. Other than
that, it doesn't do much of anything else.

## Installation

Install the prerequisites using the `requirements.txt` file.

**Linux / Mac**
```bash
python3 -m pip install -r requirements.txt
```

**Windows**
```
py -3 -m pip install -r requirements.txt
```

## Configuration

[This tutorial provides an example of how to make a bot using the Twitter API pages.](https://dototot.com/how-to-write-a-twitter-bot-with-python-and-tweepy/)

The Twitter API uses a few variables to authenticate your bot and allow it
to connect. These are the `access_token`, and the `access_token_secret`.
These variables can be found on the Twitter API dashboard.

This Twitter App will connect to user accounts on their behalf, and ask
if they want to allow permission for the app to connect. These are the
`consumer_key` and `consumer_secret`.

**Do not hard-code these variables, or upload them in any public form.**
One good practice is to store these in a file. This project uses a config `ini`
file, which is specified in the `.gitignore` file, so it doesn't get uploaded.
**If you accidentally leak one of these values**, go to your Twitter API
dashboard and reset your tokens.

To set up your confiugration, make a file called `config.ini`.
Edit the file with the following contents, fill in the blanks with your tokens:

```ini
[Twitter]
consumer_key=
consumer_secret=
access_token=
access_token_secret=
```

No need to wrap the values in quotes. Ensure that there is no whitespace
following `=` characters.

A common alternative to using a configuration file is to use environment
variables, but I don't implement that here.

## Running the Bot

Use the following command if you are running **Linux / Mac**.

```bash
python3 bot.py /path/to/config.ini
```

**Windows**

```
py -3 bot.py C:\path\to\config.ini
```

The first argument must be the path to the `config.ini` file.

The output should be something like this:
```
Using config file located at: /path/to/config.ini
tweepy version XXXX
connected to api as user USERNAME
```

Where `XXXX` is the latest version of the tweepy library, and `USERNAME` is
the username of the consumer login tokens you provided in the `config.ini`.

[tweepy-lib]: http://www.tweepy.org/
