import urllib.request
from urllib.parse import urlsplit
from os.path import basename
def downloadImage(imgTag):
    try:
        print('[+] Dowloading image...')
        imgSrc = imgTag['src']
        imgContent= urllib.request.urlopen(imgSrc).read()
        imgFileName = basename(urlsplit(imgSrc)[2])
        imgFile = open(imgFileName, 'wb')
        imgFile.write(imgContent)
        imgFile.close()
        return imgFileName
    except:
        return ''