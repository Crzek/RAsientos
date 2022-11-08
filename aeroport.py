'''
title: definicon del la clase Aeroport

Autor: Erick Cruz Cedeño
'''
#IMPORTAMOS CLASES NECESSARIAS
from bbdd import BBDD


#Representa los aeropuetos y sus funciones que puede realizar como aeropuerto
class Aeroport():

    def __init__(self,codi,nom):    #constructor de la instancia, son de tipo str
        self.codi = codi    # al crear el objeto aeropuerto siempre se debera pasar por argumentos el codigo y nombre del aeropuerto
        self.nom = nom
        self.l_vol =[]  #lista donde guardaran los objetos vuelos del aeropuerto

    def __str__(self):  # al imprir el objeto Aeropuerto, nos saldra con su codigo y nombre
        return self.nom+"--("+self.codi+")"

    def inicialitzaTeclat(self):    #En caso de que el asuario quiero introducir los atributos del aeropuerto
        self.codi = (str(input("escriu el codi: "))).upper()
        self.nom = (str(input("escriu nom: ")))

    def afegeixVol(self,vol):   #inserta los vuelos en el atributo de la lista del aeropueto
        self.l_vol += [vol]

    def pintaVol(self): #realiza un recorrido de cada eleimento de la lista del aeropuerto y lo imprime
        if len(self.l_vol[:]) > 0:  # si hay algo en la lista
            print("Lista de vuelos: ")
            i=0         #iterador
            while i < len(self.l_vol[:]): #mientras i sea inferior a la longitud de la lista
                print(self.l_vol[i])    #imprimimos el objeto que se encuentra en la lista de vuelos del aeropuerto
                i = i + 1   #siguente elemento
        else:       # al no haber nada en l_vol, la lista esta vacia
            print("lista de vuelos vacia.")

    def obteVol(self,codivol):  #obtiene el vuelo qe se encuentra en la lista de la clase aeropuerto
        trobat = False      #   realizamos una cerca
        i = 0   #iterador
        while i < len(self.l_vol) and not trobat:   #mientras no eencontrado e (i) inferieor a la longitud de la lista
            if self.l_vol[i].codi == codivol:       #coparmos si el vuelo coincide
                trobat = True   #si coincide, la varible trobat sera TRUE
            else:       #si al comparar no coinciden itera el siguiente elemento
                i+=1    #siguiente elemento
        if trobat:  #si se ha encontrado, retornara el vuelo
            vol= self.l_vol[i]
        else:       #si no se encuentra, retorna nada
            vol = None
        return vol

    def pintaDades(self,):  #imprime valores introducidos por el Usuario
        print("Codi: "+ self.codi, end=" ")
        print("Nom: " + self.nom)

    # permite obeter el el nombre del aeropuerto segun su codigo realizando una sql query
    def llegeixBBDDAeroport(self):
        print("Por favor espere, Cargando con la BBDD...")  #dependiendo del aeropuerto hay algunos que tienen mas informacion y tardan mas en procesar los datos
        bbdd = BBDD()   #creamos objeto bbdd
        self.nom = bbdd.obteNomAeroport(self.codi)  #metodo que nos permiten obtener el nombre del Aeropeto, pasando por argumento su codigo
        print("Obteniendo vuelos de la BBDD, espere...")
        # realizamos un sql query donde obtendremos todos los vuelos del aeropuerto y este sera igual a la lista de vuelos
        self.l_vol = bbdd.obteLlistaVols(self.codi)
        for i in self.l_vol:    #recoremos cada vuelo para obtner todos los asiento de su vuelo
            i.seients = bbdd.obteLlistaSeients(i.codi,i.data)  #obtenemos todos los asientos y los añadimos al atributo lista de asientos del vuelo

