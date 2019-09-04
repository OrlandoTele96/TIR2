from struct import*
import crc16
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
        p=header+msj
        print(p)
        crc=crc16.crc16xmodem(p)
        p += pack('!IB',crc,self.flag)
        msj_final=self.get_esc(p)
        #print(msj_final.hex())
        return msj_final

    def lee_payload(self,m):
        header=unpack('!BBH',m[:4])
        datos=m[4:]
        tipo='NF'
        for c in self.codigos:
            if self.codigos[c]==header[0]:
                tipo=c
        return tipo, header[1],datos

    def get_esc(self,msj):
        """Pone el patron de escpa"""
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

    def Unpack_msj(self,msj):
        self.flag=unpack('!B',bytes.fromhex(msj[:2]))[0]
        self.address=unpack('!B',bytes.fromhex(msj[2:4]))
        self.control=unpack('!B',bytes.fromhex(msj[4:6]))
        protocol=unpack('!H',bytes.fromhex(msj[6:10]))[0]
        temp=msj[10:]
        msj_out=self.lee_payload(bytes.fromhex(temp))
        return msj_out


    def quit_ptrnesc(self,msj):
        L=len(msj)
        temp=msj
        patron=pack('!B',self.pttrnescp).hex()
        for i in range(L):
            pos=temp.find(patron)
            if pos != -1:
                msj_out=temp[:pos]
                print("primera parte",msj_out)
                msj_out +=temp[pos+2:]
                print("sin patron",msj_out)
                temp=msj_out
            else:
                break
        return msj_out
