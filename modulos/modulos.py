#Los modulos son las extensiones .py de cada archivo, es decir,
#cada modulo es cada archivo y estos pueden interactuar entre ellos,
#importar los elementos de un modulo a otro por ejemplo

import modulo_saludar

saludos = modulo_saludar.saludo("Pipe")

print(saludos)