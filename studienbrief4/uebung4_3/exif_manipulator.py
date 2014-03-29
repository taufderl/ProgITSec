#!/usr/bin/env python
# python 2.x file due to pyexiv2 dependency
#
#  pdf_search.py
#
#  Copyright 2014 Tim auf der Landwehr <dev@taufderl.de>
#
#  This script provides a search in the text on a pdf file.
#
import urllib2 #python2.x
from urlparse import urlsplit #python2.x
from BeautifulSoup import BeautifulSoup #python2.x
import pyexiv2 # python 2.x

import argparse
from os.path import basename
from PIL import Image
from PIL.ExifTags import TAGS
import os
import datetime

# exif manipulator class
class ExifManipulator:
  
  # init
  def __init__(self):
    pass
  
  # find image tags on a given url
  def findImages(self, url):
    print('[+] Finding images on ' + url)
    urlContent= urllib2.urlopen(url).read()
    soup = BeautifulSoup(urlContent)
    imgTags = soup.findAll('img')
    return imgTags

  # download an image from a given html image tag 
  def downloadImage(self, imgTag):
    try:
      print('[+] Dowloading image...')
      imgSrc = imgTag['src']
      imgContent= urllib2.urlopen(imgSrc).read()
      imgFileName = basename(urlsplit(imgSrc)[2])
      imgFile = open(imgFileName, 'wb')
      imgFile.write(imgContent)
      imgFile.close()
      print('Downloaded %s'%imgFileName)
      return imgFileName
    except Exception as err:
      print('Error: %s'%err)
  
  # print exif data to stdout
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
  def setExifTime(self, imgFileName, new_time):
    try:
      metadata = pyexiv2.ImageMetadata(imgFileName)
      metadata.read()
      
      # find  date tags
      date_tag1 = metadata['Exif.Image.DateTime']
      date_tag2 = metadata['Exif.Photo.DateTimeOriginal']
      date_tag3 = metadata['Exif.Photo.DateTimeDigitized']
      
      # modify data to current time
      date_tag1.value = new_time
      date_tag2.value = new_time
      date_tag3.value = new_time

      # write metadata to file
      metadata.write()
      metadata.read()
      date_tag = metadata['Exif.Image.DateTime']
      print("Saved value: %s"%date_tag.value)
         
    except Exception as err:
      print(err)
      print('Error while extracting exif data from %s'%imgFileName)
    
  # save an image without any exif data
  def removeAllExifData(self, imgFileName, output_file_name):
    try:
      imgFile = Image.open(imgFileName)
      imgFile.save(output_file_name) # ignores exif data
    except Exception as err:
      print("Some error occured: %s"%err)
      
      
# main    
def main():
  parser = argparse.ArgumentParser()
  parser.add_argument('-u', dest='url', type=str,
      help='specify url address', required=True)
  
  # create instance of manipulator
  em = ExifManipulator()
  args = parser.parse_args()
  imgTags = em.findImages(args.url)
  
  # for all found images
  for imgTag in imgTags:
    # download image to file
    imgFileName = em.downloadImage(imgTag)

    # show exif data
    #em.showExifData(imgFileName)
    
    # set the exif date to the current time
    current_time = datetime.datetime.today()
    em.setExifTime(imgFileName, current_time)
    
    # store a copy of the image without any exif data
    #em.removeAllExifData(imgFileName, imgFileName[:-4]+'_without_exif.jpg')
      
if __name__ == '__main__':
    main()