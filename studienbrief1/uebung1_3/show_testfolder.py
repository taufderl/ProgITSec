#!/usr/bin/env python3
#
#  show_testfolder.py
#
#  Copyright 2014 Tim auf der Landwehr <dev@taufderl.de>
#
#  This script prints the contents of a certain folder 
#  recursively in a tree structure
#
import os
import sys
import argparse

# parse testfolder from arguments
parser = argparse.ArgumentParser()
parser.add_argument("testfolder", 
                    help="Please specify the path to [testfolder] without a trailing file seperator")
args = parser.parse_args()
testfolder = args.testfolder

# check if it actually is a folder
if not os.path.isdir(testfolder):
  print("Argument is not a directory")
  sys.exit(1)
  
# check if the folder is called 'testfolder', 
# should be removed if this script is supposed to be used for other folders
if not testfolder.split(os.sep)[-1:][0] == 'testfolder':
  print("Folder is not called 'testfolder'")
  sys.exit(1)

# print files in folder recursively and sorted
for root, dirs, files in sorted(os.walk(testfolder)):
  # calculate depth of current folder
  depth = root.count(os.sep)
  # print folder
  print((depth) * '  ' + os.path.basename(root)+'/')
  # print each file in this folder
  for file in sorted(files):
    print(depth*'  ' + '|--', file)
