#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from übung1_4.File import File
from übung1_4.Document import Document
from übung1_4.Audio import Audio 
from übung1_4.Picture import Picture 
from übung1_4.Video import Video
from übung1_4.Archive import Archive
from übung1_4.Email import Email

import os
import sqlite3

directory = '/home/tadl/Pictures'

pictureextensions = ('.jpg','.png','.raw','.gif','.jpeg','.bmp','.tif')
audioextensions = ('.mp3','.wma','.ogg','.wav','.aac','.m4a','.flac','.aif','.aiff','.aifc','.aifr','.midi','.mid','.rmi','.mp2')
documentextensions = ('.doc','.xls','.ppt','.odt','.ods','.pdf','.docx','.xlsx','.pptx','.odc')
videoextensions = ('.avi','.mov','.mpg','.mp4','.flv','.wmv','.mpg','.mpeg','.mpe','.mpv','.m1v','.m4v','.ifv','.qt')
compressedextensions = ('.zip','.rar','.7z','.ace','.arj','.cab','tar.gz')
emailextensions = ('emails.zip','.eml')

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
  
  #values = {}
  
  #values['filename'] = evidence.filename
  #values['filepath'] = evidence.filepath
  #values['size'] = evidence.size
  #values['checksum'] = evidence.checksum
  
  column_names = 'filename, filepath, size, checksum'
  values = "'%s', '%s', %i, '%s'"% (evidence.filename, evidence.filepath, evidence.size, evidence.checksum)
  
  if type(evidence).__name__ == 'Picture':
    column_names += ', width, height, entropy'
    values += ", %i, %i, %s"% (evidence.width, evidence.height, evidence.entropy)
    #values['width'] = evidence.width
    #values['height'] = evidence.height
    #values['entropy'] = evidence.entropy
    
  elif type(evidence).__name__ == 'Audio':
    column_names += ', artist, album, title'
    values += ", '%s', '%s', '%s'"% (evidence.artist, evidence.album, evidence.title)
    #values['artist'] = evidence.artist
    #values['album'] = evidence.album
    #values['title'] = evidence.title
    
  elif type(evidence).__name__ == 'Document':
    column_names += ', creator'
    values += ", %s"% (evidence.creator)
    #values['creator'] = evidence.creator
    
  elif type(evidence).__name__ == 'Video':
    pass # add nothing
  elif type(evidence).__name__ == 'Archive':
    pass # add nothing
  elif type(evidence).__name__ == 'Email':
    pass # add nothing
  else:
    pass # add nothing
  
  values = values.split(', ')
  values = tuple(values)
  print(values)
  print(type(values))
  print(len(values))
  
  #query = "INSERT INTO files (%s) VALUES (%s);"%(column_names, values)
  query = ("INSERT INTO files ({}) VALUES ("+(', '.join('?'*len(values)))+");").format(column_names)
  print(query)
  print(column_names)
  

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


