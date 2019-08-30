from struct import*
"""-------------------------Terminar-----------------------------------------
Checar el loging de ppp------------------------------------------------------"""
class ppp:
    codigos={
    'Configure-Request':1,
    'Configure-Ack' : 2,
    'Configure-Nak' : 3,
    'Configure-Reject' : 4
    }
    def __init__(self):
        pass

    def crea_msj(self,code,ide,data):
        length=len(data)+4#longitud de cada cabecera en bytes
        m=pack('!BBH',self.codigos[code],ide,length)+data
        return m

    def lee_msj(self,m):
        header=unpack('!BBH',m[:4])
        datos=m[4:]
        tipo='NF'
        for c in self.codigos:
            if self.codigos[c]==header[0]:
                tipo=c
        return tipo, header[1],datos

p=ppp()
m=p.crea_msj('Configure-Nak',10,'hola')
print(' '.join(x.encode('hex') for x in m))
print p.lee_msj(m)
