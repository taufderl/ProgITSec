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
  
  def show_communication(self, ip_range):
    for (ts, buf) in self.pcap:
      try:
        eth = dpkt.ethernet.Ethernet(buf)
        # only analyse TCP packets
        if eth.type == dpkt.ethernet.ETH_TYPE_IP \
          and eth.data.p == dpkt.ip.IP_PROTO_TCP:
          
          # find source
          ip = eth.data
          src = socket.inet_ntoa(ip.src)
          # check if in requested range
          if src.startswith(ip_range):
            tcp = ip.data
            http = dpkt.http.Request(tcp.data)
            print("------------------------------------------------------")
            print(http.headers['user-agent'])
            print(http.headers['host'])
            print(src)
      except:
        pass
      
def usage():
  print("\n pdf_to_text.py by Tim auf der Landwehr")
  print('')
  print(' Usage: pcap_analyser.py')
  print('   > Analyse .pcap files')
  print('')
  print(' --file [filename]')
  print(' \t.pcap-file to be analysed')
  print(' --ip [ip]')
  print(' \t.IP range to be shown, default: [192.168.179.x]')
  print(' \t.Specify without x  ')
  print(' -h --help')
  print(' \tShow this information')

def main():
  try:
    opts, args = getopt.gnu_getopt(sys.argv[1:],"ho:v",["help", "file=", "ip="])
  except (getopt.GetoptError, NameError):
    usage()
    sys.exit()

  # defaults
  filename = ''
  ip_range = '192.168.179.'

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
  analyser.show_communication(ip_range)

      
if __name__ == "__main__":
  main()
