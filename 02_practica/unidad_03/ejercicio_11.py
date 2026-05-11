"""
Unidad 03 - Ejercicio 11

Hacer un programa para ingresar cuatro números y luego mostrar por pantalla
cuántos son menores a 100.

"""

# Pedir datos
numero_1 = int(input("Ingrese un numero: "))
numero_2 = int(input("Ingrese un numero: "))
numero_3 = int(input("Ingrese un numero: "))
numero_4 = int(input("Ingrese un numero: "))

# Buscar  cuantos son menores a 100
menores_100 = 0

if numero_1 < 100:
    menores_100 = menores_100 + 1

if numero_2 < 100:
    menores_100 = menores_100 + 1
    
if numero_3 < 100:
    menores_100 = menores_100 + 1
    
if numero_4 < 100:
    menores_100 = menores_100 + 1
    
# Mostrar cuantos son menores a 100
print(f"La cantidad de numeros menores a 100 es: {menores_100}")
