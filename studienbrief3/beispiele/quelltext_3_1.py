import socket
HOST = ''       
PORT = 50007   
lis = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
lis.bind((HOST, PORT))   
lis.listen(1)            
try: 
    while True:             
        com, addr = lis.accept()
        print('Connected by', addr)
        while True:    
            data = com.recv(1024)  
            if not data:           
                com.close()
                break
            print("[%s] %s" % (addr, data))
            com.sendall(data)
finally:
    com.close()