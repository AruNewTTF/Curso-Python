
#crear funciones las cuales operen funciones basicas matematicas
#entre dos valores

#suma
def sumar():
    a = int(input("Ingrese el primer numero a sumar: ")) 
    b = int(input("Ingrese el segundo numero a sumar: "))
    resultado = a + b
    return resultado

#resta
def resta():
    a = int(input("Ingrese el primer numero a restar: ")) 
    b = int(input("Ingrese el segundo numero a restar: "))
    resultado = a - b
    return resultado

#multiplicacion
def multiplicar():
    a = int(input("Ingrese el primer numero a multiplicar: ")) 
    b = int(input("Ingrese el segundo numero a multiplicar: "))
    resultado = a * b
    return resultado

#division
def division():
    a = int(input("Ingrese el primer numero a dividir: ")) 
    b = int(input("Ingrese el segundo numero a dividir: "))
    resultado = a / b
    return resultado

seleccionador = -1
while seleccionador != 0:
    print("\nElige con que operador quieres jugar:\n1. Suma\n2. Resta\n3. Multiplicacion \n4. Division \n0. Salir")
    seleccionador = int(input("Ingrese un numero del menu: "))
    if seleccionador == 1:
        a = sumar()
        print(f"El resultado de tu suma es: {a}")
    elif seleccionador == 2:
        a = resta()
        print(f"El resultado de tu suma es: {a}")
    elif seleccionador == 3:
        a = multiplicar()
        print(f"El resultado de tu mutiplicacion es: {a}")
    elif seleccionador == 4:
        a = division()
        print(f"El resultado de tu divison es: {a}")
    elif seleccionador == 0:
        break
    else:
        print("\n--/--/--/--/--/--/--/--/\nDebes de seleccionar un numero del menu\n--/--/--/--/--/--/--/--/\n")