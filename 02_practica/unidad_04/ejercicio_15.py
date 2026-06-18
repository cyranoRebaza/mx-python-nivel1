"""
Unidad 04 - Ejercicio 15

Hacer un programa para recibir listas de números positivos que están separadas 
entre sí por un cero. El fin de la carga se notifica con un número negativo. 
Luego mostrar cuántos números tiene cada lista.

"""

numero = int(input("Ingrese un numero: "))

while numero >= 0:
    cantidad_numeros = 0

    while numero != 0:
        cantidad_numeros += 1
        numero = int(input("Ingrese un numero: "))

    print(f"La cantidad de numeros de la lista es: {cantidad_numeros}")

    numero = int(input("Ingrese un numero: "))
