#!/usr/bin/env python3
#
#  skype_messages.py
#
#  Copyright 2014 Tim auf der Landwehr <dev@taufderl.de>
#
#  This script prints all skype messages for a given database
#  that contain the word 'blaupause'
#
import sqlite3
from datetime import datetime

# method to print a skype message
def printMessage(message):
  # convert timestamp to timestamp object
  timestamp = datetime.fromtimestamp(int(message[2]))
  # format 
  time = timestamp.strftime("%H:%M:%S %d.%m.%Y") 
  print("%s %s (%s):"%(time, message[0], message[1]))
  print(message[3])
  print()

# main
def main():
  # connect to database
  conn = sqlite3.connect('../skype/otto.schmidt70/main.db')
  cursor = conn.cursor()
  
  # query messages that contain 'blaupause'
  cursor.execute("SELECT author, from_dispname, timestamp, body_xml FROM messages WHERE body_xml LIKE '%blaupause%';")
  messages = cursor.fetchall()
  
  # print messages
  for message in messages:
    printMessage(message)
  
      
if __name__ == "__main__":
  main()
  