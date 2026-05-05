"""
Unidad 03 - Ejercicio 07

Hacer un programa para ingresar cuatro números distintos y luego mostrar por
pantalla el mayor de ellos.

"""
# Pedir datos
numero_1 = int(input("Ingrese un numero: "))
numero_2 = int(input("Ingrese un numero: "))
numero_3 = int(input("Ingrese un numero: "))
numero_4 = int(input("Ingrese un numero: "))

# Buscar el mayor
if numero_1 > numero_2:
    mayor = numero_1
else:
    mayor = numero_2
    
if numero_3 > mayor:
    mayor = numero_3

if numero_4 > mayor:
    mayor = numero_4
    
# Mostrar el mayor
print(f"El mayor es el numero: {mayor}")