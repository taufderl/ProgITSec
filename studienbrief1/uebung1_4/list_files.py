#!/usr/bin/env python3
#
#  list_files.py
#
#  Copyright 2014 Tim auf der Landwehr <dev@taufderl.de>
#
#  This script collects all files in a certain folder
#  and writes their metadata into an csv output file.
#
from uebung1_4.File import File
from uebung1_4.Document import Document
from uebung1_4.Audio import Audio 
from uebung1_4.Picture import Picture 
from uebung1_4.Video import Video
from uebung1_4.Archive import Archive
from uebung1_4.Email import Email
import os

# the directory to be scanned
directory = '/home/tadl'

# the filextensions to be distinguished
pictureextensions = ('.jpg','.png','.raw','.gif','.jpeg','.bmp','.tif')
audioextensions = ('.mp3','.wma','.ogg','.wav','.aac','.m4a','.flac','.aif','.aiff','.aifc','.aifr','.midi','.mid','.rmi','.mp2')
documentextensions = ('.doc','.xls','.ppt','.odt','.ods','.pdf','.docx','.xlsx','.pptx','.odc')
videoextensions = ('.avi','.mov','.mpg','.mp4','.flv','.wmv','.mpg','.mpeg','.mpe','.mpv','.m1v','.m4v','.ifv','.qt')
compressedextensions = ('.zip','.rar','.7z','.ace','.arj','.cab','tar.gz')
emailextensions = ('emails.zip','.eml')

# writes the header line to the output file
def writeHeader():
  with open("dateien.csv", "w") as f:
    f.write("filename;filepath;size;checksum;width;height;entropy;artist;album;title;creator\n")

# writes the line for the given file to the output file
def writeFileInfos(evidence):
  csvstring = evidence.filename+';'+evidence.filepath+';'+str(evidence.size)+';'+evidence.checksum+';'

  if type(evidence).__name__ == 'Picture':
    csvstring += str(evidence.width)+';'+str(evidence.height)+';'+str(evidence.entropy)+';\n'
  elif type(evidence).__name__ == 'Audio':
    csvstring += ';;;'+evidence.artist+';'+evidence.album+';'+evidence.title+';\n'
  elif type(evidence).__name__ == 'Document':
    csvstring += ';;;;;'+evidence.creator+';\n'
  elif type(evidence).__name__ == 'Video':
    csvstring += '\n'
  elif type(evidence).__name__ == 'Archive':
    csvstring += '\n'
  elif type(evidence).__name__ == 'Email':
    csvstring += '\n'
  else:
    csvstring += '\n'

  with open("dateien.csv", "a") as f:
    f.write(csvstring)

# main
def main():
  # write the header line
  writeHeader()

  # scan the given directory
  for root, dirs, files in os.walk(directory):
    # for each file found create a file object
    # based on the given file extension
    for file in files:
      print(">> %s"% root+os.sep+file)
      if os.path.isdir(root+os.sep+file):
        pass
      elif file.lower().endswith(pictureextensions):
        evidence = Picture(file, root)
      elif file.lower().endswith(audioextensions):
        evidence = Audio(file, root)
      elif file.lower().endswith(documentextensions):
        evidence = Document(file, root)
      elif file.lower().endswith(videoextensions):
        evidence = Video(file, root)
      elif file.lower().endswith(compressedextensions):
        evidence = Archive(file, root)
      elif file.lower().endswith(emailextensions):
        evidence = Email(file, root)
      else:
        evidence = File(file, root)
      
      # write infos for the file in the output file
      writeFileInfos(evidence)
      
if __name__ == "__main__":
  main()