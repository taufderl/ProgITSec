#!/usr/bin/env python3
#
#  list_files_in_db.py
#
#  Copyright 2014 Tim auf der Landwehr <dev@taufderl.de>
#
#  This script collects all files in a certain folder
#  and writes their metadata into an sqlite3 database file.
#
from uebung1_4.File import File
from uebung1_4.Document import Document
from uebung1_4.Audio import Audio 
from uebung1_4.Picture import Picture 
from uebung1_4.Video import Video
from uebung1_4.Archive import Archive
from uebung1_4.Email import Email
import os
import sqlite3

# the directory to be scanned
directory = '/home/tadl'

# the filextensions to be distinguished
pictureextensions = ('.jpg','.png','.raw','.gif','.jpeg','.bmp','.tif')
audioextensions = ('.mp3','.wma','.ogg','.wav','.aac','.m4a','.flac','.aif','.aiff','.aifc','.aifr','.midi','.mid','.rmi','.mp2')
documentextensions = ('.doc','.xls','.ppt','.odt','.ods','.pdf','.docx','.xlsx','.pptx','.odc')
videoextensions = ('.avi','.mov','.mpg','.mp4','.flv','.wmv','.mpg','.mpeg','.mpe','.mpv','.m1v','.m4v','.ifv','.qt')
compressedextensions = ('.zip','.rar','.7z','.ace','.arj','.cab','tar.gz')
emailextensions = ('emails.zip','.eml')

# creates the table for the files in the database
def createTable(cursor):
  query = "CREATE TABLE IF NOT EXISTS files ("+ \
                  "filename text, "+ \
                  "filepath text, "+ \
                  "size integer, "+ \
                  "checksum text, "+ \
                  "width integer, "+ \
                  "height integer, "+ \
                  "entropy real, "+ \
                  "artist text, "+ \
                  "album text, "+ \
                  "title text, "+ \
                  "creator text"+ \
                  ");"
  cursor.execute(query)
  
def insertFileInfos(cursor, evidence):
  # add general file information
  column_names = 'filename, filepath, size, checksum'
  values = "'%s', '%s', %i, '%s'"% (evidence.filename, evidence.filepath, evidence.size, evidence.checksum)
  
  if type(evidence).__name__ == 'Picture':
    # add picture specific file information
    column_names += ', width, height, entropy'
    values += ", %i, %i, %s"% (evidence.width, evidence.height, evidence.entropy)
    
  elif type(evidence).__name__ == 'Audio':
    # add audio specific file information
    column_names += ', artist, album, title'
    values += ", '%s', '%s', '%s'"% (evidence.artist, evidence.album, evidence.title)
    
  elif type(evidence).__name__ == 'Document':
    # add document specific file information
    column_names += ', creator'
    values += ", %s"% (evidence.creator)
    
  elif type(evidence).__name__ == 'Video':
    pass # add nothing
  elif type(evidence).__name__ == 'Archive':
    pass # add nothing
  elif type(evidence).__name__ == 'Email':
    pass # add nothing
  else:
    pass # add nothing
  
  # prepare values to be added to the database query
  values = values.split(', ')
  values = tuple(values)
  # generate query
  query = ("INSERT INTO files ({}) VALUES ("+(', '.join('?'*len(values)))+");").format(column_names)
  # execute query to insert file data
  cursor.execute(query, values)

def main():
  conn = sqlite3.connect('files.db')
  cursor = conn.cursor()
  createTable(cursor)

  for root, dirs, files in os.walk(directory):
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
      
      insertFileInfos(cursor, evidence)
      conn.commit()
      
  # close database connection
  conn.close()
      
if __name__ == "__main__":
  main()


