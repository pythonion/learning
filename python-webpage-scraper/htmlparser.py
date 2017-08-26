from BeautifulSoup import BeautifulSoup

def parse(html):
    soup = BeautifulSoup(html)
    for link in soup.findAll('a'):
         print link.get('href')

