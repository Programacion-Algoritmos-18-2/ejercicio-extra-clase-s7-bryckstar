class OrdenamientoInsercion(): 

    def __init__(self, datos): 
        self.datos = datos 

    def agregarInformacion(self, datos): 
        self.datos = datos

    def ordenar(self,datos): 
        insercion = 0  
        for i in range(1, len(self.datos)): 
            insercion = self.datos[i]
            posicion = i 

            while posicion > 0 and self.datos[posicion - 1] > insercion: 
                self.datos[posicion] = self.datos[posicion - 1] 
                posicion = posicion - 1 

            self.datos[posicion] = insercion 

            print(self.__str__()) 
        print("El arreglo ordenado es el siguiente:\n") 
        print(self.__str__()) 


    def imprimirPasada(self, pasada, indice): 
        print("despues de pasada %2d:", pasada)

        for i in range (0,indice):    
            print(self.datos[i] + " ")

        print(self.datos[i] + "* ") 

        for i in range(indice + 1, len(self.datos)): 
            print(self.datos[i] + " ")
        print("") 
        
        for i in range(0, pasada): 
            print("--------------")
        print(" ")

    

    def __str__(self):
        cadena = " " 
        for elemento in self.datos: 
            cadena = "%s %s" % (cadena, elemento)

        cadena = "%s%s\n" % (cadena, "\n") 

        return cadena 