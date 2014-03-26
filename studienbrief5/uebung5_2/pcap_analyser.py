#!/usr/bin/env python
# this is a python 2.x file due to dpkt dependency
#
#  pcap_analyser.py
#
#  Copyright 2014 Tim auf der Landwehr <dev@taufderl.de>
#
#  This script provides a pcap data analyser.
#  It is able to count all packets in a pcap file, 
#  find IP packets and distinguish TCP and UDP packets.
#
import sys
import getopt
import dpkt
import socket

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
    print("The file %s contains %i packets."%(self.filename, packages))
    return packages
  
  # count ip, udp and tcp packets
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
  # count ip, upd and tcp packets
  analyser.count_package_types()

      
if __name__ == "__main__":
  main()
