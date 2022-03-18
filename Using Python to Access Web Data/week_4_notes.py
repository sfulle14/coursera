#
# Retrieving web pages
#
"""
import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

for line in fhand:
    print(line.decode().strip())
 
counts = dict()
for line in fhand:
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
print(counts)

 """


#
# Parsing web pages
#
""" 
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input('Enter - ')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags - http://www.dr-chuck.com/page1.htm  and http://www.dr-chuck.com/page2.htm
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))
 """

#
# Example of BeautifulSoup in action
#

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

# Retrieve all of the anchor tags - http://www.dr-chuck.com/page1.htm  and http://www.dr-chuck.com/page2.htm
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))
