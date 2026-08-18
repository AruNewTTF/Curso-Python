
diccionario = {
    "nombre" : "Pipe",
    "Edad" : 21,
    "Arrepentimientos" : "varios"
}

#este bucle solo mostrará las keys del diccionario
for key in diccionario:
    print(key)
    
print("\n-------------------\n")

#este bucle permite ver los elementos de las keys del diccionario
#ademas de las propias keys

for key in diccionario.items():
    index = key[0]
    value = key[1]
    print(f"Indice: {index}\n"
          f"Valor: {value}\n")