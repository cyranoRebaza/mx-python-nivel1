"""
Unidad 03 - Ejercicio 08

Hacer un programa para ingresar cuatro números distintos y luego mostrar por
pantalla el menor de ellos.

"""
# Pedir datos
numero_1 = int(input("Ingrese un numero: "))
numero_2 = int(input("Ingrese un numero: "))
numero_3 = int(input("Ingrese un numero: "))
numero_4 = int(input("Ingrese un numero: "))

# Buscar el mayor
if numero_1 < numero_2:
    menor = numero_1
else:
    menor = numero_2
    
if numero_3 < menor:
    menor = numero_3

if numero_4 < menor:
    menor = numero_4
    
# Mostrar el mayor
print(f"El menor es el numero: {menor}")