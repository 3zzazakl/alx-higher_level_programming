#!/usr/bin/python3
"""_summary_
"""

import urllib.request as urq


url = "https://alx-intranet.hbtn.io/status"

req = urq.Request(url)

with urq.urlopen(req) as response:
    content = response.read()
    utf8_content = content.decode('utf-8')

print("Body response:")
print("\t- type:", type(content))
print("\t- content:", content)
print("\t- utf8 content:", utf8_content)
