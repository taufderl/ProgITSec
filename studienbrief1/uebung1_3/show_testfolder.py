#!/usr/bin/env python3
import os
import sys
import argparse

# parse testfolder from arguments
parser = argparse.ArgumentParser()
parser.add_argument("testfolder", 
                    help="Please specify the path to [testfolder] without a trailing file seperator")
args = parser.parse_args()
testfolder = args.testfolder

# check if is folder
if not os.path.isdir(testfolder):
  print("Argument is not a directory")
  sys.exit(1)
  
# check if is called 'testfolder'
if not testfolder.split(os.sep)[-1:][0] == 'testfolder':
  print("Folder is not called 'testfolder'")
  sys.exit(1)


for root, dirs, files in sorted(os.walk(testfolder)):
  depth = root.count(os.sep)
  print((depth) * '  ' + os.path.basename(root)+'/')       
  for file in sorted(files):
    print(depth*'  ' + '|--', file)
