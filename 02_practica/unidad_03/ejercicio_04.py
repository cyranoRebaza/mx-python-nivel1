"""
Unidad 03 - Ejercicio 04

Hacer un programa para ingresar un número y luego se emita un cartel por
pantalla “Positivo” si el número es mayor a cero, “Negativo” si el número es
menor a cero o “Cero” si el número es igual a cero.

------------------------------------
criterio: usamos if secuencial

"""

# Pedir los datos
numero = int(input("Ingrese un numero: "))

# calcular y mostrar
if numero > 0:
    print("POsitivo")

if numero == 0:
    print("Cero")
    
if numero < 0:
    print("Negativo")