#!/usr/bin/python3
"""Summary
"""

import requests
import sys

if __name__ == '__main__':
    """main
    """
    if len(sys.argv) < 2:
        q = ""
    else:
        q = sys.argv[1]

    url = "http://0.0.0.0:5000/search_user"
    load = {'q': q}
    response = requests.post(url, load)

    try:
        json_res = response.json()
        if json_res:
            print(f"[{json_res['id']}] {json_res['name']}")
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
