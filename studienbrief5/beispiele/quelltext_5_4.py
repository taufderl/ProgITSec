#I. A. a. Violent Python
import dpkt
import socket
import pygeoip
import argparse
gi = pygeoip.GeoIP('/opt/GeoIP/Geo.dat')
def retGeoStr(ip):
    try:
        rec = gi.record_by_name(ip)
        city = rec['city']
        country = rec['country_code3']
        if city != '':
            geoLoc = city + ', ' + country
        else:
            geoLoc = country
        return geoLoc
    except Exception, e:
        return 'Unregistered'
def printPcap(pcap):
    for (ts, buf) in pcap:
        try:
            eth = dpkt.ethernet.Ethernet(buf)
            ip = eth.data
            src = socket.inet_ntoa(ip.src)
            dst = socket.inet_ntoa(ip.dst)
            print '[+] Src: ' + src + ' --> Dst: ' + dst
            print '[+] Src: ' + retGeoStr(src) +\
                ' --> Dst: ' + retGeoStr(dst)
        except:
            pass
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', dest='pcapFile',\
        type=str, help='specify pcap filename',\
        required=True)
    args = parser.parse_args()
    f = open(args.pcapFile)
    pcap = dpkt.pcap.Reader(f)
    printPcap(pcap)
if __name__ == '__main__':
    main()