#!/usr/bin/env python3
#
#  File.py
#
#  Copyright 2014 Tim auf der Landwehr <dev@taufderl.de>
#
#  This class represents a File in general
#
import os
import hashlib
import shutil

class File(object):
  def __init__(self, filename, filepath):
    self.filename = filename
    self.filepath = filepath
    self.checksum = self.calcchecksum()
    self.size = self.calcsize()

  def calcchecksum(self):
    sha1 = hashlib.sha1()
    with open(self.filepath + os.sep + self.filename, 'rb') as f:
      for chunk in iter(lambda: f.read(128 * sha1.block_size), b''): 
        sha1.update(chunk)
    return sha1.hexdigest()

  def calcsize(self):
    return os.path.getsize(self.filepath + os.sep + self.filename)

  def move(self, destination):
    os.rename(self.filepath + os.sep + self.filename,
              destination + os.sep + self.filename)
    self.filepath = destination

  def remove(self):
    os.remove(self.filepath + os.sep + self.filename)
    self.filename = None
    self.filepath = None

  def rename(self, filename):
    os.rename(self.filepath + os.sep + self.filename,
              self.filepath + os.sep + filename)
    self.filename = filename

  def copy(self, destination):
    shutil.copyfile(self.filepath + os.sep + self.filename,
                    destination + os.sep + self.filename)
