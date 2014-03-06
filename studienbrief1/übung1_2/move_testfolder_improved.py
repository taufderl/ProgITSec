#!/usr/bin/env python3
import os
import sys
import argparse

# parse testfolder from arguments
parser = argparse.ArgumentParser()
parser.add_argument("testfolder", 
                    help="Please specify the path to [testfolder] without a trailing file seperator")
parser.add_argument('-x', action="store_true", help="actually move the files")
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

# move all the files
for root, dirs, files in os.walk(testfolder):
  for file in files:
    fromFile = root+os.sep+file
    # determine path of this file within 'testfolder'
    newFileName = fromFile.split('testfolder/')[1].replace(os.sep, '_')
    #newFileName = '_'.join(filePath)
    toFile = testfolder+os.sep+newFileName
    # print each movement
    
    if args.x:
      print('Moving [%s] to [%s]...'% (fromFile, toFile))
      os.rename(fromFile, toFile)
    else:
      print('[%s] would be moved to [%s]'% (fromFile, toFile))

if args.x:
  print('Moving files done.')
else:
  print('Moving files simulated.')
