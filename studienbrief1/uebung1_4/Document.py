#!/usr/bin/env python3
#
#  Document.py
#
#  Copyright 2014 Tim auf der Landwehr <dev@taufderl.de>
#
#  This class represents a Document file
#
from uebung1_4.File import File

class Document(File):
  def __init__(self, filename, filepath):
    File.__init__(filename, filepath)  
