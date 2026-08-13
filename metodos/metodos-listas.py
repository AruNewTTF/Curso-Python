#list
#crea una lista

lista = list(["Hola", "Pipe", 21, 1, 2, 3, 4])

print(lista)

#Devuelve la cantidad de elementos de la lista
result = len(lista)

print(result)

#agregando elementos a la lista con append
#agrega un elemento al final de la lista
lista.append("xd")

print(lista)

#agregando con insert
#debes escoger en que indice agregar el nuevo elemento
lista.insert(2, "toy aqui")

print(lista)

#agregando varios elementos a la lista con extend

lista.extend([False, 2027])

print(lista)

#pop para eliminar un elemento de la lista POR indice
#para eliminar el ultimo elemento con pop
#debes de utilizar los negativos
#-1 agarra el ultimo indice y -2 el que le antecede
lista.pop(0)

print(lista)


#remover el elemento de la lista segun por su valor

lista.remove("toy aqui")

print(lista)


#ordena los elementos de la lista de manera ascendente, el ASC de sql 
#no permite valores strings
lista.remove("Pipe")
lista.remove("xd")

# al utilizar reverse true hace que los elementos se ordenen en reversa
#lista.sort(reverse=True)
lista.sort()

print(lista)


#reverse invierte los elementos de una lista
#a diferencia de sort, este unicamente invierte la lista
#sort ordena primero

#lista.reverse()



#eliminando todos los elementos de la lista

lista.clear()

print(lista)