#I. A. a. Violent Python S.35f
import argparse
from socket import *

def connScan(tgtHost, tgtPort):
    try:
        connSkt = socket(AF_INET, SOCK_STREAM)
        connSkt.connect((tgtHost, tgtPort))
        connSkt.send('ViolentPython\r\n')
        results = connSkt.recv(100)
        print('[+]%d/tcp open'% tgtPort)
        print('[+] ' + str(results))
        connSkt.close()
    except:
        print('[-]%d/tcp closed'% tgtPort)

def portScan(tgtHost, tgtPorts):
    try:
        tgtIP = gethostbyname(tgtHost)
    except:
        print("Cannot resolve '%s': Unknown host"\
            %tgtHost)
        return
    try:
        tgtName = gethostbyaddr(tgtIP)
        print('\n[+] Scan Results for: ' + tgtName[0])
    except:
        print('\n[+] Scan Results for: ' + tgtIP)
    setdefaulttimeout(1)
    for tgtPort in tgtPorts:
        print('Scanning port ' + tgtPort)
        connScan(tgtHost, int(tgtPort))

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-H', dest='tgtHost', type=str,\
        help='specify target host', required=True)
    parser.add_argument('-p', dest='tgtPort', nargs='+',\
        help='specify target port', required=True,\ 
        type=int)
    args = parser.parse_args()

    portScan(args.tgtHost, args.tgtPort)
if __name__ == '__main__':
    main()
