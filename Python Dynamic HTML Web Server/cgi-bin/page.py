#!/usr/bin/python3
import random
import datetime

print('content-type:text/html\n')
print('<!DOCTYPE html>')

print('<link rel="stylesheet" type="text/css" href="../coursera_classes/Python Dynamic HTML Web Server/style.css">')

print('div class="content"')
print('<h1> These are your random numbers at this date and time '+
      str(datetime.datetime.now()) + '</h1>')

for i in range(10):
    print('<p> Random #' + str(i+1) + ': ' + str(random.randrange(0,1000)) + '</p>')

print('<p> <a href="/"> Home Page</a></p>')
print('</div>')