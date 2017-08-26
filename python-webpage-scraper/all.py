import os
import pycurl
from os import system
from BeautifulSoup import BeautifulSoup

titleAndUrl={}

class ContentCallback:
    def __init__(self):
        self.contents = ''

    def content_callback(self, buf):
        self.contents = self.contents + buf

def parseTitles(html):
    soup = BeautifulSoup(html)
    for link in soup.findAll('a'):
         url = link.get('href')
         title = link.get('title')
         titleAndUrl[title] = url



for i in tuple(open("all","r")):
    parseTitles(i)
    

f = open("output","a");
for key,value in titleAndUrl.items():
    t = ContentCallback()
    curlObj = pycurl.Curl()
    curlObj.setopt(curlObj.URL, value)
    curlObj.setopt(curlObj.WRITEFUNCTION, t.content_callback)
    curlObj.setopt(pycurl.HTTPHEADER, ['User-Agent:Mozilla/5.0 (Windows NT 5.1; rv:33.0) Gecko/20100101 Firefox/33.0'])
    curlObj.perform()
    curlObj.close()

    f.write(t.contents);

f.close()

system("""grep -i "continue reading"  output > urls""")

