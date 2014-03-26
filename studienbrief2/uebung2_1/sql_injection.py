#!/usr/bin/env python3
#
#  sql_injection.py
#
#  Copyright 2014 Tim auf der Landwehr <dev@taufderl.de>
#
#  This file was supposed to show an example of an sql injection
#  in python. But cursor.execute(QUERY) only executes one query,
#  to protect from this issue. Therefore an sql injection cannot
#  be shown.
#
import sqlite3
import sys

def main():
  # connect to database
  conn = sqlite3.connect('database.db')
  cursor = conn.cursor()
  
  # prepare user table
  cursor.execute('CREATE TABLE IF NOT EXISTS users (name text);')
  
  # request user input
  # To attempt an SQL injection insert -> bla'); DROP TABLE users;-
  #name = input('User name: ') # -> input() does not allow semicolon
  name = ''
  while len(name) == 0:
    print('User name: ') 
    name = sys.stdin.readline().strip()
  
  # pass user input to database query
  # this is the insecure line
  query = "INSERT INTO users (name) VALUES ('%s');"% name
  print(query)
  cursor.execute(query)        # -> actually execute() only allows a single query
  #cursor.executescript(query) # -> to show an SQL injection executescript() would be required
  
  # retrieve list of users
  # if successfully deleted by injection this will throw an exception 
  cursor.execute('SELECT * from users;')
  result = cursor.fetchall()
  print('Registered Users:')
  for i, user in enumerate(result):
    print("\t%i: %s"%(i,user[0]))
  
  # commit and close connection
  conn.commit()
  conn.close()

      
if __name__ == "__main__":
  main()
