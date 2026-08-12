#Ejemplos de como utilizar las variables
#Primero se debe de declarar la variable
#y luego se debe de definir, sea numero, string o boolean

a = 45

print (a)

b = 5

print(round(a/b))

#tambien hay una manera de ir acumulando datos de una variable con +=
#considere que a es igual a 45

a += 10

print(a)

#a su vez se puede hacer a la inversa con -=

a -= 5

print(a)

#concatenar es unir varios strings
#para unir los strings se utiliza el +

nombre = "pipe"
saludos = "hola "+ nombre+ " ¿que fue?"
print(saludos)

#Hay otra manera que utilizabamos que son los f Strings
#al final permite transformar todo en formato String

nombre = 777
saludos = f"hola {nombre} ¿que fue?"
print(saludos)

#hay algunas funciones para identificar si están o no
#estas siendo in y not in
nombre = "pipe"

print("pipe" in nombre)
print("pipe" not in nombre)