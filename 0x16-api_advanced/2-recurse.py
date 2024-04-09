#!/usr/bin/python3
""" API recursive querying module """
import requests


def recurse(subreddit, hot_list=[], after=None, count=0):
    """Queries the API fcor list containing the titles of all hot articles """
    subbers = requests.get(f"https://www.reddit.com/r/{subreddit}/hot.json",
                        params={"after": after, "count": count},
                        headers={"User-Agent": "My-User-Agent"},
                        allow_redirects=False)
    if subbers.status_code >= 400:
        return None

    htlst = hot_list + [c.get("data").get("title")
                     for c in subbers.json()
                     .get("data")
                     .get("children")]

    info = subbers.json()
    if info.get("data").get("after"):
        return recurse(subreddit, htlst, info.get("data").get("count"),
                       info.get("data").get("after"))
    return htlst
