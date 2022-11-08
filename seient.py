'''
title: Definicion del la clase Seient

Autor: Erick Cruz Cedeño
'''
#Representa los asientos que tiene cada vuelo con su fila y letra
class Seient():    #Definicion de Clase Seient  que reresenta, Asientos del vuelo
    #Atributos de Seient, compartidos por todas las instancias
    fila=None
    lletra=None

    #Metodos de Asiento

    def __str__(self):  #redefine la cadena a imprimir del objeto
        c = "Seient: "+str(self.fila)+str(self.lletra)
        return c

    def pintaDades(self):   # imprime los asientos introducidos
        print("fila:",self.fila, end=" ")  #(end=" "), esto nos permite que el siguiente print se realize en la misma linea
        print("lletra:",self.lletra)

    def inicialitzaTeclat(self):    #metodo para que el usuario introduzca los atributos del asiento
        self.fila=(str(input("Inserta fila: ")))
        self.lletra=(str(input("Inserta lletra: "))).upper()    #upper transforma el str en cadenas mayusculas

    # en la consulta sql se obtendran asientos, que se guardaran como objetos seient, se  pasa por argumento la fila y letra
    def readBBDD(self,fila,lletra):
        self.fila = fila            #asignamos cada atributo con su parametro
        self.lletra = lletra
