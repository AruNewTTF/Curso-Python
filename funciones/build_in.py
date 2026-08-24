numeros = [1,2,3,4,5]

#encontrando el numero mayor de una lista

numero_alto = max(numeros)
print(numero_alto)

print("------------------------------------")

#encontrando el numero menor

numero_menor = min(numeros)
print(numero_menor)

print("------------------------------------")

#redondear a 6 decimas

numero_decimal = 13.56781234
print(round(numero_decimal,6))

print("------------------------------------")


#retorna False -> 0, vacio, False, ninguno
#Retorna True -> distinto a 0, True, cadena, dato no vacío

resultado_bool_false = bool()
resultado_bool_true = bool("24.500-3")
print(f"Resultado Booleano falso vacío: {resultado_bool_false}\n"
      f"Resultado Booleano verdadero con cadena: {resultado_bool_true}")

print("------------------------------------")

#Retorna True, si todos los valores son verdaderos

resultado_all = all([123, "true", [123,45]])
print(f"Resultado all verdadero: {resultado_all}")

resultado_all = all([0, "true", [123,45]])
print(f"Resultado all falso: {resultado_all}")

print("------------------------------------")

#suma todos los valores de un iterable
suma_total = sum(numeros)
print(suma_total)

