#para crear funciones debes de usar "def"

def salutations():
    print("Hola Mundo\nvía función")

#ejecución de la funcion simple
salutations()

print("------------------------------------")

#creando una funcion con parametros
def saludo(nombre, sexo):
    sexo = sexo.lower()
    if(sexo == "mujer"):
        adjetivo = "señorita"
    elif (sexo == "hombre"):
        adjetivo = "man"
    else:
        adjetivo = "no binario"

    print(f"Hola {nombre}, mi {adjetivo} que haces?")
saludo("Esteban", "hombre")
saludo("Karla", "MujER")
saludo("Robert", "")

print("------------------------------------")

#crear una fun que retorne valores

def crear_contraseña_random(num):
    chars = "abcdefghji"
    num_int = str(num)
    num = int(num_int[0])
    c1 = num - 2
    c2 = num
    c3 = num - 5
    contraseña = f"{chars[c1]}{chars[c2]}{chars[c3]}{num*2}"
    return contraseña
    
password = crear_contraseña_random(67)
frase = f"Nueva contraseña creada: {password}"
print(frase)

