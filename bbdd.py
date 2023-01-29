#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
title: Definicion del la clase BBDD

Autor: Erick Cruz Cedeño
'''
#importamos librerias y clases necesarias
import cx_Oracle
from vuelo import Vol
from seient import Seient

#Definicion clase BBDD, Esta nos permitira realizar consulta sql, en la cual podremoas obtener vuelos, asientos, etc..
class BBDD:
    #modifiqueu usuari i contrasenya pel que correspongui
    usuari = "your id"
    contrasenya = "your password"
    conn = None

    def obreConnexio(self): #permite conectarnos con el oracle
        dsn_tns = cx_Oracle.makedsn('sab-oracle.uab.es','1521', service_name='polux')
        self.conn = cx_Oracle.connect(user=self.usuari, password=self.contrasenya, dsn=dsn_tns)

    def tancaConnexio(self):    #permite cerrar la coneccion con aracle
        self.conn.close()

    # donat un codi d'aeroport, retorna el nom de l'aeroport
    def obteNomAeroport(self,codiAero):
        self.obreConnexio()  # abre la coneccion en els ervidor de oracle
        try:    #intenta realizar lo que hay dentro del sangriado y si hay algun fallo, pasara al except
            cur = self.conn.cursor()    #intenta conectar
            cur.execute("select nom from aeroport where codi_aeroport = '" + codiAero + "'")  # 2n forma (bind variables): cur.execute("SELECT * FROM mytab WHERE mycol = :mybv", mybv=myvar)
            n_aerop = ""  # creo un varible vacia dnd se guardara el aeropueto que concida con su codigo
            for i in cur:  # recorro cur donde almacena la sql query
                n_aerop = i[0]  # guardo el el resultado en la varible
            cur.close()  # cierro y desconectamos coneccion
            self.tancaConnexio()    # cirra la coneccion con oracle
            return n_aerop  # retornamos la varible con el nombre del aeropuerto
        except:  # si hay algun error en las lineas de try, pasara al except
            self.tancaConnexio()  # cerrara la connecion

    # obetenemos un lista de asientos, realizando una consulta dando por parametro el codigo y la fecha del vuelo
    def obteLlistaSeients(self,codivol,data):
        self.obreConnexio() #abre la coneccion en els ervidor de oracle
        try:    #intenta ejecutar lo que hay dentro del sangriado
            cur = self.conn.cursor() #abre coneccion con oreacle
            #executem la consulta SQL. combinem text fix amb text que ens passen per parÃ metre
            data = data.date()  #data(), perimite que si la fecha esta en formato dia,mes,año y horas solo coguera la yyyy-mm-dd
            cur.execute("select fila, lletra from seient where codi_vol= '" +codivol+ "' and data=to_date('" +str(data)+ "', 'yyyy-mm-dd')") #ejecutamos la consulta sql
            #creem una llista buida que contindrÃ  tots els seients del vol
            llista = [] #lista vacia donde se guardaran los asientos de la consulta
            #la consulta podria retornar diverses files. les recorrem
            for tupla in cur:
                #per cada fila, podem obtenir les columnes
                #en aquest exemple, la columna fila Ã©s la primera, i la lletra la segona
                seat = Seient() #creamos un objeto seient
                seat.readBBDD(tupla[0],tupla[1])    #permite atribuir el asineto con su fila y letra
                llista.append(seat)             #este asiento se inserta en la lista
            cur.close()     #cierra la consulta
            #retornem la llista
            #Ã©s una llista de llistes: per a cada tupla, contÃ© dos camps: la fila i la lletra
            self.tancaConnexio()    #al finalizar el recorrido, se cerrara la conneccion con oracle
            return llista   #retorna la lista con los asientos de la consulta generada
        except:     #en caso que no se pueda conectar, cierra la connecion
            self.tancaConnexio()

    # donat un codi d'aeroport, obtÃ© el codi, la data, la companyia, el tipus d'aviÃ³, la destinacio i l'origen
    # el codi d'aeroport pot ser tant d'origen com de destÃ­
    def obteLlistaVols(self,codiaero):
        self.obreConnexio() #abre la conneccion en oracle
        try:    #intentamos ejecutar la parte del try y si hay algun fallo, pasara al except
            cur = self.conn.cursor()    #abre coneccion con oreacle
            # sql query, los codigos de vuelos que tiene como origen BCN
            cur.execute("select codi_vol, data, companyia, tipus_avio, origen, destinacio from vol where origen = '" +codiaero+"'")
            l=[]    #lista vacia donde se guaradaran los vuelos de la sql query
            for i in cur:   #recorremos la sql query
                v=Vol()     #creamos un objeto vuelo
                v.readVolBBDD(i[0],i[1],i[2],i[3],i[4],i[5])    # Atribuimos el vuelo con sus atributos
                l.append(v)         #añadimos el vuelo a lista de vuelos
            #sql query, los codigos de vuelos que tiene como destino BCN
            cur.execute("select codi_vol, data, companyia, tipus_avio, destinacio, origen from vol where destinacio = '" + codiaero + "'")
            for i in cur:   #recorremos la sql query
                v = Vol()   #creamos un objeto vuelo
                v.readVolBBDD(i[0], i[1], i[2], i[3], i[5], i[4])   # Atribuimos el vuelo con sus atributos
                l.append(v)     #añadimos el vuelo a lista de vuelos
            cur.close()      #cierra la consulta
            self.tancaConnexio()    #al finalizar el recorrido, se cerrara la conneccion con oracle
            return l    #retorna la lista con los veulos de la sql query
        except:
            self.tancaConnexio()
