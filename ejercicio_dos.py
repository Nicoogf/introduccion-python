# Ejercicio 2: Calculadora simple
# Pide al usuario dos números y una operación (+, -, *, /)
# Realiza la operación y muestra el resultado (maneja la división entre zero)

numero_uno = int(input("Ingresar el primer numero : \n"))
numero_dos = int(input("Ingresar segundo numero : \n" ))
operacion = input("Ingesa operacion + / - / * / %")

if operacion == "+" :
    print(f"El resulado de la suma es {numero_uno + numero_dos} " )
elif operacion == "-" :
    print(f"El resulado de la resta es {numero_uno - numero_dos} " )
elif operacion == "*" :
    print(f"El resulado de la multiplicacion es {numero_uno * numero_dos} " )
elif operacion == "%" :
    if numero_dos == 0 :
        print("No se puede dividir por cero")
    else:
        print(f"El resultado de la division es {numero_uno / numero_dos} ")
else:
    print("No se reconoce simbolo")