try:
    import urllib.request as urllib2
except ImportError:
    import urllib2
from bs4 import BeautifulSoup

page = 'http://youtube.com'
opened = urllib2.urlopen(page)
soup = BeautifulSoup(opened)

for link in soup.find_all('a'):
    print (link.get('href'))
