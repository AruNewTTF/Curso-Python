
#Forma no optimizada de suma de valores
def suma(lista):
    numeros_sumados = 0
    for numero in lista:
        numeros_sumados = numeros_sumados + numero
    return numeros_sumados

resultado = suma([4,1,1,1,1])
print(resultado)

print("------------------------------------")

#utilizando parametro args
#el asterisco indica que lo que le sigue
#será entendido como una lista

def suma(*num):
    return sum(num)
resultado = suma(1,2,3,4,5)
print(resultado)

