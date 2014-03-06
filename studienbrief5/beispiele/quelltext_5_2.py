import dpkt

f = open('test.pcap')
pcap = dpkt.pcap.Reader(f)

for ts, buf in pcap:
    try:
        eth = dpkt.ethernet.Ethernet(buf)
        ip = eth.data
        tcp = ip.data

        if tcp.dport == 80 and len(tcp.data) > 0:
            http = dpkt.http.Request(tcp.data)
            print http.method
            print http.uri
            print http.version
            print http.headers['user-agent']
            print '-------------------------'
    except:
        pass

f.close()