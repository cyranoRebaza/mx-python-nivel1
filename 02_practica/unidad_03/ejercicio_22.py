"""
Unidad 03 - Ejercicio 22

Hacer un programa para ingresar tres números y emitir un cartel aclaratorio si
la suma de los dos primeros es mayor al producto del segundo con el tercero.

"""

# Pedir datos
numero_1 = int(input("Ingrese el numero 1: "))
numero_2 = int(input("Ingrese el numero 2: "))
numero_3 = int(input("Ingrese el numero 3: "))

# calcular suma y producto
suma = numero_1 + numero_2
producto = numero_2 * numero_3

# Mostrar cartel aclaratorio
if suma > producto:
    print("La suma es mayor")
elif producto > suma:
    print("El producto es mayor")
else:
    print("La suma y el producto son iguales")
