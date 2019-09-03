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
        self.pttrnescp=125# Patron de escape 01111110 en decimal
        self.protocol={
        'Enlace' : 49185,
        'PAP' : 49187
        }

    def crea_payload(self,code,ide,data):
        length=len(data)+4#longitud de cada cabecera en bytes
        m=pack('!BBH',self.codigos[code],ide,length)+bytes(data,'utf-8')
        #print(pack('!BBH',self.codigos[code],ide,length).hex())
        return m

    def crea_paquete(self,msj,prtcol):
        header=pack('!BBBH',self.flag,self.address,self.control,self.protocol[prtcol])
        #Aplica crc16
        p=header+msj
        msj_final=self.search_esc(p)
        #print(msj_final.hex())

    def lee_payload(self,m):
        header=unpack('!BBH',m[:4])
        datos=m[4:]
        tipo='NF'
        for c in self.codigos:
            if self.codigos[c]==header[0]:
                tipo=c
        return tipo, header[1],datos

    def search_esc(self,msj):
        """Busca que no esté el patron la bandera en el mensaje"""
        mensaje=msj.hex()
        L=len(mensaje)
        temp=mensaje[2:L-2]
        temp2=temp
        msj_f=mensaje[:2]
        flag=pack('!B',self.flag).hex()
        patron=pack('!B',self.pttrnescp).hex()
        act=0
        for i in range(len(temp)):
            pos=temp2.find(flag)
            if pos != -1:
                for i in range(act,pos):
                    msj_f += temp[i]
                act=pos

                msj_f = msj_f +patron + temp[act:act+2]
                temp2=temp[act+2:]
            else:
                msj_f=msj_f+temp2

                break

        msj_f=msj_f+mensaje[L-2:L]
        return msj_f
