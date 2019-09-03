import socket
from ppp import*


p=ppp()

print("Connection protocol...")
code=input("Choose a code : ")
ID=int(input("type an ID : "))
info=input("type information : ")

msj_payload=p.crea_payload(code,ID,info)
