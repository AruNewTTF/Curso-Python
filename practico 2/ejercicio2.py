#el profe se ausentó, los alumnos armarán la clase
#pedir el nombre y edad de los compañeros que vinieron a clases

def obtener_compañeros(cantidad):
    compañeros = []
    for i in range(cantidad):
        nombre = input("Ingrese el nombre del compañero: ")
        edad = int(input("Ingrese la edad del compañero: "))
        compañero = (nombre,edad)
        compañeros.append(compañero)
    compañeros.sort(key = lambda x:x[1])
    asistente = compañeros[0][0]
    profesor = compañeros[-1][0]
    return asistente,profesor

asistente,profesor = obtener_compañeros(5)

print(f"El profesor es: {profesor}\ny su asistente es: {asistente}")