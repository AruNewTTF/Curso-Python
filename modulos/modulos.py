#Los modulos son las extensiones .py de cada archivo, es decir,
#cada modulo es cada archivo y estos pueden interactuar entre ellos,
#importar los elementos de un modulo a otro por ejemplo

import modulo_saludar

#al importar puedes asignarle un nombre especial para llamarlo
#import modulo_saludar as m_s

#a su vez si quieres obtener una funcion en especifico
#puedes hacerlo cambiando un poco el orden al llamar al modulo
#from modulo_saludar import saludo

saludos = modulo_saludar.saludo("Pipe")

print(saludos)