#!/usr/bin/env python3
#
#  move_testfolder.py
#
#  Copyright 2014 Tim auf der Landwehr <dev@taufderl.de>
#
#  This script moves all files in subfolders of a certain
#  root directory to this root directory.
#
import os
import sys
import argparse

# parse testfolder name from arguments
parser = argparse.ArgumentParser()
parser.add_argument("testfolder", 
                    help="Please specify the path to [testfolder] without a trailing file seperator")
parser.add_argument('-x', action="store_true", help="actually move the files")
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

# move all the files from subfolders to the root folder
for root, dirs, files in os.walk(testfolder):
  for file in files:
    # determine source and target path's
    fromFile = root+os.sep+file
    toFile = testfolder+os.sep+file

    # only move if parameter -x is set
    if args.x:
      print('Moving [%s] to [%s]...'% (fromFile, toFile))
      os.rename(fromFile, toFile)
    # otherwise just simulate
    else:
      print('[%s] would be moved to [%s]'% (fromFile, toFile))

# print result
if args.x:
  print('Moving files done.')
else:
  print('Moving files simulated.')