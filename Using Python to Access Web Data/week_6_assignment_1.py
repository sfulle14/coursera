"""
http://py4e-data.dr-chuck.net/comments_42.json
http://py4e-data.dr-chuck.net/comments_1508784.json
"""

import urllib.request, urllib.parse, urllib.error
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter url: ')
uh = urllib.request.urlopen(url)
data = uh.read().decode()

js = json.loads(data)
num = 0

for x in range (len(js['comments'])):
    num += int(js['comments'][x]['count'])

print(num)