
#creando diccionario con dict()

diccionario = dict(nombre = "Pipe", apellido = "Ponce")

print(diccionario)

#Las listas NO pueden ser reconocidas como claves / keys
#si se quisiera usar una lista debe de utilizar nuevamente
#la fun de frozenset

diccionario = {("pipe", "awo"): "xd"}
diccionario = {frozenset(["pipe", "awo"]): "xd"}

print(diccionario)

#Crear dicciones con fromkeys()
#con valores none

diccionario = dict.fromkeys(["nombre", "apellido"])
print(diccionario)