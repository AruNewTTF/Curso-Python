diccionario = {
    "nombre" : 'Pipe',
    "apellido" : 'Pop',
    "edad" : '21'
}


#permite ver las keys de un diccionario
claves = diccionario.keys()
print(claves)

#get es lo mismo que un get de SQL
#permite obtener el valor de la key del diccionario
#este no lanza excepciones si no encuentra el valor
claves = diccionario.get("nombre")
print(claves)

#eliminando un elemento del diccionario
#debes de escoger la key y puede ser multiple
diccionario.pop("nombre")
print(diccionario)

#obteniendo un elemento dict_items iterable
diccionarioIterable = diccionario.items()
print(diccionarioIterable)



#clear elimina todo del diccionario
diccionario.clear()
print(diccionario)


