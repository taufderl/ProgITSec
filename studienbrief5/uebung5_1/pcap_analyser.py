#!/usr/bin/env python
# this is a python 2.x file due to dpkt dependency
#
#  pcap_analyser.py
#
#  Copyright 2014 Tim auf der Landwehr <dev@taufderl.de>
#
#  This script provides a pcap data analyser.
#  It is able to count the packets in a pcap file.
#
import sys
import getopt
import dpkt

# pcap analyser class
class PCAPAnalyser:
  
  # init
  def __init__(self, filename):
    self.filename = filename
    pcap_file = open(filename)
    self.pcap = dpkt.pcap.Reader(pcap_file)
  
  # count all packages
  def count_packages(self):
    packages = 0
    for x,y in self.pcap:
      packages += 1
    print("The file %s contains %i packages."%(self.filename, packages))
    
# usage
def usage():
  print("\n pdf_to_text.py by Tim auf der Landwehr")
  print('')
  print(' Usage: pcap_analyser.py')
  print('   > Analyse .pcap files')
  print('')
  print(' --file [filename]')
  print(' \t.pcap-file to be analysed')
  print(' -h --help')
  print(' \tShow this information')
  
# main
def main():
  try:
    opts, args = getopt.gnu_getopt(sys.argv[1:],"ho:v",["help", "file="])
  except (getopt.GetoptError, NameError):
    usage()
    sys.exit()

  # defaults
  filename = ''

  # get parameters
  for o,v in opts:
    if o in ['--file']:
      filename = v
    elif o in ['-h','--help']:
      usage()
      sys.exit(1)
    else:
      print('unknown parameter %s'%o)
      sys.exit(1)

  # make sure that a file is specified
  if filename == '':
      print('Please specify an input file.')
      sys.exit(1)

  # create analyser
  analyser = PCAPAnalyser(filename)
  # count packets
  analyser.count_packages()

if __name__ == "__main__":
  main()
