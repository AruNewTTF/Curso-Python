import modulo_matematico

seleccionador = -1
while seleccionador != 0:
    print("\nElige con que operador quieres jugar:\n1. Suma\n2. Resta\n3. Multiplicacion \n4. Division \n0. Salir")
    seleccionador = int(input("Ingrese un numero del menu: "))
    if seleccionador == 1:
        a = modulo_matematico.sumar()
        print(f"El resultado de tu suma es: {a}")
    elif seleccionador == 2:
        a = modulo_matematico.resta()
        print(f"El resultado de tu suma es: {a}")
    elif seleccionador == 3:
        a = modulo_matematico.multiplicar()
        print(f"El resultado de tu mutiplicacion es: {a}")
    elif seleccionador == 4:
        a = modulo_matematico.division()
        print(f"El resultado de tu divison es: {a}")
    elif seleccionador == 0:
        break
    else:
        print("\n--/--/--/--/--/--/--/--/\nDebes de seleccionar un numero del menu\n--/--/--/--/--/--/--/--/\n")