#I. A. a. Violent Python S.38f
import argparse
from socket import *
from threading import *
screenLock = Semaphore(value=1)
def connScan(tgtHost, tgtPort):
    try:
        connSkt = socket(AF_INET, SOCK_STREAM)
        connSkt.connect((tgtHost, tgtPort))
        connSkt.send('HS AlbSig\r\n')
        results = connSkt.recv(100)
        screenLock.acquire()
        print('[+]%d/tcp open'% tgtPort)
        print('[+] ' + str(results))

    except:
        screenLock.acquire()
        print('[-]%d/tcp closed'% tgtPort)
    finally:
        screenLock.release()
        connSkt.close()

def portScan(tgtHost, tgtPorts):
    try:
        tgtIP = gethostbyname(tgtHost)
    except:
        print("[-] Cannot resolve '%s': Unknown host"\
            %tgtHost)
        return
    try:
        tgtName = gethostbyaddr(tgtIP)
        print('\n[+] Scan Results for: ' + tgtName[0])
    except:
        print('\n[+] Scan Results for: ' + tgtIP)
    setdefaulttimeout(1)
    for tgtPort in tgtPorts:
        t = Thread(target=connScan, args=(tgtHost,\
            int(tgtPort)))
        t.start()
        print('Scanning port ' + tgtPort)
        connScan(tgtHost, int(tgtPort))

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-H', dest='tgtHost',\
        help='specify target host', required=True)
    parser.add_argument('-p', dest='tgtPort', nargs='+',\
        help='specify target ports separated by comma',\
        required=True)
    args = parser.parse_args()
    tgtHost = args.tgtHost
    tgtPorts = args.tgtPort

    portScan(tgtHost, tgtPorts)
if __name__ == '__main__':
    main()