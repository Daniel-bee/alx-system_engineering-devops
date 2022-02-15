#!/usr/bin/python3
"""Get number of subscribers"""
import requests


def number_of_subscribers(subreddit):
    """
        Return number of subscribers
        If not a valid subreddit, return 0
    """
    res = requests.get('https://reddit.com/r/{}/about.json'.format(subreddit))
    if res:
        return res.json()['data']['subscribers']
    else:
        return 0
