import urllib
import os
from os import path
from os.path import basename
import urllib

count=0
for i in tuple(open('main.2','r')):
    if i[0] != '#':
        n=i.strip()
        name=basename(n)
        urllib.URLopener.version = 'User-Agent:Mozilla/5.0 (Windows NT 5.1; rv:33.0) Gecko/20100101 Firefox/33.0'
        urllib.urlretrieve(n, name)
        count += 1
        if count%50 == 0:
             print("Downloaded %d images" % count)
