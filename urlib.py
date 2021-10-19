import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import numpy as np
import matplotlib
import pytorch

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('span class="comments"')
for tag in tags:
    print(tag)
    
