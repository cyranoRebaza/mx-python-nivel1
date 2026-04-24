"""
Unidad 03 - Ejercicio 02

Hacer un programa para ingresar dos números distintos y luego se muestre por
pantalla el menor de ellos.

"""
# Pedir datos
numero_1 = int(input("Ingrese primer numero: "))
numero_2 = int(input("Ingrese segundo numero: "))

# Calcular y mostrar
if numero_1 < numero_2:
    print(f"El menor de los dos numeros es: {numero_1}")