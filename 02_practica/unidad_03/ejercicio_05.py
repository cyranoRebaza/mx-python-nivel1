"""
Unidad 03 - Ejercicio 05

Hacer un programa para ingresar un número y mostrar por pantalla un cartel
aclaratorio si el mismo es PAR o IMPAR.

Nota: leé sobre el operador “Resto”.

"""

# Pedir datos
numero = int(input("Ingrese un numero: "))

# calcular y mostrar
if numero % 2 == 0:
    print("es PAR")
else:
    print("es IMPAR")