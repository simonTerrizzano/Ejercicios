def pricipal():
	def IngreseNum():
		num=0
		lista=[]
		for i in range(0,10):
			num=int(input("Ingrese un numero: "))
			lista.append(num)
		
		return lista
	def sumNum(list):
		listaSumados=[]
		for i in range(0,10):
			suma=0
			numChar=str(lista[i])
			for j in range(0,len(numChar)):
				suma=suma+int(numChar[j])
			listaSumados.append(suma)
		return listaSumados
	def buscarMay(listaSumados):
		may=listaSumados[0]
		for i in range(1,10):
			if listaSumados[i] > may:
				may=listaSumados[i]
				pos=i+1
		print("La posicion del numero que la suma de sus digitos es mayor es: " + str(pos))

	lista=IngreseNum()
	listaSumados=sumNum(lista)
	buscarMay(listaSumados)
pricipal()