# Ejercicio 1: Determinar el mayor de dos números
# Pide al usuario que introduzca dos números y muestra un mensaje
# indicando cuál es mayor o si son iguales

numero_uno = int(input("Ingresar numero uno : \n"))
numero_dos = int(input("Ingresar numero dos: \n"))

if numero_uno > numero_dos :
 print("El primer numero fue mas grande")
elif numero_uno < numero_dos :
 print("El segundo numero fue mas grande")
else:
 print("Son iguales")