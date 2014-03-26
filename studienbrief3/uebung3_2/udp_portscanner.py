#!/usr/bin/env python
# since nmap is not available for python3 this is an python2.x file
#
#  udp_portscanner.py
#
#  Copyright 2014 Tim auf der Landwehr <dev@taufderl.de>
#
#  This script provides an udp portscanner.
#
import sys
import nmap
import getopt

# usage
def usage():
  print("\n udp_portscanner.py by Tim auf der Landwehr")
  print('')
  print(' Usage: udp_portscanner.py')
  print('   > Scan UDP all ports on certain host and writes result to csv file')
  print('')
  print(' --host [hostname]')
  print(' \tSet the hostname, default: localhost')
  print(' -o --out [filename]')
  print(' \tSet the output filename, default: ports.csv')
  print(' --range [from-to]')
  print(' \tSet the port range in the format \'a-b\', default: 20-443')
  print(' --tcp')
  print(' \tAdditionally scan all TCP ports in the given range')
  print(' -h --help')
  print(' \tShow this information')

# main
def main():
  try:
    opts, args = getopt.gnu_getopt(sys.argv[1:],"ho:v",["help", "host=", "range=", "out=", "tcp"])
  except (getopt.GetoptError, NameError):
    usage()
    sys.exit()

  # defaults
  hostname = '127.0.0.1'
  port_range = '20-443'
  outfile = 'ports.csv'
  udp = True
  tcp = False
  
  # get parameters
  for o,v in opts:
    if o in ['--host']:
      hostname = v
    elif o in ['--range']:
      port_range = v
    elif o in ['-o', '--out']:
      outfile = v
    elif o in ['-h','--help']:
      usage()
      sys.exit(1)
    elif o in ['--tcp']:
      tcp = True
    else:
      print('unknown parameter %s'%o)
      sys.exit(1)

  # write headers to csv file
  with open(outfile, 'w') as csv_file:
    csv_file.write('protocol;port;state;name;program;version\n')
  
  # run nmap scanner
  nm = nmap.PortScanner()
  nm.scan(hostname, port_range)
  
  # write results to file
  with open(outfile, 'a') as csv_file:
    if udp:
      for port in nm[hostname].all_udp():
        port_info = nm[hostname]['udp'][port]
        csv_string = 'UDP'
        csv_string += ';'+ str(port)
        csv_string += ';'+ port_info['state']
        csv_string += ';'+ port_info['name']
        csv_string += ';'+ port_info['product']
        csv_string += ';'+ port_info['version']
        csv_string += '\n'
        csv_file.write(csv_string)
    if tcp:
      for port in nm[hostname].all_tcp():
        port_info = nm[hostname]['tcp'][port]
        csv_string = 'TCP'
        csv_string += ';'+ str(port)
        csv_string += ';'+ port_info['state']
        csv_string += ';'+ port_info['name']
        csv_string += ';'+ port_info['product']
        csv_string += ';'+ port_info['version']
        csv_string += '\n'
        csv_file.write(csv_string)
    
  print("Wrote open ports to %s."%outfile)
    
if __name__ == "__main__":
  main()
