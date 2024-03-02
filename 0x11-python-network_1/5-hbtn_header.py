#!/usr/bin/python3
"""_summary_
"""

import requests
import sys


if __name__ == '__main__':
    url = sys.argv[1]

    response = requests.get(url)

    id = response.headers.get('X-Request-Id')
    print(id)
