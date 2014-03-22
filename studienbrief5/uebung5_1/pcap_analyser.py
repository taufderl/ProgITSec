#!/usr/bin/env python
# this is a python 2.x file due to dpkt dependency
import sys
import getopt
import dpkt

class PCAPAnalyser:
  
  def __init__(self, filename):
    self.filename = filename
    pcap_file = open(filename)
    self.pcap = dpkt.pcap.Reader(pcap_file)
    
  def count_packages(self):
    packages = 0
    for x,y in self.pcap:
      packages += 1
    print("The file %s contains %i packages."%(self.filename, packages))
    
    
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

def main():
  try:
    opts, args = getopt.gnu_getopt(sys.argv[1:],"ho:v",["help", "file="])
  except (getopt.GetoptError, NameError):
    usage()
    sys.exit()

  # defaults
  filename = ''

  for o,v in opts:
    if o in ['--file']:
      filename = v
    elif o in ['-h','--help']:
      usage()
      sys.exit(1)
    else:
      print('unknown parameter %s'%o)
      sys.exit(1)

  if filename == '':
      print('Please specify an input file.')
      sys.exit(1)

  analyser = PCAPAnalyser(filename)
  analyser.count_packages()

      
if __name__ == "__main__":
  main()
