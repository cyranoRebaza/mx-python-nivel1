"""
Unidad 03 - Ejercicio 18

Hacer un programa para ingresar las longitudes de los tres lados de un
triángulo y determinar si el mismo es:

Equilátero
Isósceles
Escaleno

"""

# Pedir datos
lado_1 = int(input("Ingrese el lado 1: "))
lado_2 = int(input("Ingrese el lado 2: "))
lado_3 = int(input("Ingrese el lado 3: "))

# Mostrar tipo de triangulo
if lado_1 == lado_2 and lado_2 == lado_3:
    print("Equilatero")
elif lado_1 != lado_2 and lado_1 != lado_3 and lado_2 != lado_3:
    print("Escaleno")
else:
    print("Isosceles")