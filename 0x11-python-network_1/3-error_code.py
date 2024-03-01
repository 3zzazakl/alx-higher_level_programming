#!/usr/bin/python3
"""_summary_
"""

import urllib.request as urq
import urllib.error as err
import sys


if __name__ == '__main__':
    url = sys.argv[1]

    try:
        with urq.urlopen(url) as response:
            body = response.read().decode('utf-8')
            print(body)

    except err.HTTPError as e:
        print(f"Error code: {e.code}")
