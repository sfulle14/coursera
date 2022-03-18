"""
http://py4e-data.dr-chuck.net/comments_42.html      -- sum=2553
http://py4e-data.dr-chuck.net/comments_1508781.html -- sum ends in 8
"""


import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

tags = soup('span')
nums = []
for tag in tags:
    num = int(tag.contents[0])
    nums.append(num)
print(sum(nums))