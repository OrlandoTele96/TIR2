import socket
from ppp import*


p=ppp()
p2=ppp()

print("Connection protocol...")
code=input("Choose a code : ")
ID=int(input("type an ID : "))
info=input("type information : ")

msj_payload=p.crea_payload(code,ID,info)

msj_final=p.crea_paquete(msj_payload,'Enlace')

#p2.quit_ptrnesc(msj_final)
