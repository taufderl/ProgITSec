#!/usr/bin/env python3
#
#  Video.py
#
#  Copyright 2014 Tim auf der Landwehr <dev@taufderl.de>
#
#  This class represents a Video file
#
from uebung1_4.File import File

class Video(File):
  def __init__(self, filename, filepath):
    File.__init__(self, filename, filepath)  
  
