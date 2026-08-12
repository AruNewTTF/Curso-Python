ingresoMensual = 100000

if ingresoMensual > 10000:
    print("Economicamente estable en cualquier parte del mundo")
elif ingresoMensual > 1000:
    print("Economicamente estable en Latinoamerica")
else:
    print("Cagaste")
    
#Por ejemplo en estos bloques, si la primera condicional no se cumple pasa a la siguiente condicional,
#si este tampoco funciona, entonces pasará al else
#hay ifs anidados, un if dentro de otro