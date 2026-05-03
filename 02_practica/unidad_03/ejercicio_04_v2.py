"""
Unidad 03 - Ejercicio 04 (v2)

Hacer un programa para ingresar un número y luego se emita un cartel por
pantalla “Positivo” si el número es mayor a cero, “Negativo” si el número es
menor a cero o “Cero” si el número es igual a cero.

------------------------------------
criterio: usamos if anidado

"""

# Pedir los datos
numero = int(input("Ingrese un numero: "))

# calcular y mostrar
if numero > 0:
    print("POsitivo")
    
else:
    if numero == 0:
        print("Cero")
    else:
        print("Negativo")
    
