
#for es un bucle que recorre todos los elementos iterables
#en el ejemplo de una lista va a iterar todos los elementos dentro de ella
lista = ["gato", "perro", "loro", "cocodrilo"]

for animales in lista:
    print(f"La variable animal actual es: {animales}")
    
numeros = [1,2,3,4,5,6,7,8,9,10]
otrosNumeros = [1,2,3,4]

print("---------------------------------------")

for num in numeros:
    result = num * 100
    print(f"Puedes crear variables dentro de un for para trabajarlas\n"
          f"Resultado de {num} por 10: {result}")
    
print("---------------------------------------")    

#iterar dos lista

for numero, animal in zip(otrosNumeros, lista):
    print(f"Recorriendo lista 1: {numero}")
    print(f"Recorriendo lista 2: {animal}")
    
print("---------------------------------------")
    
#uso de la fun range()
#para definir range, se coloca primero
#donde empieza el numero y el segundo es para 
#definir donde termina
#el tercero es para ir realizando saltos

for num in range(5,11,2):
    print(f"Numero actual de num: {num}")
    
print("---------------------------------------")
    
#como recorrer una lista segun su index
#enumerate tranforma num en una tupla

for num in enumerate(numeros):
    index = num[0]
    valor = num[1]
    print(f"Indice: {index}\n"
          f"Valor: {valor}\n")
    
print("---------------------------------------")
    
#utilizando else

for num in numeros:
    print(f"Ejecutando el ultimo bucle, valor actual: {num}\n")
else:
    print("El bucle ha terminado")