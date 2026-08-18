
#creando un conjunto con set()

conjunto = set(["Dato1"])

#agregando un conjunto dentro de otro

conjunto1 = frozenset(["Dato1", "Dato2"])
conjunto2 = {conjunto1, "Dato3"}

print(conjunto)

#Teoria de conjuntos

conjunto1 = {1,3,5,7}
conjunto2 = {1,3,7}

#como verificamos que un conjunto
#es un subconjunto de otro
print("------------------------------------")
resultado = conjunto2.issubset(conjunto1)
print(resultado)

print("------------------------------------")
#verificar si es un superconjunto
resultado = conjunto2.issuperset(conjunto1)
print(resultado)

print("------------------------------------")
#verificar si hay similitudes
resultado = conjunto2.isdisjoint(conjunto1)
print(resultado)