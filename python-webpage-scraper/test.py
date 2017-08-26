import sys
import os
import pycurl

URL=""

class ContentCallback:
    def __init__(self):
        self.contents = ''

    def content_callback(self, buf):
        self.contents = self.contents + buf

t = ContentCallback()
curlObj = pycurl.Curl()
curlObj.setopt(curlObj.URL, URL)
curlObj.setopt(curlObj.WRITEFUNCTION, t.content_callback)
curlObj.setopt(pycurl.HTTPHEADER, ['User-Agent:Mozilla/5.0 (Windows NT 5.1; rv:33.0) Gecko/20100101 Firefox/33.0'])
curlObj.perform()
curlObj.close()
#print t.contents

f = open("output","w");
f.write(t.contents);
f.close()

from os import system
system("""grep -i "continue reading"  output > urls""")


from BeautifulSoup import BeautifulSoup

def parse(html):
    soup = BeautifulSoup(html)
    for link in soup.findAll('a'):
         print link.get('href')

lines = tuple(open("urls", 'r'))
for i in lines:
    parse(i)
