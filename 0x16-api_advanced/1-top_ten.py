#!/usr/bin/python3
""" API querying module that returns the top ten hottest reddits """
import requests


def top_ten(subreddit):
    """Queries the API for titles of the first 10 hot reddit posts """
    subbers = requests.get(f"https://www.reddit.com/r/{subreddit} \
                        /hot.json?limit=10",
                        headers={"User-Agent": "My-User-Agent"},
                        allow_redirects=False)
    if subbers.status_code >= 300:
        print('None')
    else:
        [print(c.get("data").get("title"))
         for c in subbers.json().get("data").get("children")]
