import urllib.request
from bs4 import BeautifulSoup
def findImages(url):
    print('[+] Finding images on ' + url)
    urlContent = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(urlContent)
    imgTags = soup.findAll('img')
    return imgTags