#!/usr/bin/python3
"""_summary_
"""

import requests
import sys


if __name__ == '__main__':
    url = sys.argv[1]
    email = sys.argv[2]

    mail = {'email': email}
    response = requests.post(url, mail)

    print(response.text)
