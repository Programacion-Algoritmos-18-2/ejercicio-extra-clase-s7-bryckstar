class OrdenamientoSeleccion: 

	def __init__(self, datos):
		self.datos = datos 

	def agregarInformacion(self, datos): 
		self.datos = datos

	def ordenar(self, datos): 
		
		for i in range(len(self.datos)): 
			masPequenio = i 
			for j in range(i + 1, len(self.datos)): 
				if(self.datos[j] < self.datos[i]): 
					masPequenio = j 

			
			if masPequenio != i: 
				temporal = self.datos[i] 
				self.datos[i] = self.datos[masPequenio] 
				self.datos[masPequenio] = temporal 
		
		print(self.__str__())


	def __str__(self):
		
		cadena = " " 

		for elemento in self.datos:
			cadena = "%s %s" % (cadena, elemento)

		cadena = "%s\n" % (cadena) 
		print("El arreglo ordenado es el siguiente:")

		return cadena
		 