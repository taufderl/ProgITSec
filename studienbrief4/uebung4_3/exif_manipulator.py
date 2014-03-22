#!/usr/bin/env python3
import urllib.request
import argparse
from urllib.parse import urlsplit
from os.path import basename
from bs4 import BeautifulSoup
from PIL import Image
from PIL.ExifTags import TAGS
import os



class ExifManipulator:
  
  def __init__(self):
    pass
  
  def findImages(self, url):
    print('[+] Finding images on ' + url)
    urlContent= urllib.request.urlopen(url).read()
    soup = BeautifulSoup(urlContent)
    imgTags = soup.findAll('img')
    return imgTags
  
  def downloadImage(self, imgTag):
    try:
      print('[+] Dowloading image...')
      imgSrc = imgTag['src']
      imgContent= urllib.request.urlopen(imgSrc).read()
      imgFileName = basename(urlsplit(imgSrc)[2])
      print(imgFileName)
      imgFile = open(imgFileName, 'wb')
      imgFile.write(imgContent)
      imgFile.close()
      return imgFileName
    except Exception as err:
      return 'Error: %s'%err
  
  def showExifData(self, imgFileName):
    try:
      imgFile = Image.open(imgFileName)
      info = imgFile._getexif()
      if info:
        print("[%s] contains the following exif data"%imgFileName)
        for (tag, value) in info.items():
          decoded_tag = TAGS.get(tag, tag)
          print("\t%s:\t%s"%(decoded_tag, value))
    except:
      print('Error while extracting exif data from %s'%imgFileName)
  
  # manipulate a certain exif field
  def modidyExifData(self, imgFileName, key, new_value):
    try:
      imgFile = Image.open(imgFileName)
      info = imgFile._getexif()
      
      # do change
      # TODO
         
    except Exception as err:
      print(err)
      print('Error while extracting exif data from %s'%imgFileName)
    
  # save an image without any exif data
  def removeAllExifData(self, imgFileName, output_file_name):
    imgFile = Image.open(imgFileName)
    imgFile.save(output_file_name) # ignores exif data
      
    
def main():
  parser = argparse.ArgumentParser()
  parser.add_argument('-u', dest='url', type=str,
      help='specify url address', required=True)
  
  em = ExifManipulator()
  args = parser.parse_args()
  imgTags = em.findImages(args.url)
  
  for imgTag in imgTags[0:1]:
    imgFileName = em.downloadImage(imgTag)
    print(imgFileName)
    #em.showExifData(imgFileName)
    #em.modidyExifData(imgFileName, 'date', 'today', imgFileName[:-4]+'_manipulaed_date.jpg')
    #em.removeAllExifData(imgFileName, imgFileName[:-4]+'_without_exif.jpg')
      
if __name__ == '__main__':
    main()