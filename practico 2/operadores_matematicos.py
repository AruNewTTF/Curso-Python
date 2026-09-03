
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

print(f"El resultado es: {division()}")