#!/usr/bin/python3
"""_summary_
"""

import urllib.request as urq
import sys


if __name__ == '__main__':
    url = sys.argv[1]

    req = urq.Request(url)
    with urq.urlopen(req) as response:
        id = response.getheader('X-Request-Id')
        print(id)
