"""
Unidad 03 - Ejercicio 24

Hacer un programa que solicite cuatro numeros y emitir un cartel aclaratorio si
todos son iguales entre si, caso contrario, no emitir nada.

"""

# Pedir datos
numero_1 = int(input("Ingrese el numero 1: "))
numero_2 = int(input("Ingrese el numero 2: "))
numero_3 = int(input("Ingrese el numero 3: "))
numero_4 = int(input("Ingrese el numero 4: "))

# Verificar igualdad
if numero_1 == numero_2 and numero_2 == numero_3 and numero_3 == numero_4:
    print("Son iguales")