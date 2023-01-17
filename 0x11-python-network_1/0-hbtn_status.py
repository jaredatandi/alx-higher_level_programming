#!/usr/bin/python3
""" A module to fetch the status of a server
"""
import urllib.request


def fetcher():
    """ Fetches the status of a server"""
    with urllib.request.urlopen("https://alx-intranet.hbtn.io/status") as r:
        data = r.read()
        print("Body response:")
        print("\t- type: ", type(data))
        print("\t- content: ", (data))
        print("\t- utf8: ", data.decode("utf-8"))


if __name__ == "__main__":
    fetcher()
