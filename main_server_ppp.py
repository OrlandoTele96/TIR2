from ppp import*
import socket


"""Init"""
p=ppp()
IP='127.0.0.1'
PORT=3000

"""Receive information"""
sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.bind((IP,PORT))
sock.listen(1)
while True:
    print("waiting for info....")
    connection,client_address=sock.accept()
    while True:
        print("connecting....")
        msj_reveived=connection.recv(1064)
        if not msj_reveived:
            break
connection.close()
sock.close()
