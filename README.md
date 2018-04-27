# Twitter Python Example (Barebones)

A bot that demonstrates an example of the [Tweepy library][tweepy-lib] for Python.

A bot that currently does nothing. Haven't figured out what I want to do yet.
Might be used as an example.

## Installation

Install the prerequisites using the `requirements.txt` file.

```bash
python3 -m pip install -r requirements.txt
```

Add a file called `config.ini`. This will contain the configuration for the
bot.

[Make a new bot using the Twitter API pages.](https://dototot.com/how-to-write-a-twitter-bot-with-python-and-tweepy/)

Edit the file with the following contents, fill in the blanks with your tokens:

```ini
[Twitter]
consumer_key =
consumer_secret =
access_token =
access_token_secret =
```

No need to wrap the values in quotes. Be sure to keep these values private.

If you don't want to use a configuration file, using environment variables
is another option that I don't implement here.

## Execution

Either use the configuration that is provided with the PyCharm project
files, or use the following command:

```bash
python bot.py /path/to/config.ini
```

The first argument must be the path to the `config.ini` file.

[tweepy-lib]: http://www.tweepy.org/