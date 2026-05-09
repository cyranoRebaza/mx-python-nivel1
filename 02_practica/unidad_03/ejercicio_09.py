"""
Unidad 03 - Ejercicio 09

Hacer un programa para ingresar cinco números distintos y luego mostrar por
pantalla el mayor y el menor de ellos.

"""

# Pedir datos
numero_1 = int(input("Ingrese un numero: "))
numero_2 = int(input("Ingrese un numero: "))
numero_3 = int(input("Ingrese un numero: "))
numero_4 = int(input("Ingrese un numero: "))
numero_5 = int(input("Ingrese un numero: "))

# Proceso
if numero_1 > numero_2:
    mayor = numero_1
    menor = numero_2
else:
    mayor = numero_2
    menor = numero_1
    
if numero_3 > mayor:
    mayor = numero_3
elif numero_3 < menor:
    menor = numero_3
    
if numero_4 > mayor:
    mayor = numero_4
elif numero_4 < menor:
    menor = numero_4
    
if numero_5 > mayor:
    mayor = numero_5
elif numero_5 < menor:
    menor = numero_5
    
# Mostrar
print(f"El menor es: {menor}")
print(f"El mayor es: {mayor}")
    


