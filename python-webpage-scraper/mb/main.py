from BeautifulSoup import BeautifulSoup

f = open("main.1","w")
def parse(html):
    soup = BeautifulSoup(html)
    for link in soup.findAll('img'):
          f.write(link.get('src').encode('utf-8')+"\n")

lines = tuple(open("main_jpgs", 'r'))
for i in lines:
    parse(i)

