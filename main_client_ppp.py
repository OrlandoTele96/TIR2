import socket
from ppp import*

"""Init """
p=ppp()
IP='127.0.0.1'
PORT=3000

"""information"""
print("Connection protocol...")
code=input("Choose a code : ")
ID=int(input("type an ID : "))
info=input("type information : ")
"""making payload"""
msj_payload=p.crea_payload(code,ID,info)
"""packing the message"""
msj_final=p.crea_paquete(msj_payload,'Enlace')
print(msj_final)
"""Sending information"""
sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.connect((IP,PORT))
print("Connection with ...",IP)

sock.sendall(msj_final.encode('utf-8'))
