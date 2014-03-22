#!/usr/bin/env python3
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
  #cursor.executescript(query) # -> to show an SQL injection executescript() needs to be used
  
  # retrieve list of users
  # if successfully deleted by injection this will throw an exception 
  cursor.execute('SELECT * from users;')
  result = cursor.fetchall()
  print('Registered Users:')
  for i, user in enumerate(result):
    print("\t%i: %s"%(i,user[0]))
  
  
  conn.commit()
  conn.close()

      
if __name__ == "__main__":
  main()
