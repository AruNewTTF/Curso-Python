#lambda es para crear una funcion anónima
#sirve para crear instrucciones unicas y simples

multiplicar_por_dos = lambda x : x*2

#creando funcion que identifique numeros pares
numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

def es_par(num):
    if(num%2==0):
        return True

#usando filter con una fun comun
numeros_pares = filter(es_par,numeros)

print(list(numeros_pares))

print("------------------------------------")

#Creando lo mismo de antes, pero en lambda

numeros_pares = filter(lambda numero:numero%2 == 0, numeros)
print(list(numeros_pares))