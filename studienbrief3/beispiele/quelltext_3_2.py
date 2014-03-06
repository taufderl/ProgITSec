import socket

HOST = '127.0.0.1'
PORT = 50007
con = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
con.connect((HOST, PORT))

try:
    while True:
        message = input("Ihre Eingabe: ")
        message_b = message.encode('iso-8859-1')
        con.sendall(message_b)
        answer = con.recv(1024)
        answer_2=answer.decode('iso-8859-1')
        print('Received', ((repr(answer_2))) )
finally: 
    con.close()