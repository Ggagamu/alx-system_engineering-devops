#!/usr/bin/python3
""" API querying module that returns reddit subscribers """
import requests


def number_of_subscribers(subreddit):
    """Queries the API for the total number of a subreddit subscribers """
    subbers = requests.get(f"https://www.reddit.com/r/{subreddit}/about.json",
                        headers={"User-Agent": "My-User-Agent"},
                        allow_redirects=False)
    if subbers.status_code >= 300:
        return 0

    return subbers.json().get("data").get("subscribers")
