from struct import*
"""-------------------------Terminar-----------------------------------------
Checar el loging de ppp------------------------------------------------------"""
class ppp:

    def __init__(self):
        self.codigos={
            'Configure-Request':1,
            'Configure-Ack' : 2,
            'Configure-Nak' : 3,
            'Configure-Reject' : 4
        }
        pass

    def crea_p(self,code,ide,data):
        length=len(data)+4#longitud de cada cabecera en bytes
        m=str(pack('!BBH',self.codigos[code],ide,length).hex())+data
        #print(pack('!BBH',self.codigos[code],ide,length).hex())
        return m

    def lee_p(self,m):
        header=unpack('!BBH',m[:4])
        datos=m[4:]
        tipo='NF'
        for c in self.codigos:
            if self.codigos[c]==header[0]:
                tipo=c
        return tipo, header[1],datos

p=ppp()
m=p.crea_p('Configure-Nak',10,'hola')
print(' '.join(x for x in m))
print(m)
#print (p.lee_p(m))
