
frase = input("Ingrese alguna frase para realizar el calculo de lapso de tiempo: ")

cantidad_palabras = frase.split(" ")

cantidad_palabras_separadas = len(cantidad_palabras)

if(cantidad_palabras_separadas > 120):
    print("El mesias del nuevo testamento")

print(f"Dijiste {cantidad_palabras} palabras y tardarías\n"
      f"alrededor de {cantidad_palabras_separadas / 2} segundos en decirlo")

print(f"Dalto lo diria en {cantidad_palabras_separadas / 2 * 1.3} en decirlo")