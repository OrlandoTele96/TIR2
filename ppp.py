from struct import*
"""-------------------------Terminar-----------------------------------------
Checar el loging de ppp------------------------------------------------------"""
class ppp:

    def __init__(self):
        self.codigos={
            'Configure-Request':1,
            'Configure-Ack' : 2,
            'Configure-Nak' : 3,
            'Configure-Reject' : 4,
            'Terminate-Request' : 5,
            'Terminate-Ack' : 6,
            'Code-Reject' : 7,
            'Protocol-Reject' : 8,
            'Echo-Request' : 9,
            'Echo-Reply' : 10,
            'Discard-Request' : 11
        }
        self.address=255 #broadcast
        self.flag=126#bandera 01111110 en decimal
        self.control=3 #byte de control 00000011 en decimal
        #self.pttrnescp=126
        self.protocol={
        'Enlace' : 49185,
        'Password-Auth' : 49187
        }

    def crea_payload(self,code,ide,data):
        length=len(data)+4#longitud de cada cabecera en bytes
        m=pack('!BBH',self.codigos[code],ide,length)+bytes(data,'utf-8')
        #print(pack('!BBH',self.codigos[code],ide,length).hex())
        return m

    def crea_frame(self,msj):
        pass

    def lee_payload(self,m):
        header=unpack('!BBH',m[:4])
        datos=m[4:]
        tipo='NF'
        for c in self.codigos:
            if self.codigos[c]==header[0]:
                tipo=c
        return tipo, header[1],datos

p=ppp()
m=p.crea_payload('Configure-Nak',10,'hola')
#print(' '.join(x for x in m))
print(m)
print(type(m))
print (p.lee_payload(m))
