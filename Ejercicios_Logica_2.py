def esPrimo(num):
	if num < 2:
		return False
	elif num == 2:
		return True
	else:

		for x in range(2,num):
			if num % x == 0:
				return False
		return True
def esMultiplo(num1, num2):
	if num1 % num2 == 0:
		return True
	else:
		return False
def esPar(num):
	if num % 2 == 0:
		return True
	else:
		return False
def esDivisorExacto(num1,num2):
	if num1 % num2 == 0:
		return True
	else:
		return False
# --------------------------------------------------
# Ejercicio 1
def ultimo4():

	"""Funcion que nos devuelve si un numero termina en 4"""

	while True:

		try:
			num=int(input("Ingrese un numero: "))
			break
		except ValueError:
			print("Error! \nNo ha ingresado un numero.")

	if str(num)[-1] == "4":
		print("El ultimo digito del numero {} es igual a 4".format(num))
	else:
		print("El ultimo digito del numero {} es diferente a 4".format(num))

# --------------------------------------------------

# Ejercicio 2

def suma2digitos():

	"""Funcion que nos devuelve la suma de los digitos de un numero de 2 digitos"""

	while True:

		try:
			num=int(input("Ingrese un numero de 2 digitos: "))
			break
		except ValueError:
			print("Error! \nNo ha ingresado un numero.")

	while True:
		if len(str(num)) != 2:
			print("Error! \nNo ha ingresado un numero.")
			num=int(input("Ingrese un numero de 2 digitos: "))
		else:
			break

	dig1=int(str(num)[0])
	dig2=int(str(num)[1])
	res= numChar1 + numChar2
	print("La suma de los 2 digitos de {} es {}".format(num,res))

# --------------------------------------------------

# Ejercicio 3


def esNegativo():

	"""Funcion que nos devuelve si un numero es negativo"""

	while True:

		try:
			num=int(input("Ingrese un numero: "))
			break
		except ValueError:
			print("Error! \nNo ha ingresado un numero.")

	if num < 0:
		print("El numero {} es negativo".format(num))
	else:
		print("El numero {} no es negativo".format(num))

# --------------------------------------------------

# Ejercicio 4

def tiene3digitos():

	"""Funcion que nos devuelve si un numero tiene 3 digitos"""

	while True:

		try:
			num=int(input("Ingrese un numero: "))
			break
		except ValueError:
			print("Error! \nNo ha ingresado un numero.")

	if len(str(num)) == 3:
		print("El numero {} tiene 3 digitos".format(num))
	else:
		print("El numero {} no tiene 3 digitos".format(num))

# --------------------------------------------------

# Ejercicio 5

def numEsPar():

	"""Funcion que nos devuelve si un numero es par"""

	while True:

		try:
			num=int(input("Ingrese un numero: "))
			break
		except ValueError:
			print("Error! \nNo ha ingresado un numero.")

	if esPar(num):
		print("El numero {} es par".format(num))
	else:
		print("El numero {} es impar".format(num))

# --------------------------------------------------

# Ejercicio 6

def numPrimo():


	"""Funcion que nos devuelve si un numero es primo"""

	while True:

		try:
			num=int(input("Ingrese un numero: "))
			break
		except ValueError:
			print("Error! \nNo ha ingresado un numero.")

	if esPrimo(num):
		print("El numero {} es primo".format(num))
	else:
		print("El numero {} no es primo".format(num))	

# --------------------------------------------------

# Ejercicio 7

def negYprimo(num):

	"""Funcion que nos devuelve si un numero es negativo o primo"""

	while True:
		try:
			num=int(input("Ingrese un numero: "))
			break
		except ValueError:
			print("Error! \nNo ha ingresado un numero.")

	if num < 0:									
		print("El numero {} es negativo".format(num))
	else:
		print("El numero {} no es negativo".format(num))

	if esPrimo(num) == True:
		print("El numero {} es primo".format(num))
	else:
		print("El numero {} no es primo".format(num))	

# --------------------------------------------------

# Ejercicio 8

def dig2Primo():

	"""Funcion que nos devuelve si un digito de un numero de 2 digitos es primo o  no"""

	while True:

		try:
			num=int(input("Ingrese un numero: "))
			break
		except ValueError:
			print("Error! \nNo ha ingresado un numero.")


	while True:
		if len(str(num)) != 2:
			print("Error! \nNo ha ingresado un numero.")
			num=int(input("Ingrese un numero de 2 digitos: "))
		else:
			break


	dig1=int(str(num)[0])
	dig2=int(str(num)[1])

	if esPrimo(dig1):
		print("El numero {} es primo".format(dig1))
	else:
		print("El numero {} no es primo".format(dig1))	
	if esPrimo(dig2):
		print("El numero {} es primo".format(dig2))
	else:
		print("El numero {} no es primo".format(dig2))
# --------------------------------------------------

# Ejercicio 9

def dig2Multiplo():

	"""Funcion que nos devuelve si un digito de un numero de 2 digitos es multiplo del otro o  no"""

	while True:

		try:
			num=int(input("Ingrese un numero: "))
			break
		except ValueError:
			print("Error! \nNo ha ingresado un numero.")


	while True:
		if len(str(num)) != 2:
			print("Error! \nNo ha ingresado un numero.")
			num=int(input("Ingrese un numero de 2 digitos: "))
		else:
			break


	dig1=int(str(num)[0])
	dig2=int(str(num)[1])

	try:
		if esMultiplo(int(dig1), int(dig2)):
			print("{} es multiplo de {}".format(dig1,dig2))
		else:
			print("{} no es multiplo de {}".format(dig1,dig2))
	except ZeroDivisionError:
		print("{} no es multiplo de {}".format(dig1,dig2))

	if esMultiplo(dig2, dig1):
		print("{} es multiplo de {}".format(dig2,dig1))
	else:
		print("{} no es multiplo de {}".format(dig2,dig1))

# --------------------------------------------------

# Ejercicio 10

def digDif():

	"""Funcion que nos devuelve si un digito de un numero de 2 digitos igual al otro o no"""

	while True:

		try:
			num=int(input("Ingrese un numero: "))
			break
		except ValueError:
			print("Error! \nNo ha ingresado un numero.")

	while True:
		if len(str(num)) != 2:
			print("Error! \nNo ha ingresado un numero.")
			num=int(input("Ingrese un numero de 2 digitos: "))
		else:
			break

	dig1=int(str(num)[0])
	dig2=int(str(num)[1])


	if dig1 == dig2:
		print("{} es igual a {}".format(dig1,dig2))
	else:
		print("{} es no igual a {}".format(dig1,dig2))

# --------------------------------------------------

# Ejercicio 10


def numMayMen():

	"""Funcion que nos devuelve si un numero igual o mayor otro"""

	while True:

		try:
			num1=int(input("Ingrese un numero: "))
			break
		except ValueError:
			print("Error! \nNo ha ingresado un numero.")

	while True:

		try:
			num2=int(input("Otro un numero: "))
			break
		except ValueError:
			print("Error! \nNo ha ingresado un numero.")


	if num1 == num2:
		print("{} es igual a {}".format(num1,num2))
	elif num1 > num2:
		print("{} es mayor a {}".format(num1,num2))
	else:
		print("{} es mayor a {}".format(num2,num1))

# --------------------------------------------------

# Ejercicio 12

def num2Coinciden():

	"""Funcion que nos devuelve si algun digito de 2 numeros de 2 digitos tienen alguna coincidencia"""

	while True:

		try:
			num=int(input("Ingrese un numero: "))
			break
		except ValueError:
			print("Error! \nNo ha ingresado un numero.")


	while True:
		if len(str(num)) != 2:
			print("Error! \nNo ha ingresado un numero.")
			num=int(input("Ingrese un numero de 2 digitos: "))
		else:
			break

	dig1=str(num)[0]
	dig2=str(num)[1]

	while True:

		try:
			num2=int(input("Ingrese un numero: "))
			break
		except ValueError:
			print("Error! \nNo ha ingresado un numero.")


	while True:
		if len(str(num)) != 2:
			print("Error! \nNo ha ingresado un numero.")
			num=int(input("Ingrese un numero de 2 digitos: "))
		else:
			break


	dig3=str(num2)[0]
	dig4=str(num2)[1]

	if dig1 == dig3 or dig1 == dig4 or dig2 == dig3 or dig2 == dig4:
		print("El numero {} tiene digitos comunes con ".format(num,num2))
	else:
		print("El numero {} no tiene digitos comunes con el numero ".format(num,num2))

# --------------------------------------------------

# Ejercicio 13

def num2esPar():

	"""Funcion que nos devuelve si el resultado de la suma de numeros es par o impar"""

	while True:

		try:
			num=int(input("Ingrese un numero: "))
			break
		except ValueError:
			print("Error! \nNo ha ingresado un numero.")

	while True:

		try:
			num2=int(input("Ingrese un numero: "))
			break
		except ValueError:
			print("Error! \nNo ha ingresado un numero.")

	if esPar(num+num2):
		print("El numero {} es par".format(res))
	else:
		print("El numero {} es impar".format(res))
# --------------------------------------------------

# Ejercicio 14

def sumaTodosDigitos():

	"""Funcion que nos devuelve la suma de los digitos 2 numeros de 2 digitos tienen alguna coincidencia"""

	while True:

		try:
			num=int(input("Ingrese un numero: "))
			break
		except ValueError:
			print("Error! \nNo ha ingresado un numero.")


	while True:
		if len(str(num)) != 2:
			print("Error! \nNo ha ingresado un numero.")
			num=int(input("Ingrese un numero de 2 digitos: "))
		else:
			break


	dig1=int(str(num)[0])
	dig2=int(str(num)[1])

	while True:

		try:
			num2=int(input("Ingrese un numero: "))
			break
		except ValueError:
			print("Error! \nNo ha ingresado un numero.")


	while True:
		if len(str(num)) != 2:
			print("Error! \nNo ha ingresado un numero.")
			num=int(input("Ingrese un numero de 2 digitos: "))
		else:
			break


	dig3=int(str(num2)[0])
	dig4=int(str(num2)[1])

	res=dig1+dig2+dig3+dig4

	print("La suma de todos los digitos es: {}".format(res))

# --------------------------------------------------


def suma3digitos():

	"""Funcion que nos devuelve la suma de los digitos de un numero de 2 digitos"""

	while True:

		try:
			num=int(input("Ingrese un numero de 3 digitos: "))
			break
		except ValueError:
			print("Error! \nNo ha ingresado un numero.")

	while True:
		if len(str(num)) != 3:
			print("Error! \nNo ha ingresado un numero.")
			num=int(input("Ingrese un numero de 3 digitos: "))
		else:
			break

	dig1=int(str(num)[0])
	dig2=int(str(num)[1])
	dig3=int(str(num)[2])
	res= dig1 + dig2 + dig3  
	print("La suma de los 3 digitos de {} es {}".format(num,res))

# --------------------------------------------------

# Ejercicio 16

def comun3digitos():

	"""Funcion que nos devuelve si un numero tiene coinsidencias entre sus digitos"""

	while True:

		try:
			num=int(input("Ingrese un numero de 3 digitos: "))
			break
		except ValueError:
			print("Error! \nNo ha ingresado un numero.")

	while True:
		if len(str(num)) != 3:
			print("Error! \nNo ha ingresado un numero.")
			num=int(input("Ingrese un numero de 3 digitos: "))
		else:
			break

	dig1=str(num)[0]
	dig2=str(num)[1]
	dig3=str(num)[2]

	if dig1 == dig2 or dig1 == dig3 or dig2 == dig3:
		print("El numero {} coincide en al menos 1 digito".format(num))
	else:
		print("El numero {} no coincide en ningun numero".format(num))

# --------------------------------------------------

# Ejercicio 17

def mayor3digitos():

	"""Funcion que nos devuelve la posicion de el digito mayor de un numero de 3 cifras"""

	while True:

		try:
			num=int(input("Ingrese un numero de 3 digitos: "))
			break
		except ValueError:
			print("Error! \nNo ha ingresado un numero.")

	while True:
		if len(str(num)) != 3:
			print("Error! \nNo ha ingresado un numero.")
			num=int(input("Ingrese un numero de 3 digitos: "))
		else:
			break

	dig1=int(str(num)[0])
	dig2=int(str(num)[1])
	dig3=int(str(num)[2])
	if dig1 == dig2 and dig1 == dig3:
		print("Los 3 digitos son iguales")
	elif dig1 > dig2 and dig1 > dig3:
		print("El mayor digito esta en la posicion 1")
	elif dig2 > dig1 and dig2 > dig3:
		print("El mayor digito esta en la posicion 2")
	else:
		print("El mayor digito esta en la posicion 3")

# --------------------------------------------------

# Ejercicio 18

def multiplo3digitos():

	"""Funcion que nos devuelve si que los digitos de un numero de 3 digitos son multiplos"""

	while True:

		try:
			num=int(input("Ingrese un numero de 3 digitos: "))
			break
		except ValueError:
			print("Error! \nNo ha ingresado un numero.")

	while True:
		if len(str(num)) != 3:
			print("Error! \nNo ha ingresado un numero.")
			num=int(input("Ingrese un numero de 3 digitos: "))
		else:
			break

	num1=int(str(num)[0])
	num2=int(str(num)[1])
	num3=int(str(num)[2])
	try:
		if esMultiplo(num1, num2):
			print("{} es multiplo de {}".format(num1, num2))
		else:
			print("{} no es multiplo de {}".format(num1, num2))
	except ZeroDivisionError:
		print("{} no es multiplo de {}".format(num1, num2))

	try:
		if esMultiplo(num1, num3):
			print("{} es multiplo de {}".format(num1, num3))
		else:
			print("{} no es multiplo de {}".format(num1, num3))
	except ZeroDivisionError:
		print("{} no es multiplo de {}".format(num1, num3))


	if esMultiplo(num2, num1):
		print("{} es multiplo de {}".format(num2, num1))
	else:
		print("{} no es multiplo de {}".format(num2, num1))

	try:
		if esMultiplo(num2, num3):
			print("{} es multiplo de {}".format(num2, num3))
		else:
			print("{} no es multiplo de {}".format(num2, num3))
	except ZeroDivisionError:
		print("{} no es multiplo de {}".format(num2, num3))

	if esMultiplo(num3, num1):
		print("{} es multiplo de {}".format(num3, num1))
	else:
		print("{} no es multiplo de {}".format(num3, num1))

	try:
		if esMultiplo(num3, num2):
			print("{} es multiplo de {}".format(num3, num2))
		else:
			print("{} no es multiplo de {}".format(num3, num2))
	except ZeroDivisionError:
		print("{} no es multiplo de {}".format(num3, num2))

# --------------------------------------------------

# Ejercicio 19


def mayor3Num():

	"""Funcion que nos devuelve mayor de 3 numeros pero usando 2 variables"""

	while True:

		try:
			num1=int(input("Ingrese el 1er numero: "))
			break
		except ValueError:
			print("Error! \nNo ha ingresado un numero.")

	while True:

		try:
			num2=int(input("Ingrese el 2do numero: "))
			break
		except ValueError:
			print("Error! \nNo ha ingresado un numero.")


	if num1 == num2:
		while True:

			try:
				num2=int(input("Ingrese el 3er numero: "))
				break
			except ValueError:
				print("Error! \nNo ha ingresado un numero.")

		if num1 == num2:
			print("Todos los numeros son iguales")
		elif num1 > num2:
			print("El numero {} es el mayor de los 3".format(num1))
		else:
			print("El numero {} es el mayor de los 3".format(num2))
	if num1 > num2:
		while True:

			try:
				num2=int(input("Ingrese el 3er numero: "))
				break
			except ValueError:
				print("Error! \nNo ha ingresado un numero.")
		if num1 > num2:
			print("El numero {} es el mayor de los 3".format(num1))
		else:
			print("El numero {} es el mayor de los 3".format(num1))
	if num2 > num1:
		while True:

			try:
				num2=int(input("Ingrese el 3er numero: "))
				break
			except ValueError:
				print("Error! \nNo ha ingresado un numero.")
		if num2 > num1:
			print("El numero {} es el mayor de los 3".format(num2))
		else:
			print("El numero {} es el mayor de los 3".format(num1))

# --------------------------------------------------

# Ejercicio 20



def orden3Num():

	"""Funcion que nos devuelve 3 numeros ingresados ordenados de mayor a menor"""

	while True:

		try:
			num1=int(input("Ingrese el 1er numero: "))
			break
		except ValueError:
			print("Error! \nNo ha ingresado un numero.")

	while True:

		try:
			num2=int(input("Ingrese el 2do numero: "))
			break
		except ValueError:
			print("Error! \nNo ha ingresado un numero.")

	while True:

		try:
			num3=int(input("Ingrese el 3er numero: "))
			break
		except ValueError:
			print("Error! \nNo ha ingresado un numero.")

	if num1 == num2 and num1 == num3:
		print(num1)
		print(num2)
		print(num3)
	if num1 > num2 and num1 == num3:
		print(num1)
		print(num3)
		print(num2)
	if num1 > num3 and num1 == num2:
		print(num1)
		print(num2)
		print(num3)
	if num2 > num1 and num2 == num3:
		print(num2)
		print(num3)
		print(num1)
	if num1 > num2 and num1 > num3:
		print(num1)
		if num2 > num3:
			print(num2)
			print(num3)
		else:
			print(num3)
			print(num2)
	if num2 > num1 and num2 > num3:
		print(num2)
		if num1 > num3:
			print(num1)
			print(num3)
		else:
			print(num3)
			print(num1)
	if num3 > num2 and num3 > num1:
		print(num3)
		if num2 > num1:
			print(num2)
			print(num1)
		else:
			print(num1)
			print(num2)

# --------------------------------------------------

# Ejercicio 21

# num1=22

# numChar=str(num1)
# num1Char=numChar[0]
# num2Char=numChar[1]

# num2=32

# numChar2=str(num2)
# num3Char=numChar2[0]
# num4Char=numChar2[1]

# num3=89

# numChar3=str(num3)
# num5Char=numChar3[0]
# num6Char=numChar3[1]


# dig1=int(num1Char)
# dig2=int(num2Char)
# dig3=int(num3Char)
# dig4=int(num4Char)
# dig5=int(num5Char)
# dig6=int(num6Char)

# digitos=[dig1,dig2,dig3,dig4,dig5,dig6]
# may=0
# con=0
# while con <= 5:
# 	if digitos[con]==dig1:
# 		may=digitos[con]
# 	elif digitos[con]>may:
# 		may=digitos[con]
# 	elif digitos[con]>may:
# 		may=may
# 	con=con+1
# print("El mayor digito es : " + str(may))

# --------------------------------------------------

# Ejercicio 22

# num="339"

# if num[0]==num[2]:
# 	print("El 1er digito es igual al ultimo")
# else:
# 	print("El 1er digito es diferente al ultimo")

# --------------------------------------------------

# Ejercicio 23

# num=267

# numChar=str(num)
# numChar1=numChar[0]
# numChar2=numChar[1]
# numChar3=numChar[2]

# num1=int(numChar1)
# num2=int(numChar2)
# num3=int(numChar3)

# def esprimo(num):
# 	if num < 2:
# 		return False
# 	elif num == 2:
# 		return True
# 	else:

# 		for x in range(2,num):
# 			if num % x == 0:
# 				return False
# 		return True
# cont=0
# if esprimo(num1) == True:
# 	cont=cont+1
# if esprimo(num2) == True:
# 	cont=cont+1
# if esprimo(num3) == True:
# 	cont=cont+1
# print("El numero tiene " + str(cont) + " digito/s primo/s")

# --------------------------------------------------

# Ejercicio 24

# num=201

# numChar=str(num)
# numChar1=numChar[0]
# numChar2=numChar[1]
# numChar3=numChar[2]

# num1=int(numChar1)
# num2=int(numChar2)
# num3=int(numChar3)

# def espar(num):
# 	if num % 2 == 0:
# 		return True
# 	else:
# 		return False
# cont=0
# if espar(num1) == True:
# 	cont = cont+1

# if espar(num2) == True:
# 	cont = cont+1

# if espar(num3) == True:
# 	cont = cont+1
# print("El numero tiene " + str(cont) + " digitos pares")


# --------------------------------------------------

# Ejercicio 25

# def sumaEntreDigitos():
# 	num=int(input("Ingrese un numero: "))
# 	numChar=str(num)

# 	num1=int(numChar[0])
# 	num2=int(numChar[1])
# 	num3=int(numChar[2])

# 	if num1 + num2 == num3:
# 		return True
# 	if num2 + num3 == num1:
# 		return True
# 	if num1 + num3 == num2:
# 		return True
# if sumaEntreDigitos() == True:
# 	print("La suma de 2 digitos es igual a otro de los digitos")

# --------------------------------------------------

# Ejercicio 26

# num=int(input("Ingrese un numero: "))

# numChar=str(num)

# num1=numChar[0]
# num2=numChar[1]
# num3=numChar[2]
# num4=numChar[3]

# res = num1 + num2 + num3 + num4

# print("Esl resultado de la suma de los digitos es " + str(res))

# --------------------------------------------------

# Ejercicio 27

# num=2019

# numChar=str(num)
# numChar1=numChar[0]
# numChar2=numChar[1]
# numChar3=numChar[2]
# numChar4=numChar[3]

# num1=int(numChar1)
# num2=int(numChar2)
# num3=int(numChar3)
# num4=int(numChar4)

# def espar(num):
# 	if num % 2 == 0:
# 		return True
# 	else:
# 		return False
# cont=0
# if espar(num1) == True:
# 	cont = cont+1

# if espar(num2) == True:
# 	cont = cont+1

# if espar(num3) == True:
# 	cont = cont+1

# if espar(num4) == True:
# 	cont = cont+1
# print("El numero tiene " + str(cont) + " digitos pares")

# --------------------------------------------------

# Ejercicio 28

# def esprimo(num):
# 	if num < 2:
# 		return False
# 	elif num == 2:
# 		return True
# 	else:

# 		for x in range(2,num):
# 			if num % x == 0:
# 				return False
# 		return True
# num= int(input("Ingrese un numero: "))
# while num >= 0 and num < 50:
# 	if esprimo(num) == True:
# 		print("El numero es primo")
# 	else:
# 		print("El numero no es primo")
# 	num=num*(-1)
# print("El numero esta fuera del rango")

# --------------------------------------------------

# Ejercicio 29

# num=88780

# numChar=str(num)

# if numChar[0] == numChar[-1] and numChar[1] == numChar[-2]:
# 	print("El numero es capicua")
# else:
# 	print("El numero no es capicua")

# --------------------------------------------------

# Ejercicio 30

# num=8880

# numChar=str(num)

# if numChar[1] == numChar[-2]:
# 	print("El 2do digito es igual al penultimo")
# else:
# 	print("El 2do digito es difirente al penultimo")

# --------------------------------------------------

# Ejercicio 31

# num=int(input("Ingrese un numero: "))

# if num == 10:
# 	print("El numero es igual a 10")
# else:
# 	print("El numero no es igual a 10")

# --------------------------------------------------

# Ejercicio 32

# num=int(input("Ingrese un numero: "))

# if num % 7 == 0:
# 	print("El numero " + str(num) + " es multiplo de 7")
# else:
# 	print("El numero " + str(num) + " no es multiplo de 7")

# --------------------------------------------------

# Ejercicio 33

# num=int(input("Ingrese un numero: "))

# numChar=str(num)

# if int(numChar[-1]) == 7:
# 	print("El ultimo digito de " + numChar + " es 7")
# else:
# 	print("El ultimo digito de " + numChar + " no es 7")

# --------------------------------------------------

# Ejercicio 34

# num=int(input("Ingrese un numero menor a 1000: "))
# numChar = str(num)
# if num < 1000:
# 	print("El numero " + numChar + " tiene " + str(len(numChar)) + " digito/s")
# else:
# 	print("El numero " + numChar + " esta fuera del rango")

# --------------------------------------------------

# Ejercicio 35

# num=int(input("Ingrese un numero de 2 digitos: "))

# numChar=str(num)

# dig1=numChar[0]
# dig2=numChar[1]

# print("El 1er digito es " + dig1)
# print("El 2do digito es " + dig2)

# --------------------------------------------------

# Ejercicio 36

# num=int(input("Ingrese un numero de 4 digitos: "))

# numChar = str(num)

# dig1=numChar[0]
# dig2=numChar[1]
# dig3=numChar[2]
# dig4=numChar[3]

# def espar(num):
# 	if num % 2 == 0:
# 		return True
# 	else:
# 		return False
# contpar=0
# contimpar=0
# if espar(int(dig1)) == True:
# 	contpar = contpar+1
# elif espar(int(dig1)) == False:
# 	contimpar = contimpar+1

# if espar(int(dig2)) == True:
# 	contpar = contpar+1
# elif espar(int(dig2)) == False:
# 	contimpar = contimpar+1

# if espar(int(dig3)) == True:
# 	contpar = contpar+1
# elif espar(int(dig3)) == False:
# 	contimpar = contimpar+1

# if espar(int(dig4)) == True:
# 	contpar = contpar+1
# elif espar(int(dig4)) == False:
# 	contimpar = contimpar+1

# if contpar == contimpar:
# 	print("El numero " + numChar + " tiene igual cantidad de digitos pares que impares")

# elif contpar > contimpar:
# 	print("El numero " + numChar + " tiene mayor cantidad de digitos pares que impares")
# elif contimpar > contpar:
# 	print("El numero " + numChar + " tiene mayor cantidad de digitos impares que pares")

# --------------------------------------------------

# Ejercicio 37

# num1=int(input("Ingrese un numero: "))
# num2=int(input("Ingrese un numero: "))
# try:
# 	if num1 % num2 == 0:
# 		print(str(num1) + " es multiplo de " + str(num2))
# except ZeroDivisionError:
# 	print("0 no tiene multiplos")
# try:
# 	if num2 % num1 == 0:
# 		print(str(num2) + " es multiplo de " + str(num1))
# except ZeroDivisionError:
# 	print("0 no tiene multiplos")

# --------------------------------------------------

# Ejercicio 38

# num1=str(input("Ingrese un numero: "))
# num2=str(input("Ingrese un numero: "))
# num3=str(input("Ingrese un numero: "))

# if num1[-1] == num2[-1] and num1[-1] == num3[-1]:
# 	print("Los ultimos digitos de los 3 numeros ingresados son iguales")
# else:
# 	print("Los ultimos digitos de los 3 numeros ingresados no son iguales")

# --------------------------------------------------

# Ejercicio 39

# num1=str(input("Ingrese un numero: "))
# num2=str(input("Ingrese un numero: "))
# num3=str(input("Ingrese un numero: "))

# if num1[-2] == num2[-2] and num1[-2] == num3[-2]:
# 	print("Los penultimos digitos de los 3 numeros ingresados son iguales")
# else:
# 	print("Los penultimos digitos de los 3 numeros ingresados no son iguales")

# --------------------------------------------------

# Ejercicio 40

# num1=int(input("Ingrese un numero: "))
# num2=int(input("Ingrese un numero: "))

# res = num1 - num2
# may = num1
# men = num2

# if res < 0:
# 	res = num2 - num1
# 	may = num2
# 	men = num1

# if res <= 10:
# 	for i in range(men,may):
# 		print(i+1)
# else:
# 	print("La diferencia es mayor a 10")

# --------------------------------------------------

# Ejercicio 41

# num1=int(input("Ingrese un numero: "))
# num2=int(input("Ingrese un numero: "))
# def esprimo(num):
# 	if num < 2:
# 		return False
# 	elif num == 2:
# 		return True
# 	else:

# 		for x in range(2,num):
# 			if num % x == 0:
# 				return False
# 		return True

# res = num1 - num2

# if res < 0:
# 	res = num2 - num1

# if esprimo(res) == True:
# 	print("La diferencia entre " + str(num1) + " y " + str(num2) + " es un numero primo")
# else:
# 	print("La diferencia entre " + str(num1) + " y " + str(num2) + " no es un numero primo")

# --------------------------------------------------

# Ejercicio 42

# num1=int(input("Ingrese un numero: "))
# num2=int(input("Ingrese un numero: "))
# def espar(num):
# 	if num % 2 == 0:
# 		return True
# 	else:
# 		return False

# res = num1 - num2

# if res < 0:
# 	res = num2 - num1

# if espar(res) == True:
# 	print("La diferencia entre " + str(num1) + " y " + str(num2) + " es un numero par")
# else:
# 	print("La diferencia entre " + str(num1) + " y " + str(num2) + " no es un numero par")

# --------------------------------------------------

# Ejercicio 43

# num1=int(input("Ingrese un numero: "))
# num2=int(input("Ingrese un numero: "))

# res = num1 - num2

# if res < 0:
# 	res = num2 - num1

# if num1 % res == 0:
# 	print("La diferencia entre " + str(num1) + " y " + str(num2) + " es un divisor exacto de " + str(num1))
# if num2 % res == 0:
# 	print("La diferencia entre " + str(num1) + " y " + str(num2) + " es un divisor exacto de " + str(num2))

# --------------------------------------------------

# Ejercicio 44

# num=str(input("Ingrese un numero de cuatro digitos: "))

# dig=int(num[0])

# for i in range(1,4):
# 	if int(num[i]) % dig == 0:
# 		print(str(dig) + " es multiplo de " + num[i])
# 	else:
# 		print(str(dig) + " no es multiplo de " + num[i])

# --------------------------------------------------

# Ejercicio 45

# num=int(input("Ingrese un numero de dos digitos: "))

# numChar=str(num)

# res=0

# def esprimo(num):
# 	if num < 2:
# 		return False
# 	elif num == 2:
# 		return True
# 	else:

# 		for x in range(2,num):
# 			if num % x == 0:
# 				return False
# 		return True

# if num % 2 == 0:
# 	res=int(numChar[0]) + int(numChar[1])
# 	print(res)
# if esprimo(num) == True and num < 10:
# 	print(numChar[1])
# if num % 5 == 0 and num < 30:
# 	print(numChar[0])

# --------------------------------------------------

# Ejercicio 46

# num=int(input("Ingrese un numero de dos digitos: "))

# numChar=str(num)

# res=0

# if int(numChar[1]) == 1:
# 	print(numChar[0])
# if int(numChar[1])== 2:
# 	res=int(numChar[0]) + int(numChar[1])
# 	print(res)
# if int(numChar[1]) == 3:
# 	res=int(numChar[0]) * int(numChar[1])
# 	print(res)

# --------------------------------------------------

# Ejercicio 47

# num1=str(input("Ingrese un numero de dos digitos: "))
# num2=str(input("Ingrese un numero de dos digitos: "))

# dig1=num1[0]
# dig2=num1[1]
# dig3=num2[0]
# dig4=num2[1]
# dif=0
# res=0




# def esprimo(num):
# 	if num < 2:
# 		return False
# 	elif num == 2:
# 		return True
# 	else:

# 		for x in range(2,num):
# 			if num % x == 0:
# 				return False
# 		return True

# dif = int(num1) - int(num2)

# if dif < 0:
# 	dif = int(num2) - int(num1)
# difChar=str(dif)

# if dif % 2 == 0:
# 	res=int(dig1)+int(dig2)+int(dig3)+int(dig4)
# 	print(res)
# elif esprimo(dif) == True and dif < 10:
# 	print(int(num2) * int(num1))
# if difChar[-1] == '4':
# 	print(dig1)
# 	print(dig2)
# 	print(dig3)
# 	print(dig4)

# --------------------------------------------------

# Ejercicio 48

# def esprimo(num):
# 	if num < 2:
# 		return False
# 	elif num == 2:
# 		return True
# 	else:

# 		for x in range(2,num):
# 			if num % x == 0:
# 				return False
# 		return True


# num=int(input("Ingrese un numero menor a 100: "))
# if num >=100:
# 	while num >= 100:
# 		print("Numero mayor a 100")
# 		num=int(input("Ingrese un numero menor a 100: "))

# if esprimo(num) == True:
# 	print("El numero " + str(num) + " es primo")
# else:
# 	print("El numero " + str(num) + " no es primo")

# --------------------------------------------------

# Ejercicio 49

# def esprimo(num):
# 	if num < 2:
# 		return False
# 	elif num == 2:
# 		return True
# 	else:

# 		for x in range(2,num):
# 			if num % x == 0:
# 				return False
# 		return True


# num=int(input("Ingrese un numero: "))

# numChar=str(num)

# if num % 4 == 0:
# 	if esprimo(int(numChar[-1])) == True:
# 		print("El numero " + numChar[-1] + " es primo")
# 	else:
# 		print("El numero " + numChar[-1] + " no es primo")

# --------------------------------------------------

# Ejercicio 50

# num=int(input("Ingrese un numero: "))

# numChar=str(num)

# if num % 4 == 0:
# 	print(num/2)
# if num % 5 == 0:
# 	print(num*num)
# if num % 6 == 0:
# 	print(numChar[0])

# ________________[Final de ejercicios de las paginas 137, 138, 139 y 140]________________

# Ejercicio 1

# num=int(input("Ingrese un numero: "))

# for i in range(1,num):
# 	print(i)

# --------------------------------------------------

# Ejercicio 2

# num=int(input("Ingrese un numero: "))

# for i in range(1,num):
# 	if i % 2 == 0:
# 		print(i)

# --------------------------------------------------

# Ejercicio 3

# num=int(input("Ingrese un numero: "))

# for i in range(1,num):
# 	if num % i == 0:
# 		print(i) 

# --------------------------------------------------

# Ejercicio 4

# num1=int(input("Ingrese un numero: "))
# num2=int(input("Ingrese un numero: "))

# res = num1 - num2
# may = num1
# men = num2

# if res < 0:
# 	may = num2
# 	men = num1


# for i in range(men,may):
# 	print(i)

# --------------------------------------------------

# Ejercicio 5

# num1=int(input("Ingrese un numero: "))
# num2=int(input("Ingrese un numero: "))

# res = num1 - num2
# may = num1
# men = num2

# if res < 0:
# 	may = num2
# 	men = num1

# iChar=''
# for i in range(men,may):
# 	iChar = str(i)
# 	if iChar[-1] == '4':
# 		print(i)

# --------------------------------------------------

# Ejercicio 6

# num=str(input("Ingrese un numero de 3 digitos: "))


# if len(num) == 3:
# 	dig1=int(num[0])
# 	dig2=int(num[1])
# 	dig3=int(num[2])
# 	for i in range(1,dig1):
# 		print(i)

# 	for i in range(1,dig2):
# 		print(i)

# 	for i in range(1,dig3):
# 		print(i)
# else:
# 	print("El numero no tiene 3 cifras")

# --------------------------------------------------

# Ejercicio 7

# for i in range(1,100):
# 	print(i)

# --------------------------------------------------

# Ejercicio 8

# for i in range(20,200):
# 	if i % 2 == 0:
# 		print(i)

# --------------------------------------------------

# Ejercicio 9

# iChar=''
# for i in range(25,205):
# 	iChar = str(i)
# 	if iChar[-1] == '6':
# 		print(i)

# --------------------------------------------------

# Ejercicio 10

# num=int(input("Ingrese un numero: "))

# res=0
# num=num+1
# for i in range(1,num):
# 	res= res+i
# print(res)

# --------------------------------------------------

# Ejercicio 11

# num=str(input("Ingrese un numero: "))

# dig1=int(num[0])
# dig2=int(num[1])

# res = dig1 - dig2
# may = dig1
# men = dig2

# if res < 0:
# 	may = dig2
# 	men = dig1

# for i in range(men,may):
# 	print(i)

# --------------------------------------------------

# Ejercicio 12

# num=str(input("Ingrese un numero de 3 digitos: "))


# if len(num) == 3:
# 	for i in range(0,3):
# 		if num[i] == '1':
# 			print("El digito " + num[i] + " es igual a 1")
# 		else:
# 			print("El digito " + num[i] + " no es igual a 1")
# else:
# 	print("El numero ingresado no es un numero de 3 digitos")

# --------------------------------------------------

# Ejercicio 13

# num=int(input("Ingrese un numero: "))

# for i in range(1,num):
# 	if i % 5 == 0:
# 		print(i)

# --------------------------------------------------

# Ejercicio 14

# for i in range(3,61,3):
# 	print(i)

# --------------------------------------------------

# Ejercicio 15

# res=0

# for i in range(3,61,3):
# 	res = res + i
# print(res)

# --------------------------------------------------

# Ejercicio 16

# num=int(input("Ingrese un numero: "))

# numMul = 1 + num*3
# res=0

# for i in range(3,numMul,3):
# 	res = res + i
# print(res/num)

# --------------------------------------------------

# Ejercicio 17

# numx=int(input("Ingrese un numero: "))
# numy=int(input("Ingrese un numero: "))

# numMulx = 1 + numx*2
# numMuly = 1 + numy*5
# resx = 0
# resy = 0


# for i in range(2,numMulx,2):
# 	resx = resx + i
# for i in range(5,numMuly,5):
# 	resy = resy + i

# resx= resx/numx
# resy= resy/numy

# if resx == resy:
# 	print("El promedio de los 1ros " + str(numx) + " multiplos de 2 es igual a el promedio de los 1ros " + str(numy) + " multiplos de 5")
# if resx > resy:
# 	print("El promedio de los 1ros " + str(numx) + " multiplos de 2 es mayor a el promedio de los 1ros " + str(numy) + " multiplos de 5")
# else:
# 	print("El promedio de los 1ros " + str(numy) + " multiplos de 5 es mayor a el promedio de los 1ros " + str(numx) + " multiplos de 2")	

# --------------------------------------------------

# Ejercicio 18

# num1=int(input("Ingrese un numero: "))
# num2=int(input("Ingrese un numero: "))

# res = num1 - num2
# may = num1
# men = num2

# if res < 0:
# 	may = num2
# 	men = num1

# for i in range(men, may):
# 	if i % 5 == 0:
# 		print(i)

# --------------------------------------------------

# Ejercicio 19

# num=int(input("Ingrese un numero: "))

# if esprimo(num) == True:
# 	print("El numero " + str(num) + " es primo")
# else:
# 	print("El numero " + str(num) + " no es primo")


# --------------------------------------------------

# Ejercicio 20

# num=str(input("Ingrese un numero: "))

# print("El numero tiene " + str(len(num)) + " digito/s")

# --------------------------------------------------

# Ejercicio 21

# num=int(input("Ingrese un numero: "))

# numChar=str(num)
# res=0

# for i in range(0,len(numChar)):

# 	res=res + int(numChar[i])

# print("La suma de los digitos del numero " + str(num) + " es : " + str(res))
	
# --------------------------------------------------

# Ejercicio 22

# num=str(input("Ingrese un numero: "))

# cont=0

# for i in range(0,len(num)):
# 	if num[i] == '1':
# 		cont= cont + 1
# print("El numero " + num + " contiene " + str(cont) + " numero/s 1")

# --------------------------------------------------

# Ejercicio 23

# num=str(input("Ingrese un numero: "))

# res=0

# for i in range(0,len(num)):
# 	res = res + int(num[i])
	
# if esprimo(res) == True:
# 	print("El resultado de la suma de todos los digitos del numero " + num + " es primo")
# else:
# 	print("El resultado de la suma de todos los digitos del numero " + num + " no es primo")

# --------------------------------------------------

# Ejercicio 24

# num=str(input("Ingrese un numero: "))

# res=0

# for i in range(0,len(num)):
# 	if int(num[i]) % 2 == 0:
# 		res = res + int(num[i])

# print("El resultado de la suma de todos los digitos pares del numero " + num + " es : " + str(res))

# --------------------------------------------------

# Ejercicio 25

# num=str(input("Ingrese un numero: "))

# res=0

# for i in range(0,len(num)):
# 	res = res + int(num[i])
# prom= res / len(num)

# print("El promedio de la suma de todos los digitos de " + num + " es " + str(prom))

# --------------------------------------------------

# Ejercicio 26

# num=str(input("Ingrese un numero: "))

# may=int(num[0])

# for i in range(0,len(num)):
# 	if int(num[i]) > may:
# 		may=int(num[i])

# print("El mayor digito del numero " + num + " es " + str(may))

# --------------------------------------------------

# Ejercicio 27

# num1=str(input("Ingrese un numero: "))
# num2=str(input("Ingrese un numero: "))

# if len(num1) == len(num2):
# 	print("El numero " + num1 + " y el numero " + num2 + " tienen la misma cantidad de digitos")
# elif len(num1) > len(num2):
# 	print("El numero " + num1 + " tiene mas digitos que el numero " + num2)
# else:
# 	print("El numero " + num2 + " tiene mas digitos que el numero " + num1)

# --------------------------------------------------

# Ejercicio 28

# numx=str(input("Ingrese un numero: "))
# numy=str(input("Ingrese un numero: "))

# conx=0
# cony=0

# for i in range(0,len(numx)):
# 	if esPrimo(int(numx[i])) == True:
# 		conx= conx + 1
# for i in range(0,len(numy)):
# 	if esPrimo(int(numy[i])) == True:
# 		cony= cony + 1

# if conx == cony:
# 	print("El numero " + numx + " y el numero " + numy + " tienen la misma cantidad de digitos primos")
# elif conx > cony:
# 	print("El numero " + numx + " tiene mas digitos primos que el numero " + numy)
# else:
# 	print("El numero " + numy + " tiene mas digitos primos que el numero " + numx)

# --------------------------------------------------

# Ejercicio 29

# num=str(input("Ingrese un numero: "))

# print("El 1er digito del numero " + num + " es igual a " + num[0])

# --------------------------------------------------

# Ejercicio 30

# num=int(input("Ingrese un numero: "))

# for i in range(1,num):
# 	if num % i == 0:
# 		print(i)

# --------------------------------------------------

# Ejercicio 31

# num=1
# res=0
# cont=0
# numChar=''
# while num != 0:
# 	num=int(input("Ingrese un numero: "))
# 	numChar=str(num)
# 	if numChar[-1] == '5':
# 		res=res + int(num)
# 		cont=cont+1
# res = res/cont
# print("El promedio de los numeros ingresados terminados en 5 es " + str(res))

# --------------------------------------------------

# Ejercicio 32

# num=1
# res=0
# cont=0
# numChar=''
# while num != 0:
# 	num=int(input("Ingrese un numero: "))
# 	if esPrimo(num) == True:
# 		res=res+num
# 		cont=cont+1

# res = res/cont
# res = round(res)
# print("El promedio de los numeros primos ingresados es " + str(res))

# --------------------------------------------------

# Ejercicio 33

# num=32768

# while num !=0:
# 	num= num-1
# 	if esPrimo(num) == True:
# 		print("El numero primo mas cercano a 32768 es: " + str(num))
# 		num=0

# --------------------------------------------------

# Ejercicio 34

# num=11
# for i in range(1,11):
# 	num= num - 1
# 	print(num)

# --------------------------------------------------

# Ejercicio 35

# num1=str(input("Ingrese un numero: "))
# num2=str(input("Ingrese un numero: "))

# res= int(num1[0]) * int(num2[0])

# print("El resultado del producto mutuo del 1er digito de " + num1 + " y " + num2 + " es: " + str(res))

# --------------------------------------------------

# Ejercicio 36

# res=5
# for i in range(1,11):
# 	res=5*i
# 	print("5 * " + str(i)+ "= " + str(res))

# --------------------------------------------------

# Ejercicio 37

# res=0

# for i in range(1,11):
# 	for x in range(1,11):
# 		res = i * x
# 		print(str(i) + "*"+ str(x) + "=" + str(res))

# --------------------------------------------------

# Ejercicio 38

# num=int(input("Ingrese un numero: "))

# res=5
# for i in range(1,11):
# 	res=num*i
# 	print("5 * " + str(i)+ "= " + str(res))

# --------------------------------------------------

# Ejercicio 39

# num1=1
# res=1
# res2=1
# lista=[]

# print('0')
# print(num1)

# while res<=10000:
# 	res2=res
# 	res= res + num1
# 	num1=res2
# 	print(res)
# --------------------------------------------------

# Ejercicio 40

# num=int(input("Ingrese un numero de 2 digitos: "))

# numChar=str(num)
# num1=1
# res=1
# res2=1
# cont=0


# if len(numChar) == 2:
# 	while res<=10000:
# 		res2=res
# 		res= res + num1
# 		num1=res2
# 		if num == 0 or num == 1 or num == res:
# 			cont=1
# 	if cont > 0:
# 		print("El numero " + str(num) + " pertenece a la serie de Fibonacci")
# 	else:
# 		print("El numero pertenece " + str(num) + " no pertenece a la serie de Fibonacci")
# else:
# 	print("El numero esta fuera del rango")

# --------------------------------------------------

# Ejercicio 41

# num1=1
# res=1
# res2=1
# lista=[0,1]
# while res<=10000:
# 	res2=res
# 	res= res + num1
# 	num1=res2
# 	lista.append(res)

# res=0

# for i in range(0,len(lista)):
#  	if lista[i] < 100:
#  		res=res + lista[i]

# print("El resultado de sumar todos los elementos de la serie de Fibonacci conprendidos desde el 0 al 100 es " + str(res))

# --------------------------------------------------

# Ejercicio 42

# num1=1
# res=1
# res2=1
# cont=0
# lista=[0,1]
# while res<=10000:
# 	res2=res
# 	res= res + num1
# 	num1=res2
# 	lista.append(res)

# res=0

# for i in range(0,len(lista)):
#  	if lista[i] > 1000:
#  		res=res + lista[i]
#  		cont= cont + 1

# res= res /cont


# print("El promedio de sumar todos los elementos de la serie de Fibonacci conprendidos desde el 0 al 1000 es " + str(res))

# --------------------------------------------------

# Ejercicio 43

# num1=1
# res=1
# res2=1
# cont=0
# lista=[0,1]
# while res<=10000:
# 	res2=res
# 	res= res + num1
# 	num1=res2
# 	lista.append(res)

# print(lista)
# res=0

# for i in range(0,len(lista)):
#  	if lista[i] > 1000 and lista[i] < 2000:
#  		cont= cont + 1

# print("Entre 1000 y 2000 hay " + str(cont) + " numero/s")

# --------------------------------------------------

# Ejercicio 44

# num=int(input("Ingrese un numero: "))

# res=1
# num= num+1
# for i in range(1,num):
# 	res = res * i
# num=num-1
# print("La factorial de " + str(num) + " es " + str(res))

# --------------------------------------------------

# Ejercicio 45

# num=int(input("Ingrese un numero: "))

# res=1
# num= num + 1
# for i in range(1,num):
# 	for x in range(1,i):
# 		x= x + 1
# 		res = res * x
# 	print("La factorial de " + str(i) + " es " + str(res))
# 	res=1

# --------------------------------------------------

# Ejercicio 46

# num=int(input("Ingrese un numero: "))
# prom=0
# res=1
# num= num + 1
# for i in range(1,num):
# 	for x in range(1,i):
# 		x= x + 1
# 		res = res * x
# 		prom= prom+res
# 	res=1

# num= num-1
# prom= prom/num

# print("El promedio de todas las factoriales entre 1 y " + str(num) + " es " + str(prom))

# --------------------------------------------------

# Ejercicio 47

# num=int(input("Ingrese un numero: "))
# sum=0
# res=1
# num= num + 1
# for i in range(1,num):
# 	for x in range(1,i):
# 		x= x + 1
# 		res = res * x
# 		sum= sum+res
# 	res=1

# num= num-1

# print("La suma de todas las factoriales entre 1 y " + str(num) + " es " + str(sum))

# --------------------------------------------------

# Ejercicio 48

# a=0
# b=1
# c=0
# for i in range(1,6):
# 	c=1
# 	while c <=2:
# 		print(a,b)
# 		a=a+1
# 		c=c+1
# 	b=b+1

# --------------------------------------------------

# Ejercicio 49
# a=1
# b=1
# c=1
# d=0
# while d<=2:
# 	c=1
# 	while c<=3:
# 		print(a,b,c)
# 		a+=1
# 		c+=1
# 	b+=1
# 	d+=1
# --------------------------------------------------

# Ejercicio 50

# a=0
# b=1
# c=0
# while b<3:
# 	c=0
# 	while c<=3:
# 		print(a,b)
# 		a+=1
# 		c+=1
# 	b+=1
# ________________[Final de ejercicios de las paginas 190, 191, 192, 193, 194]________________

# Ejercicio 1

# cont=1
# num=0
# maxm=0
# lista=[]
# while cont<11:
# 	num=int(input("Ingrese un numero: "))
# 	lista.append(num)
# 	cont+=1
# for i in range(0,len(lista)):
# 	if lista[i] > maxm:
# 		maxm= lista[i]
# 		cont=i
# cont+=1
# print("La posicion del numero mayor es: " + str(cont))

# --------------------------------------------------

# Ejercicio 2

# cont=1
# num=0
# maxm=0
# lista=[]
# while cont<11:
# 	num=int(input("Ingrese un numero: "))
# 	lista.append(num)
# 	cont+=1
# cont=0
# for i in range(0,len(lista)):
# 	if lista[i] % 2 == 0:
# 		if lista[i] > maxm:
# 			maxm= lista[i]
# 			cont=i
# cont+=1
# if cont==1:
# 	print("No hay numeros pares")
# else:
# 	print("La posicion del numero mayor par es: " + str(cont))

# --------------------------------------------------

# Ejercicio 3

# cont=1
# num=0
# maxm=0
# lista=[]
# while cont<11:
# 	num=int(input("Ingrese un numero: "))
# 	lista.append(num)
# 	cont+=1
# cont=0
# for i in range(0,len(lista)):
# 	if esPrimo(lista[i]) == True:
# 		if lista[i] > maxm:
# 			maxm= lista[i]
# 			cont=i
# cont+=1
# if cont==1:
# 	print("No hay numeros primos")
# else:
# 	print("La posicion del numero mayor primo es: " + str(cont))

# --------------------------------------------------

# Ejercicio 4

# num=0
# num2=1
# aux=1
# lista=[0,1]
# while len(lista) < 10:
# 	aux=num2
# 	num2=num2+num
# 	lista.append(num2)
# 	num=aux
# print(lista)

# --------------------------------------------------

# Ejercicio 5

# def pricipal():
# 	def esPrimo(num):
# 		if num < 2:
# 			return False
# 		elif num == 2:
# 			return True
# 		else:

# 			for x in range(2,num):
# 				if num % x == 0:
# 					return False
# 			return True
# 	def encuentraPrimos():
# 		lista=[]
# 		for i in range(100,301):
# 			if esPrimo(i) == True:
# 				lista.append(i)
# 		for i in range(0,10):
# 		 	print(lista[i])

# 	encuentraPrimos()

# pricipal()

# --------------------------------------------------

# Ejercicio 6

# def pricipal():
# 	def esPrimo(num):
# 		if num < 2:
# 			return False
# 		elif num == 2:
# 			return True
# 		else:

# 			for x in range(2,num):
# 				if num % x == 0:
# 					return False
# 			return True
# 	def encuentraPrimos():
# 		num1=int(input("Ingrese un numero:"))
# 		num2=int(input("Ingrese un numero:"))
# 		min=0
# 		max=0
# 		if num1 == num2:
# 			max=num1
# 			min=num2
# 		elif num1 > num2:
# 			max=num1
# 			min=num2
# 		else:
# 			max=num2
# 			min=num1
# 		lista=[]
# 		for i in range(min,max):
# 			if esPrimo(i) == True:
# 				print(i)
# 	encuentraPrimos()

# pricipal()

# --------------------------------------------------

# Ejercicio 7

# def pricipal():
# 	def ingresaNumeros():
# 		lista=[]

# 		for i in range(0,10):
# 			num=int(input("Ingrese un numero:"))
# 			lista.append(num)
# 		return lista

# 	def encontrarMayor(lista):
# 		may=lista[0]
# 		for i in range(0,10):
# 			if lista[i] > may:
# 				may = lista[i]
# 		print("El numero mayor es: " + str(may))
# 	encontrarMayor(ingresaNumeros())

# pricipal()

# --------------------------------------------------

# Ejercicio 8

# def pricipal():
# 	def ingresaNumeros():
# 		lista=[]

# 		for i in range(0,10):
# 			num=int(input("Ingrese un numero:"))
# 			lista.append(num)
# 		return lista

# 	def encontrarTerminadoEn4(lista):
# 		num=""
# 		for i in range(0,10):
# 			num=str(lista[i])
# 			if num[-1] == "4":
# 				print("El numero "+ num +" esta en la posicion " + str(i+1))
# 	encontrarTerminadoEn4(ingresaNumeros())

# pricipal()

# --------------------------------------------------

# Ejercicio 9

# def pricipal():
# 	def ingresaNumeros():
# 		lista=[]

# 		for i in range(0,10):
# 			num=int(input("Ingrese un numero:"))
# 			lista.append(num)
# 		return lista

# 	def encontrarMayor(lista):
# 		may=lista[0]
# 		for i in range(0,10):
# 			if lista[i] > may:
# 				may = lista[i]

# 		if lista[9] == may:
# 			pass
# 		else:
# 			lista[9] = may
# 			lista.append(may)
# 		return lista
# 	def repeticionMayor(lista):
# 		cont=0
# 		for i in range(0,len(lista)):
# 			if lista[i] == lista[-1]:
# 				cont=cont + 1
# 		if len(lista) == 11:
# 			print("El numero "+ str(lista[-1]) + " se repite " + str(cont-2) + " vez/veces")
# 		else:
# 			print("El numero "+ str(lista[9]) + " se repite " + str(cont) + " vez/veces")
# 	repeticionMayor(encontrarMayor(ingresaNumeros()))

# pricipal()

# --------------------------------------------------

# Ejercicio 10

# def pricipal():
# 	def ingresaNumeros():
# 		lista=[]

# 		for i in range(0,10):
# 			num=int(input("Ingrese un numero:"))
# 			lista.append(num)
# 		return lista

# 	def encontrar3Cifras(lista):
# 		pos=1
# 		for i in range(0,10):
# 			if len(str(lista[i])) == 3:
# 				pos=i
# 				print("El numero: " + str(lista[i])+" esta en la posicion " + str(pos+1))
# 	encontrar3Cifras(ingresaNumeros())

# pricipal()

# --------------------------------------------------

# Ejercicio 11

# def pricipal():
# 	def ingresaNumeros():
# 		lista=[]

# 		for i in range(0,10):
# 			num=int(input("Ingrese un numero:"))
# 			lista.append(num)
# 		return lista

# 	def encontrarMenos3Cifras(lista):
# 		cont=0
# 		for i in range(0,10):
# 			if len(str(lista[i])) < 3:
# 				cont=cont+1
# 		print("Hay " +str(cont)+ " numero/s con menos de 3 cifras")
# 	encontrarMenos3Cifras(ingresaNumeros())

# pricipal()

# --------------------------------------------------

# Ejercicio 12

# def pricipal():
# 	def ingresaNumeros():
# 		lista=[]

# 		for i in range(0,10):
# 			num=int(input("Ingrese un numero:"))
# 			lista.append(num)
# 		return lista

# 	def calculaPromedio(lista):
# 		prom=0
# 		for i in range(0,10):
# 			prom=prom+lista[i]
# 		prom=prom/10
# 		print("El promedio de los numeros ingresados es: " + str(prom))
# 	calculaPromedio(ingresaNumeros())

# pricipal()

# --------------------------------------------------

# Ejercicio 13

# def pricipal():
# 	def ingresaNumeros():
# 		lista=[]

# 		for i in range(0,10):
# 			num=int(input("Ingrese un numero:"))
# 			lista.append(num)
# 		return lista

# 	def calculaPromedio(lista):
# 		prom=0
# 		for i in range(0,10):
# 			prom=prom+lista[i]
# 		prom=prom/10
# 		lista.append(prom)
# 		return lista

# 	def promEnLista(lista):
# 		for i in range(0,9):
# 			if lista[i] == lista[-1]:
# 				return True
# 	if promEnLista(calculaPromedio(ingresaNumeros())) == True:
# 		print("El promedio de los numeros ingresados se encuantra dentro de los mismos")
# 	else:
# 		print("El promedio de los numeros ingresados no se encuantra dentro de los mismos")
# pricipal()

# --------------------------------------------------

# Ejercicio 14

# def pricipal():

# 	def ingresaNumeros():
# 		lista=[]

# 		for i in range(0,10):
# 			num=int(input("Ingrese un numero:"))
# 			lista.append(num)
# 		return lista

# 	def calculaPromedio(lista):
# 		prom=0
# 		for i in range(0,10):
# 			prom=prom+lista[i]
# 		prom=prom/10
# 		lista.append(prom)
# 		return lista

# 	def promEnLista(lista):
# 		cont=1
# 		for i in range(0,9):
# 			if lista[i] == lista[-1]:
# 				cont=cont+1
# 		return cont
# 	cont=promEnLista(calculaPromedio(ingresaNumeros()))
# 	if cont > 0:
# 		print("El promedio de los numeros ingresados se encuantra "+str(cont)+" vez/veces entre los mismos")
# 	else:
# 		print("El promedio de los numeros ingresados no se encuantra dentro de los mismos")
# pricipal()

# --------------------------------------------------

# Ejercicio 15

# def pricipal():

# 	def ingresaNumeros():
# 		lista=[]

# 		for i in range(0,10):
# 			num=int(input("Ingrese un numero:"))
# 			lista.append(num)
# 		return lista
# 	def esMultiploDe3(lista):
# 		cont=0
# 		for i in range(0,10):
# 			if lista[i] % 3 == 0:
# 				cont=cont+1
# 		return cont
# 	cont=esMultiploDe3(ingresaNumeros())
# 	print(str(cont)+" numeros de los ingresados son multiplos de 3")

# pricipal()

# --------------------------------------------------

# Ejercicio 16

# def pricipal():

# 	def ingresaNumeros():
# 		lista=[]

# 		for i in range(0,10):
# 			num=int(input("Ingrese un numero:"))
# 			lista.append(num)
# 		return lista
# 	def esMultiploDe3(lista):
# 		cont=0
# 		for i in range(0,10):
# 			if lista[i] % 3 == 0:
# 				print(str(lista[i])+" es multiplo de 3")
# 	esMultiploDe3(ingresaNumeros())
# pricipal()

# --------------------------------------------------

# Ejercicio 17

# def pricipal():

# 	def ingresaNumeros():
# 		lista=[]

# 		for i in range(0,10):
# 			num=int(input("Ingrese un numero:"))
# 			lista.append(num)
# 		return lista
# 	def saberNumNegativ(lista):
# 		cont=0
# 		for i in range(0,10):
# 			if lista[i] < 0:
# 				cont = cont + 1
# 		if cont == 0:
# 			print("No hay numeros negativos")
# 		else:
# 			print("Hay " +str(cont)+" numeros negativos")
# 	saberNumNegativ(ingresaNumeros())
# pricipal()

# --------------------------------------------------

# Ejercicio 18

# def pricipal():

# 	def ingresaNumeros():
# 		lista=[]

# 		for i in range(0,10):
# 			num=int(input("Ingrese un numero:"))
# 			lista.append(num)
# 		return lista
# 	def mostrarPositivos(lista):
# 		for i in range(0,10):
# 			if lista[i] >= 0:
# 				print("El numero "+ str(lista[i]) +" esta en la posicion " + str(i+1)) 
# 	mostrarPositivos(ingresaNumeros())
# pricipal()

# --------------------------------------------------

# Ejercicio 19

# def pricipal():

# 	def ingresaNumeros():
# 		lista=[]

# 		for i in range(0,10):
# 			num=int(input("Ingrese un numero:"))
# 			lista.append(num)
# 		return lista
# 	def mostrarMenor(lista):
# 		men=lista[0]
# 		for i in range(0,10):
# 			if lista[i] < men:
# 				men=lista[i]
# 		print("El numero menor es "+str(men))
				
# 	mostrarMenor(ingresaNumeros())
# pricipal()

# --------------------------------------------------

# Ejercicio 20

# def principal():

# 	def ingresaNumeros():
# 		lista=[]

# 		for i in range(0,10):
# 			num=int(input("Ingrese un numero:"))
# 			lista.append(num)
# 		return lista

# 	def esPrimo(num):
# 		if num < 2:
# 			return False
# 		elif num == 2:
# 			return True
# 		else:

# 			for i in range(2,num):
# 				if num % i == 0:
# 					return False
# 			return True

# 	def encontrarPrimo(lista):
# 		listaPrimo=[0]
# 		for i in range(0,10):
# 			if esPrimo(lista[i]) == True:
# 				listaPrimo.append(lista[i])
# 		return listaPrimo

# 	def encontrarMenorPrimo(listaPrimo):
# 		if len(listaPrimo) > 1:
# 			men=listaPrimo[1]
# 			for i in range(1,len(listaPrimo)):
# 				if listaPrimo[i] < men:
# 					men=listaPrimo[i]
# 			print("El menor numero primo es: " + str(men))
# 		else:
# 			print("No hay numeros primos")
# 	encontrarMenorPrimo(encontrarPrimo(ingresaNumeros()))



# principal()



# --------------------------------------------------

# Ejercicio 21

# def pricipal():
# 	def IngreseNum():
# 		num=0
# 		lista=[]
# 		for i in range(0,10):
# 			num=int(input("Ingrese un numero: "))
# 			lista.append(num)
		
# 		return lista
# 	def sumNum(list):
# 		listaSumados=[]
# 		for i in range(0,10):
# 			suma=0
# 			numChar=str(lista[i])
# 			for j in range(0,len(numChar)):
# 				suma=suma+int(numChar[j])
# 			listaSumados.append(suma)
# 		return listaSumados
# 	def buscarMay(listaSumados):
# 		may=listaSumados[0]
# 		for i in range(1,10):
# 			if listaSumados[i] > may:
# 				may=listaSumados[i]
# 				pos=i+1
# 		print("La posicion del numero que la suma de sus digitos es mayor es: " + str(pos))

# 	lista=IngreseNum()
# 	listaSumados=sumNum(lista)
# 	buscarMay(listaSumados)

# pricipal()

# --------------------------------------------------

# Ejercicio 22


# def principal():

# 	def ingresaNumeros():
# 		lista=[]

# 		for i in range(0,10):
# 			num=int(input("Ingrese un numero:"))
# 			lista.append(num)
# 		return lista

# 	def multiploDe5(lista):

# 		for i in range(0,10):
# 			if lista[i] % 5 == 0:
# 				print("El numero " +str(lista[i])+" esta en la posicion " + str(i+1))

# 	multiploDe5(ingresaNumeros())

# principal()

# --------------------------------------------------

# Ejercicio 23

# def principal():

# 	def ingresaNumeros():
# 		lista=[]

# 		for i in range(0,10):
# 			num=int(input("Ingrese un numero:"))
# 			lista.append(num)
# 		return lista

# 	def determinaRepetido(lista):
# 		repetido = []
# 		unico = []
 
# 		for x in lista:
# 			if x not in unico:
# 				unico.append(x)
# 			else:
# 				if x not in repetido:
# 					repetido.append(x)
# 		if repetido == []:
# 			print("No hay numeros repetidos")
# 		else:
# 			print("Si hay numeros repetidos")

# 	determinaRepetido(ingresaNumeros())

# principal()

# --------------------------------------------------

# Ejercicio 24


# def principal():

# 	def ingresaNumeros():
# 		lista=[]

# 		for i in range(0,10):
# 			num=int(input("Ingrese un numero:"))
# 			lista.append(num)
# 		return lista
# 	def encontrarNumMasLargo(lista):
# 		may=lista[0]
# 		for i in range(0,10):
# 			if len(str(lista[i])) > len(str(may)):
# 				may=lista[i]
# 		print("El numero con mas digitos es: " + str(may))

# 	encontrarNumMasLargo(ingresaNumeros())

# principal()

# --------------------------------------------------

# Ejercicio 25

# def principal():

# 	def ingresaNumeros():
# 		lista=[]

# 		for i in range(0,10):
# 			num=int(input("Ingrese un numero:"))
# 			lista.append(num)
# 		return lista

# 	def esPrimo(num):
# 		if num < 2:
# 			return False
# 		elif num == 2:
# 			return True
# 		else:

# 			for i in range(2,num):
# 				if num % i == 0:
# 					return False
# 			return True

# 	def encontrarPrimo(lista):
# 		listaPrimo=[0]
# 		for i in range(0,10):
# 			if esPrimo(lista[i]) == True:
# 				listaPrimo.append(lista[i])
# 		return listaPrimo

# 	def encontrarPrimoTermEn3(lista):
# 		cont=0
# 		num=""
# 		for i in range(0,len(lista)):
# 			num=str(lista[i])
# 			if num[-1] == "3":
# 				cont=cont+1
# 		print("Hay " + str(cont)+" numero/s primo/s terminado/s en 3")


# 	encontrarPrimoTermEn3(encontrarPrimo(ingresaNumeros()))

# principal()

# --------------------------------------------------

# Ejercicio 26

# def principal():

# 	def ingresaNumeros():
# 		lista=[]

# 		for i in range(0,10):
# 			num=int(input("Ingrese un numero:"))
# 			lista.append(num)
# 		return lista

# 	def calculaFactoEnLista(lista):
# 		listaFacto=[]
# 		facto=1
# 		for i in range(0,10):
# 			facto=1
# 			if lista[i] > 0:
# 				for j in range(1,lista[i]):
# 					facto=facto*j
# 			listaFacto.append(facto)
# 		print(listaFacto)

# 	calculaFactoEnLista(ingresaNumeros())


# principal()

# --------------------------------------------------

# Ejercicio 27

# def principal():

# 	def ingresaNumeros():
# 		lista=[]

# 		for i in range(0,10):
# 			num=int(input("Ingrese un numero:"))
# 			lista.append(num)
# 		return lista

# 	def calculaFactoEnLista(lista):
# 		listaFacto=[]
# 		facto=1
# 		for i in range(0,10):
# 			facto=1
# 			if lista[i] > 0:
# 				for j in range(1,lista[i]):
# 					facto=facto*j
# 			listaFacto.append(facto)
# 		return listaFacto
# 	def promedioEnLista(lista):
# 		prom=0
# 		for i in range(0,10):
# 			prom=prom+lista[i]
# 		prom=prom/10
# 		print(round(prom))
# 	promedioEnLista(calculaFactoEnLista(ingresaNumeros()))


# principal()

# --------------------------------------------------

# Ejercicio 28

# def principal():

# 	def ingresaNumeros():
# 		lista=[]

# 		for i in range(0,10):
# 			num=int(input("Ingrese un numero:"))
# 			lista.append(num)
# 		return lista
# 	def mostrarNumEnLista(lista):
# 		for i in range(0,10):
# 			for j in range(0,lista[i]):
# 				print(j)
# 	mostrarNumEnLista(ingresaNumeros())

# principal()

# --------------------------------------------------

# Ejercicio 29

# def principal():

# 	def ingresaNumeros():
# 		lista=[]

# 		for i in range(0,10):
# 			num=int(input("Ingrese un numero:"))
# 			lista.append(num)
# 		return lista
# 	def mostrarDigDeNumEnLista(lista):
# 		numChar=""
# 		for i in range(0,10):
# 			numChar=str(lista[i])
# 			for j in range(0,len(numChar)):
# 				for k in range(0,int(numChar[j])):
# 					print(k)
# 	mostrarNumEnLista(ingresaNumeros())

# principal()

# --------------------------------------------------

# Ejercicio 30


# def principal():

# 	def ingresaNumeros():
# 		lista=[]

# 		for i in range(0,10):
# 			num=int(input("Ingrese un numero:"))
# 			lista.append(num)
# 		return lista
# 	def encontrarNumEnLista(lista):
# 		num=int(input("Ahora ingrese el numero que desea buscar dentro de la lista: "))
# 		cont=0
# 		for i in range(0,10):
# 			if lista[i]==num:
# 				cont=cont+1
# 		if cont == 0:
# 			print("El numero "+str(num)+" no se encuentra entre los numeros ingresados")
# 		else:
# 			print("El numero "+str(num)+" se encuentra entre los numeros ingresados")

# 	encontrarNumEnLista(ingresaNumeros())

# principal()

# --------------------------------------------------

# Ejercicio 31


# def principal():

# 	def ingresaNumeros():
# 		lista=[]

# 		for i in range(0,10):
# 			num=int(input("Ingrese un numero:"))
# 			lista.append(num)
# 		return lista
# 	def encontrarDivExacEnLista(lista):
# 		num=int(input("Ahora ingrese el numero que desea buscar cuantos divisores exctos hay ingresados: "))
# 		cont=0
# 		for i in range(0,10):
# 			if lista[i]%num==0:
# 				cont=cont+1
# 		print("Hay "+str(cont)+" divisor/es exacto/s de " + str(num))
# 	encontrarNumEnLista(ingresaNumeros())

# principal()

# --------------------------------------------------

# Ejercicio 32

# def principal():

# 	def ingresaNumeros():
# 		lista=[]

# 		for i in range(0,10):
# 			num=int(input("Ingrese un numero:"))
# 			lista.append(num)
# 		return lista
# 	def encontrarUltDig(lista):
# 		num=str(input("Ahora ingrese el numero que desea buscar cuantos numeros hay terminados en el mismo: "))
# 		cont=0
# 		numChar=""
# 		for i in range(0,10):
# 			numChar=str(lista[i])
# 			if numChar[-1] == num:
# 				cont=cont+1
# 		print("Hay "+str(cont)+" que terminan en " + str(num))
# 	encontrarNumEnLista(ingresaNumeros())

# principal()

# --------------------------------------------------

# Ejercicio 33

# def principal():

# 	def esPar(num):
# 		if num % 2 == 0:
# 			return True
# 	def ingresaNumeros():
# 		lista=[]

# 		for i in range(0,10):
# 			num=int(input("Ingrese un numero:"))
# 			lista.append(num)
# 		return lista
# 	def sumaDeDigPares(lista):
# 		res=0
# 		numChar=""
# 		listaPares=[]
# 		for i in range(0,10):
# 			numChar=str(lista[i])
# 			for j in range(0,len(numChar)):
# 				if esPar(int(numChar[j]))==True:
# 					listaPares.append(int(numChar[j]))
# 		for i in range(0,len(listaPares)):
# 			res=res+listaPares[i]
# 		print("La suma de todos los numeros Pares es: " + str(res))
# 	sumaDeDigPares(ingresaNumeros())

# principal()

# --------------------------------------------------

# Ejercicio 34

# def principal():

# 	def ingresaNumeros():
# 		lista=[]

# 		for i in range(0,10):
# 			num=int(input("Ingrese un numero:"))
# 			lista.append(num)
# 		return lista

# 	def candidadDe2(lista):
# 		numChar=""
# 		cont=0
# 		for i in range(0,10):
# 			numChar=str(lista[i])
# 			for j in range(0,len(numChar)):
# 				if numChar[j] == "2":
# 					cont=cont+1
# 		print("Entre los numeros ingresados hay " +str(cont)+" numero/s 2")
# 	candidadDe2(ingresaNumeros())
# principal()

# --------------------------------------------------

# Ejercicio 35


# def principal():

# 	def ingresaNumeros():
# 		lista=[]

# 		for i in range(0,10):
# 			num=int(input("Ingrese un numero:"))
# 			lista.append(num)
# 		return lista

# 	def esPrimo(num):
# 		if num < 2:
# 			return False
# 		elif num == 2:
# 			return True
# 		else:

# 			for i in range(2,num):
# 				if num % i == 0:
# 					return False
# 			return True
# 	def promEsPrimo(lista):
# 		prom=0
# 		for i in range(0,10):
# 			prom=prom+lista[i]
# 		prom=prom/10
# 		if esPrimo(round(prom)) == True:
# 			print("El promedio de los numeros ingresados es un numero primo") 
# 		else:
# 			print("El promedio de los numeros ingresados no es un numero primo")
# 	promEsPrimo(ingresaNumeros())
# principal()

# --------------------------------------------------

# Ejercicio 36


# def principal():

# 	def ingresaNumeros():
# 		lista=[]

# 		for i in range(0,10):
# 			num=int(input("Ingrese un numero:"))
# 			lista.append(num)
# 		return lista

# 	def esPrimo(num):
# 		if num < 2:
# 			return False
# 		elif num == 2:
# 			return True
# 		else:

# 			for i in range(2,num):
# 				if num % i == 0:
# 					return False
# 			return True

# 	def cantidadDePrimos(lista):
# 		cont=0
# 		numChar=""
# 		for i in range(0,10):
# 			numChar=str(lista[i])
# 			for j in range(0,len(numChar)):
# 				if esPrimo(int(numChar[j]))==True:
# 					cont=cont+1
# 		print("Entre los digitos ingresados hay " +str(cont)+"numero/s primo/s")
	
# 	cantidadDePrimos(ingresaNumeros())

# principal()


# --------------------------------------------------

# Ejercicio 37

# def principal():

# 	def ingresaNumeros():
# 		lista=[]

# 		for i in range(0,10):
# 			num=int(input("Ingrese un numero:"))
# 			lista.append(num)
# 		return lista

# 	def listaAlCuadrado(lista):
# 		res=0
# 		listaAlCuadrado=[]
# 		for i in range(0,10):
# 			res=0
# 			res=lista[i] * lista[i]
# 			listaAlCuadrado.append(res)
# 		print(listaAlCuadrado)

# 	listaAlCuadrado(ingresaNumeros())

# principal()

# --------------------------------------------------

# Ejercicio 38


# def principal():

# 	def ingresaNumeros():
# 		lista=[]

# 		for i in range(0,10):
# 			num=int(input("Ingrese un numero:"))
# 			lista.append(num)
# 		return lista

# 	def esPrimo(num):
# 		if num < 2:
# 			return False
# 		elif num == 2:
# 			return True
# 		else:

# 			for i in range(2,num):
# 				if num % i == 0:
# 					return False
# 			return True

# 	def semisumaEsPrimo(lista):
# 		res=0
# 		for i in range(0,10):
# 			res= res + lista[i]
# 		res=res/2
# 		if esPrimo(round(res)) == True:
# 			print("El resultado de la semisuma de los numeros ingresados es un numero primo") 
# 		else:
# 			print("El resultado de la semisuma de los numeros ingresados es no un numero primo")
# 	semisumaEsPrimo(ingresaNumeros())

# principal()


# --------------------------------------------------

# Ejercicio 39

# def principal():

# 	def ingresaNumeros():
# 		lista=[]

# 		for i in range(0,10):
# 			num=int(input("Ingrese un numero:"))
# 			lista.append(num)
# 		return lista

# 	def esPar(num):
# 		if num % 2 == 0:
# 			return True
# 	def semisumaEsPar(lista):
# 		res=0
# 		for i in range(0,10):
# 			res= res + lista[i]
# 		res=res/2
# 		if esPar(res) == True:
# 			print("El resultado de la semisuma de los numeros ingresados es un numero par") 
# 		else:
# 			print("El resultado de la semisuma de los numeros ingresados es no un numero par")
# 	semisumaEsPar(ingresaNumeros())

# principal()


# --------------------------------------------------

# Ejercicio 40

# num=int(input("Ingrese un numero: "))
# def esImpar(num):
#     if num % 2 != 0:
#         return True

# if esImpar(num) == True:
#     print("Weird")
# elif num > 2 and num < 6:
#     print("Not Weird")
# elif num > 6 and num < 21:
#     print("Weird")
# elif num > 20:
#     print("Not Weird")









































































