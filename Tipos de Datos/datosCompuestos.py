#lista, un contenedor de varios datos   

lista = ["pipe", True, 75, 75.8]

print(lista)

#para seleccionar algun valor de la lista recordar que empieza desde el 0
#Si seleccionamos 0, entonces seleccionara el primer valor de la lista
print(lista[0])

#las tuplas en vez de corchetes se definen con parentesis
#las tuplas NO pueden modificarse a diferencia de las listas

tupla = ("pipe", True, 75, 75.8)

#como modificar algo de la lista
lista[1] = False
print(lista)

#Pero hacer lo mismo con la tupla generará un error
#tupla[3] = False

#Creacion de un conjunto o set
#el conjunto tampoco se puede modificar algun valor,
#pero si se puede redifinir
#a su vez no permite valores duplicados
#tampoco se puede acceder por indice como lo hace la lista

conjunto = {"pipe", True, 75, 75.8}
print(conjunto)
conjunto = {"nuevo set creado"}
print(conjunto)

#diccionario

diccionario = {
    'nombre': "pipe",
    'edad': 21,
    'altura': 1.69
}

#en vez de llamar por indice, aqui hay que llamar segun su nombre definido

print(diccionario["nombre"])
