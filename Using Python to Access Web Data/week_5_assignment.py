"""
http://py4e-data.dr-chuck.net/comments_42.xml
http://py4e-data.dr-chuck.net/comments_1508783.xml 
"""


import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
xml = ET.fromstring(html)

counts = xml.findall('.//count')
total = 0

for x in counts:
    nums = x.text
    num_int = int(nums)
    total += num_int

print(total)