'''
Title: Projecte Gestió dels vols d'un Aeroport

Autor: Erick Cruz Cedeño
'''

#IMPORTAMOS CLASES QUE NECESSITAMOS (VUELO, SEIENT, Aeropueto) (from <fichero> import <funcion/clases>)
from vuelo import Vol
from seient import Seient
from aeroport import Aeroport

def mostraMenu(aeroport):       #Muestra el menu principal, si la eleccion es correcta retornara el num seleccionado, sino vuelve a llamar la misma fucnicon#
    print(aeroport)             #segun el aeropurto que se introdusca en el (def main) saldra por pantalla uno u otro
    print(" 0. Surt del programa ")
    print(" 1. Crea un nou vol ")
    print(" 2. Cerca un vol  ")
    print(" 3. Modifica un vol ")
    print(" 4. Esborra un vol. Què voleu fer??")
    aeroport.pintaVol()         #muestra por pantalla los vuelos que se han introducido o los que hay en BBDD
    num=int(input("Introduce un numero: "))     # numero entero que introduce el usuario

    if num>=0 and num<=4:   #si el num introducido esta entre 0-4, retornalo
        return num  #retorna el numero introducido por el usuario
    else:
        print("ERROR. Introduzca un numero entre 0-4. ")
        mostraMenu(aeroport)    #recurcion: crida de la misma funcion en ejecucion, en caso de que el num sea incorrecto

def executaOpcioMenu(opcio,aerop):
    if opcio==1:        #1. Crear un vol
        crearVol(aerop)
    elif opcio==2:      #2.Buscar un vuelo
        cercaVol(aerop)
    elif opcio==3:      #3.MODIFICAR UN VUELO
        modificaVol(aerop)
    else:               #opcio==4     4.Esborrar un vol#
        esborraVol(aerop)

def esborraVol(aerop):  #funcion que elimina un vuelo, segun el codigo introducido
    codi_eli=str(input("Codi vol a Eliminar: ")).upper()    #pedimos al usuario que escriba el codigo del vuelo a borrar
    codi_eli=aerop.obteVol(codi_eli)    #miramos si el codigo del vuelo existe en la lista del aeropueto, que es un atributo
    if codi_eli != None:    #si hay algo, porque el metodo obteVol puede retornarte el vuelo o nada.
        aerop.l_vol.remove(codi_eli)    #eliminamos el vuelo con dicho codigo
    else:       #si el codigo del usuario no coincide con ninguno de la lista de codigos de vuelo, imprime un error
        print("ERROR, codi de vol errorni...")

def modificaVol(aerop):     #funcion para modificar algun atributo del vuelo
    codi_mod=str(input("Codi vol a modificar: ")).upper()   #usuario intriduce el codigo del vuelo
    vol = aerop.obteVol(codi_mod) #obtendremos el objeto vuelo que esta lista vuelos de la clase aeropuerto
    if vol != None:     #si hay algo
        print("Actualment el tipus d'avio es:",vol.type_avio,end="")    #se imprime el atributo (avion) que tiene el vuelo
        new_value = str(input(". Introduiu el nou tipos d'avio:"))    #entrada por el usuario el nuevo valor que se introducira en el atrivuto tipo_avion
        vol.type_avio = new_value   #al tener el vuelo podremos modificar el atributo que querramos
    else:   #la varible (vol) no contine nada
        print("El Codi de Vol introduid no coincideix.... vols tornar a intar-ho? (S/N) ")  #en caso de no coincidir ningun vuelo con el que el usuario ha introducido
        opcio = str(input()).upper()    #se da la opcion si quiere volver a introducir el vuelo
        if len(opcio) > 0 and opcio[0] == "S": #si hay algo y en el primer caracter es 'S', realiza un recurcion de la funcuion
            modificaVol(aerop)  # llamada de la mismo funcion en ejecucion

def crearVol(aerop):
    v = Vol()       #Para crear un objeto que esta en otro fichero, (nom_ficher).(nom_clase)(parametro)
    v.inicialitzaTeclat()   #llamas un metodo del vuelo(class)
    s = Seient()    #intancia un objeto de tipo Seient
    s.inicialitzaTeclat()   #permite introducir los atributos del asiento
    v.afegeixSeient(s)      #Añade el asiento al vuelo
    aerop.afegeixVol(v)     #Añade el vuelo al eropuerto
    v.pintaDades()  # imprime la informacion que tiene del vuelo introducido
    opcio=(str(input("Voleu introduir un altre seient? (S/N) "))).upper()       # opcio.upper, convertimos en mayusculas
    while len(opcio)>0 and opcio[0]=="S":   #se da la opcion de introducir diversos asientos en el vuelo
        s=Seient()              #creamos un objeto nuevo
        s.inicialitzaTeclat()   #llamada del metodo para introduccir fila y letra del objeto Seient
        v.afegeixSeient(s)      #llamada del metodo para agregar el objeto asiento en la lista de seient del objeto vuelo
        v.pintaDades()          #imprime la informacon que tiene del vuelo introducido
        opcio=(str(input("Voleu introduir un altre seient? (S/N) "))).upper()   #preguntamos al usuario si quiero volver a introducir un asiento
    aerop.pintaVol()        #imprimimos los vuelos que tiene almacenados el objeto aeroport en su atrubuto lista de vuelos

def cercaVol(aerop):        #permite buscar un vuelo segun las opciones siguientes
    print("0. Surt de la cerca")
    print("1. Cerca per aeroport de destinacio")
    print("2. Cerca per nom de la companyia")
    print("Qué voleu fer")
    num=int(input("Introduce un numero: "))

    if num==0:  #vuelve a la funcion mostramenu()
        mostraMenu(aerop)
    elif num==1:    #cerca por destino
        codi_desti = str(input("Escriu inicials del aeroport de destinacio: ")).upper() #usuario introduce el codigo de destino
        l_cercaVD = []      #lista vacia dnd se guardaran los vuelos encontados
        for i in range(len(aerop.l_vol[:])):    #iteramos la lista de vuelos del aeropueto
            if aerop.l_vol[i].desti == codi_desti:  #si el destino coincide con lo introducido por el usuario
                l_cercaVD = l_cercaVD + [aerop.l_vol[i]]    #se añade a la lista que creamos
        if len(l_cercaVD) ==0:  #si la lista es vacia, es porque no haay ningun vuelo que coincida
            print("No hi ha cap vol que coincideixi")
        else:       #la lista contiene almenos 1 elemento
            print("Llista de codis de vol que coincideixen amb la cerca")
            for j in range(len(l_cercaVD[:])):  #recorrido para printar cada elemento de la lista
                print(l_cercaVD[j])             #imprime cada objeto almacenado en la lista donde se han guardado los vuelos coincidentes
        cercaVol(aerop)
    elif num==2:    #cerca por companyia, es lo mismo que la cerca de destino, solo cambia los atributos a los que se ha de acceder del objeto
        company=str(input("escriu nom de la companyia: ")).upper()
        l_cercaC = []       #lista vacia dnd se guardaran los vuelos encontados
        for i in range(len(aerop.l_vol[:])):
            if aerop.l_vol[i].company == company:
                l_cercaC.append(aerop.l_vol[i])
        if len(l_cercaC) == 0:
            print("No hi ha cap vol que coincideixi")
        else:
            print("Llista de codis de vol que coincideixen amb la cerca")
            for j in range(len(l_cercaC[:])):
                print(l_cercaC[j])
        cercaVol(aerop)
    else: #si es distinto de de 0,1,2#
        print("ERROR. Introduzca un numero entre 0-4. ")
        cercaVol(aerop)     # recursion

def main():
    codi = str(input("Introdueix codi-Aeroport: ")).upper()     #usuario introduce el codigo del AEROPUERTO
    aero_pt = Aeroport(codi,None)   #creamos un objeto aeropuerto donde introducimos nosotros los argumentos que nos solicita el metodo __init__
    aero_pt.llegeixBBDDAeroport()   #de la BBDD lee los vuelos con sus atrivutos y los añade en lista vuelos
    opcio = mostraMenu(aero_pt)     #muestra el menu principal con sus opciones , donde retornara un numero entero
    while (opcio != 0) :            #mientras num sea distinto de 0
        executaOpcioMenu(opcio,aero_pt)     #llama a la funcion que pasamos por paremetros el numero entero y el aeropuerto
        opcio= mostraMenu(aero_pt)          #varible que nos permitira salir del bucle y finalizar el programa
    print("Se esta saliendo del programa ...")  #muestra por pantalla

#progrma principal
main()  #llama a la funcion main()
