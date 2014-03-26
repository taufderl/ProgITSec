#!/usr/bin/env python3
#
#  Picture.py
#
#  Copyright 2014 Tim auf der Landwehr <dev@taufderl.de>
#
#  This class represents a Picture file
#
from uebung1_4.File import File
from PIL import Image
import math
import os

class Picture(File):
  def __init__(self, filename, filepath):
    File.__init__(self, filename, filepath)

    self.width, self.height = self.dimensions()
    self.entropy = self.entropy()

  def dimensions(self):
    img = Image.open(self.filepath+os.sep+self.filename)
    return img.size

  def entropy(self):
    img = Image.open(self.filepath+os.sep+self.filename)
    histogram = img.histogram()
    histogram_length = sum(histogram)

    samples_probability = [float(h) /
        histogram_length for h in histogram]

    return -sum([p * math.log(p, 2) for p in
        samples_probability if p != 0])