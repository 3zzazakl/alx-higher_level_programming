#!/usr/bin/python3
"""_summary_
"""

import urllib.request as urq
import urllib.parse as prs
import sys


if __name__ == '__main__':
    url = sys.argv[1]
    email = sys.argv[2]

    data = prs.urlencode({'email': email}).encode('utf-8')
    req = urq.Request(url, data)

    with urq.urlopen(req) as response:
        content = response.read().decode('utf-8')

    print(content)
