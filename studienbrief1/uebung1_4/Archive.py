#!/usr/bin/env python3
#
#  Archive.py
#
#  Copyright 2014 Tim auf der Landwehr <dev@taufderl.de>
#
#  This class represents an Archive file
#
from uebung1_4.File import File

class Archive(File):
  def __init__(self, filename, filepath):
    super(Archive, self).__init__(self, filename, filepath)  
