#!/usr/bin/env python
# this is a python 2.x file due to dpkt dependency
import sys
import getopt
import dpkt
import socket

class PCAPAnalyser:
  
  def __init__(self, filename):
    self.filename = filename
    pcap_file = open(filename)
    self.pcap = dpkt.pcap.Reader(pcap_file) 
    
  def count_packages(self):
    packages = 0
    for x,y in self.pcap:
      packages += 1
    print("The file %s contains %i packets."%(self.filename, packages))
    return packages
  
  def count_package_types(self):
    ip = tcp = udp = other = nonip = 0
    for (ts, buf) in self.pcap:
      try:
        eth = dpkt.ethernet.Ethernet(buf)
        if eth.type == dpkt.ethernet.ETH_TYPE_IP:
          ip += 1
          if eth.data.p == dpkt.ip.IP_PROTO_TCP:
            tcp += 1
          elif eth.data.p == dpkt.ip.IP_PROTO_UDP:
            udp += 1
          else:
            other += 1
        else:
          nonip += 1
      except:
        pass
    print("The file %s contains:"%(self.filename))
    print("%i IP packets"%ip)
    print("  >%i TCP packets"%tcp)
    print("  >%i UDP packets"%udp)
    print("  >%i other IP packets"%other)
    print("%i non-IP packets"%nonip)
    
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
  analyser.count_package_types()

      
if __name__ == "__main__":
  main()
