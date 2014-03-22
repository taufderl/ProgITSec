#!/usr/bin/env python3
import sqlite3
import zipfile
import os
import re
from symbol import except_clause

###############################################################################
##########################  predefined methods  ###############################
###############################################################################
def printForm(formDB):
  try:
    conn = sqlite3.connect(formDB)
    print(formDB)
    c = conn.cursor()
    try:
      query = "SELECT value, timesUsed, datetime( \
        firstUsed/1000000,'unixepoch'), datetime( \
        firstUsed/1000000,'unixepoch') FROM moz_formhistory;"
        
      c.execute(query)
      print('\n--- Formulardaten --- ')
      for row in c:
        print('Eingabe: ' + str(row[0]) + ' Anzahl: '\
          + str(row[1]) + ' erste Nutzung: ' +\
          str(row[2]) + ' letzte Nutzung: ' +\
          str(row[3]))
    except:
      print('Could not execute query:')
      print('\t%s'%query)
  except:
      print('Could not open DB %s'%formDB)

def printCookies(cookiesDB):
  try:
    conn = sqlite3.connect(cookiesDB)
    c = conn.cursor()
    query = 'SELECT host, name, value FROM moz_cookies;';
    c.execute(query)
    print('\n[*] -- Gefundene Cookies --')
    for row in c:
      host = str(row[0])
      name = str(row[1])
      value = str(row[2])
      print('[+] Host: ' + host + ', Cookie: ' + \
      name + ', Wert: ' + value)
  except Exception as e:
    if 'encrypted' in str(e):
      print('\n[*] Fehler beim Lesen der DB')
            
def printHistory(placesDB):
  try:
    conn = sqlite3.connect(placesDB)
    c = conn.cursor()
    query = "select url, datetime(visit_date/ \
      1000000, 'unixepoch') from moz_places,  \
      moz_historyvisits where visit_count >   \
      0 and moz_places.id==moz_historyvisits. \
      place_id;"
    c.execute(query)
    print('\n[*] -- Browser History --')
    for row in c:
      url = str(row[0])
      date = str(row[1])
      print('[+] ' + date + ' - Visited: ' + url)
  except Exception as e:
    if 'encrypted' in str(e):
      print('\n[*] Fehler beim Lesen der DB')
        
def printGoogle(placesDB):
  conn = sqlite3.connect(placesDB)
  c = conn.cursor()
  query = "select url, datetime(visit_date/1000000, \
       'unixepoch') from moz_places, moz_historyvisits \
        where visit_count > 0 and moz_places.id==\
        moz_historyvisits.place_id;"
  c.execute(query)
  print('\n--- Google gefunden ---')
  for row in c:
    url = str(row[0])
    date = str(row[1])
    if 'google' in url.lower():
      r = re.findall(r'q=.*\&', url)
      if r:
        search=r[0].split('&')[0]
        search=search.replace('q=', '').\
            replace('+', ' ')
        print(date+' - Suchanfrage: ' + search)
                
###############################################################################
#########################  passsword extraction  ##############################
###############################################################################

def printPasswords(passwordDB):
  try:
    conn = sqlite3.connect(passwordDB)
    c = conn.cursor()
    try:
      query = "SELECT hostname, encryptedUsername, encryptedPassword, \
        datetime(timeCreated/1000000, 'unixepoch'), \
        datetime(timeLastUsed/1000000, 'unixepoch'), \
        timesUsed \
        FROM moz_logins;";
      c.execute(query)
      print('\n[*] -- Found passwords --')
      for row in c:
        host = str(row[0])
        user = str(row[1])
        pwd = str(row[2])
        created = str(row[3])
        lastUsed = str(row[4])
        timesUsed = str(row[5])
        print('[+] Host: ' + host + ', User: ' + \
              user + ', Password: ' + pwd + ', created: '+ \
              created + ', lastUsed: '+lastUsed+ ', timesUsed: '+timesUsed)
    except Exception as e:
      print('Could not execute query on password DB:')
      print('  --> %s'%query)
  except Exception as e:
    if 'encrypted' in str(e):
      print('\n[*] Error reading the database')

###############################################################################
##################################  main  #####################################
###############################################################################
def main():
  # Windows
  #firefoxfolder = os.environ['appdata'] + os.sep + 'Mozilla'+os.sep+'Firefox'+os.sep+'Profiles'
  # Linux
  firefoxfolder = os.path.expanduser('~') + os.sep+'.mozilla/firefox'
  # in respsitory
  # firefoxfolder = '../firefox'

  try:
    firefoxprofiles = os.listdir(firefoxfolder)
    
    for firefoxprofile in firefoxprofiles:
      profile_path = firefoxfolder+os.sep+firefoxprofile
      
      if os.path.isdir(profile_path) and not firefoxprofile == 'Crash Reports':
        #printForm(profile_path+os.sep+'formhistory.sqlite')
        #printCookies(profile_path+os.sep+'cookies.sqlite')
        #printHistory(profile_path+os.sep+'places.sqlite')
        #printGoogle(profile_path+os.sep+'places.sqlite')
        printPasswords(profile_path+os.sep+'signons.sqlite')
        
        # zip profile
        zip_file_name = firefoxprofile+'.zip'
        print('Writing zipfile to %s'%zip_file_name)
        zip_file = zipfile.ZipFile(zip_file_name, 'w', zipfile.ZIP_DEFLATED)
        rootlen = len(profile_path) + 1
        for base, dirs, files in os.walk(profile_path):
          for file in files:
            fn = os.path.join(base, file)
            zip_file.write(fn, fn[rootlen:])

  except Exception:
    print('Das Verzeichnis '+firefoxfolder+' ist nicht vorhanden.')      


      
if __name__ == "__main__":
  main()
  