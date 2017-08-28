import sys
import os
import pycurl

class ContentCallback:
    def __init__(self):
        self.contents = ''

    def content_callback(self, buf):
        self.contents = self.contents + buf

class curly:
    def __init__(self, url):
        self.t = ContentCallback()
        self.curlObj = pycurl.Curl()
        self.curlObj.setopt(self.curlObj.URL, url)
        self.curlObj.setopt(self.curlObj.WRITEFUNCTION, self.t.content_callback)
        self.curlObj.setopt(pycurl.HTTPHEADER, ['User-Agent:Mozilla/5.0 (Windows NT 5.1; rv:33.0) Gecko/20100101 Firefox/33.0'])

    def getData(self):
        self.curlObj.perform()
        self.curlObj.close()
        return self.t.contents

