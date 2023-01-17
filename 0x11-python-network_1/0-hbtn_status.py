#!/usr/bin/python3
""" A module to fetch the status of a server
"""
import urllib.request


def fetcher():
    """ Fetches the status of a server"""
    with urllib.request.urlopen("https://intranet.hbtn.io/status") as r:
        html = r.read()
        print("Body response:")
        print("\t- type: {}".format(type(html)))
        print("\t- content: {}".format(html))
        print("\t- utf8: {}".format(html.decode("utf-8")))

if __name__ == "__main__":
    fetcher()
