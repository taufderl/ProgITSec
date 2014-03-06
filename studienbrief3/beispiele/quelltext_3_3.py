from socket import *
status={0:"open", 10049:"address not available",
        10061:"closed",10060:"timeout",
        10056:"already connected",10035:"filtered",
        11001:"IP not found",10013:"permission denied"}
def scan(ip,port,timeout):
    s = socket(AF_INET, SOCK_STREAM)
    s.settimeout(timeout)   
    try:
        result= s.connect_ex((ip, port)) 
    except: 
        print ("Cannot connect to IP")
        return
    s.close()
    return status[result]

ip="127.0.0.1"
portstart=1
portstop=1023
timeout=1
for  port in range (portstart, portstop):
    ret=scan(ip,port,timeout)
    print("Port ", port, " is ", ret)