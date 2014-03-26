#!/usr/bin/env python3
#
#  Email.py
#
#  Copyright 2014 Tim auf der Landwehr <dev@taufderl.de>
#
#  This class represents an Email file
#
from uebung1_4.File import File

class Email(File):
  def __init__(self, filename, filepath):
    File.__init__(self, filename, filepath)  

