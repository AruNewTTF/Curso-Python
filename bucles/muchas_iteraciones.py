
frutas = ["platano", "manzana", "ciruela", "pera", "naranja", "granada", "durazno"]

for fruta in frutas:
    if fruta == "granada":
        #Continue lo que permite es continuar con el bucle saltandose
        #lo que se le exiga
        continue
    print(f"Me comeré una {fruta}\n")
    
for fruta in frutas:
    print(f"Me comeré una {fruta}\n")
    if fruta == "pera":
        #Detiene el bucle por completo
        #continua todo lo que le siga por debajo de este bucle
        break
else:
    print("No seré ejecutado por el break anterior")
    
print("Bucle terminado")

print("\n-------------------\n")

#Recorrer una cadena de texto

cadena = "Hola Pipe"
#normalmente al utilizar el for para recorerr un string
#este va quitando cada valor de la cadena, es decir
#cada letra de ella

for letra in cadena:
    print(letra)
    
print("\n-------------------\n")
    
#for en una unica linea
#lista de numeros
numeros = 1,2,3,4,5

#ejemplo de un for convencional
numeros_duplicados = list()
for num in numeros:
    numeros_duplicados.append(num*2)
    
print(f"Este es el resultado del for convencional: {numeros_duplicados}")

#For de una sola linea
numeros_duplicados = [x*2 for x in numeros]

print(f"Este es el resultado del for de una sola linea {numeros_duplicados}")

print("\n-------------------\n")