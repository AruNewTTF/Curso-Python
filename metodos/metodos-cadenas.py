#Como utilizar los metodos:
# Dato.metodo()

cadena1 = "Hola pipe"
cadena2 = "A Veces Juego al Ligoleyen"

#dir()
#devuelve todos los atributos
#todo lo que puedes hacer con el objeto que ingresas

print(dir(cadena1))
#print(dir(5)) #no solo se limita a texto

#UPPER CONVIERTE TODAS LAS CADENAS A MAYUSCULAS

solv = cadena1.upper()
print(solv)

#lower convierte todas las cadenas a minusculas
solv = cadena1.lower()
print(solv)

#Capitalize convierte unicamente el primer caracter en mayuscula,
#lo demas se queda en minusculas

solv = cadena2.capitalize()
print(solv)

#find
#busca una cadena dentro de otra
#más bien, la posicion del indice de lo que se pida
#si da -1 como resultado, es porque el dato no existe

busquedaFind = cadena1.find("a")
print(busquedaFind)

#index
#busca nuevamente una cadena dentro de otra
#la diferencia es que al no encontrar un valor, entrega una exception

busquedaIndex = cadena1.index("H")
print(busquedaIndex)

#isnumeric
#si es numerico es True sino es False
#puede captar numeros dentro de una cadena

cadenaNumerica = "12345"

esNumeric = cadena1.isnumeric()
print(esNumeric)

esNumeric = cadenaNumerica.isnumeric()
print(esNumeric)

#isalpha
#si es un numero alfanumerico devuelve True sino False
#unicamente valores desde la a hasta la z

esAlfa = cadenaNumerica.isalpha()
print(esAlfa)

#count()
#cuantas veces se repite un valor

contarCoincidencia = cadena1.count(" pipe")
print(contarCoincidencia)

#len()
#se cuentan cuantos caracteres tiene una cadea, osea su longitud

contarLen = len(cadena1)
print(contarLen)

#startswith()
#verificamos si una cadena empieza con otra cadena ingresada

empiezaCon = cadena1.startswith("k")
print(empiezaCon)

#endswith()
#viceversa a startswith

termincaCon = cadena1.endswith("e")
print(termincaCon)

#Replace()
#reemplaza un valor de la cadena que se le asigne a otra
#replace("valor viejo", "valor nuevo")

nuevaCadena = cadena1.replace("la", "li")
print(nuevaCadena)

#split
#devuelve una matriz, o sea una lista
#puedes asignarle por que caracter separar

cadenaParaSplit = "un,ejemplo,de,esto,es,esto"

cadenaSplit = cadena1.split()
print(cadenaSplit)

cadenaSplit = cadenaParaSplit.split(",")
print(cadenaSplit)