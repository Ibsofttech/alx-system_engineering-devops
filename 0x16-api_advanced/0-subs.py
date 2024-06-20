#!/usr/bin/python3

"""
Program that queries the Reddit API.
"""


import requests


def number_of_subscribers(subreddit):
    """Returns the number of subscribers for a given subreddit."""
    if not isinstance(subreddit, str):
        return 0

    url = f"http://www.reddit.com/r/{subreddit}/about.json"

    headers = {"User-Agent": "Mozilla/5.0 (Linux; Android 10; K) \
              AppleWebKit/537.36 (KHTML, like Gecko) \
              Chrome/117.0.0.0 Safari/537.36"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  #
        data = response.json()
        subscribers = data["data"]["subscribers"]
        return subscribers
    except requests.exceptions.RequestException as e:
        return 0
    except KeyError:
        return 0
