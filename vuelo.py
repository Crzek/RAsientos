'''
title: definicon del la clase Vol

Autor: Erick Cruz Cedeño
'''
#Representan los vuelos que tiene un aeropueto, con sus, codigo, destino,origen,etc.
class Vol():
    #Atributos del VOL a traves de un constructor de la instancia en el momento de crear el objeto
    def __init__(self): # todos son tipo (str), ecepto seient que es una lista vacia que tendra objetos seients
        self.codi = None
        self.data = None
        self.company  = None
        self.type_avio = None
        self.origen = None
        self.desti = None
        self.seients = []   #lista donde se guardan los objetos seients


    #Metodos
    def __str__(self):  #al imprimir dicho objeto nos saldra la forma en que nos guarda la variable c
        c = "CODI:"+self.codi+" Data: "+str(self.data)+" Companyia:"+self.company+" Avio:"+self.type_avio+" Origen:"+self.origen+" desti:"+self.desti
        return c    #retorna la cadena de caracteres redefinida

    def pintaDades(self):   #muestra los datos introducidos por el usuario
        print("Codi:", self.codi, end=" ")  # end="", esto perimite que el siguiente print se realice en la misma linia
        print("Data(yyyy-mm-dd):", self.data, end=" ")
        print("Companyia:", self.company, end=" ")
        print("Tipo de avio:", self.type_avio, end=" ")
        print("Desti:", self.desti, end=" ")
        print("Origen:", self.origen, end=" ")
        print("seients:",end="")
        self.pintaSeient()

    def inicialitzaTeclat(self):  # metodo para que el usuario pueda intrucir atributos del vuelo
        self.codi = ((str(input("Introduce Codi: ")))).upper()  #upper, tranforma todos los caracteres en mayusculas
        self.data = self.comprovarData(str(input("Introduce data (dd/mm/yyyy): ")))
        while not self.data:  # entrara en el bucle siempre y cuando data= TRUE, y se debera repetir otra vez el ingreso de la variable
            self.data = str(input("Introduce data (dd/mm/yyyy): "))  # modo abreviado==> self.data=comprovarData(str(input("Introduce data:")))
            self.data = self.comprovarData(self.data)                #comprueba si la data es correcta
        self.company = (str(input("Introduce Companyia: "))).upper()
        self.type_avio = (str(input("Introduce tipo de Avion: "))).capitalize() #capitalize, transforma el el primer caracter de la cadena en mayuscula
        self.origen = (str(input("Introduce origeno: "))).upper()
        self.desti = (str(input("Introduce destino: "))).upper()

    def afegeixSeient(self, seat):  # añade el seient en la lista seients
        self.seients.append(seat)  # agrega a la lista el objeto seient ==> opcion2) seients = seients +[seat]

    def pintaSeient(self):  # muestra todos los asientos del vuelo, recorrer lista e imprimir cada valor recorrido
        if len(self.seients[:]) > 0:  # si hay algo en la lista
            for i in self.seients:#recorremos el atributo lista seients, para obtener la fila y lletra, para imprimirlas
                if i==self.seients[-1]: #verificamos si el elemento coniencide con el ultimo de la lista
                    print(i.fila, i.lletra) #lo imprimimos pero sin el end=""
                else:
                    print(i.fila, i.lletra, end=",")#muestra por pantalla la fila y letra del asiento
        else:   #si esta vacia lista
            print("lista de asientos vacia.")

    def comprovarData(self,textData):   #funcion para combrovar la fecha
        from datetime import datetime   #importamos libreria que necesitamos
        try:
            data = datetime.strptime(textData,"%d/%m/%Y")  #si la data es correcta retorna la fecha
            print ("La data és correcta")
            return data     #devuelve la fecha correcta
        except ValueError:
            print ("El format de la data o la data no són correctes")
            return False    #la fecha es incorrecta

    # este metodo permite que la consulta sql generada de los vuelos se convierta en un objeto vuelo con sus atributos
    def readVolBBDD(self,codi,data,company,t_avio,origen,desti):
        self.codi = codi    #asignamos cada atributo con su parametro
        self.data = data
        self.company = company
        self.type_avio = t_avio
        self.origen = origen
        self.desti = desti


