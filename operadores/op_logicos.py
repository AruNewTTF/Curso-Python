# AND
# Ambos deben ser valores True para que sea True
Resultado = True & True # Devolver True
print(f"Resultado (True & True): {Resultado}")

Resultado1 = False & True # Devolver False
print(f"Resultado1 (False & True): {Resultado1}")

Resultado2 = True & False # Devolver False
print(f"Resultado2 (True & False): {Resultado2}")

Resultado3 = False & False # Devolver False
print(f"Resultado3 (False & False): {Resultado3}")

print("-" * 30)

# OR
# Solo devolverá False si es que ninguna de las condiciones se cumplen
Resultado4 = True | True # Devolver True
print(f"Resultado4 (True | True): {Resultado4}")

Resultado5 = False | True # Devolver True
print(f"Resultado5 (False | True): {Resultado5}")

Resultado6 = True | False # Devolver True
print(f"Resultado6 (True | False): {Resultado6}")

Resultado7 = False | False # Devolver False
print(f"Resultado7 (False | False): {Resultado7}")

print("-" * 30)

# NOT
# si no es True es false y si no es false es true
Resultado8 = not True # Devolver False
print(f"Resultado8 (not True): {Resultado8}")

Resultado9 = not False # Devolver True
print(f"Resultado9 (not False): {Resultado9}")