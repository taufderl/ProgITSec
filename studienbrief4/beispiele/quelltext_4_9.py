#I. A. a. Violent Python
import urllib.request
import argparse
from urllib.parse import urlsplit
from os.path import basename
import urllib.request
from bs4 import BeautifulSoup
from PIL import Image
from PIL.ExifTags import TAGS
def findImages(url):
    print('[+] Finding images on ' + url)
    urlContent= urllib.request.urlopen(url).read()
    soup = BeautifulSoup(urlContent)
    imgTags = soup.findAll('img')
    return imgTags
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
def testForExif(imgFileName):
    try:
        exifData = {}
        imgFile = Image.open(imgFileName)
        info = imgFile._getexif()
        if info:
            for (tag, value) in info.items():
                decoded = TAGS.get(tag, tag)
                exifData[decoded] = value
            exifGPS = exifData['GPSInfo']
            if exifGPS:
                print('[*] ' + imgFileName + \
                    ' contains GPS MetaData')
    except:
        pass
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', dest='url', type=str,
        help='specify url address', required=True)
    args = parser.parse_args()
    imgTags = findImages(args.url)
    for imgTag in imgTags:
        imgFileName = downloadImage(imgTag)
        testForExif(imgFileName)
if __name__ == '__main__':
    main()