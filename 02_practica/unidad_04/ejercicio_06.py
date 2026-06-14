"""
Unidad 04 - Ejercicio 06

Hacer un programa que solicite al usuario números enteros positivos.
El programa deberá seguir solicitando números mientras se ingresen valores 
positivos.

Al finalizar (cuando se ingrese un número menor o igual a cero), informar:

- La cantidad total de números ingresados

"""
cantidad_numeros = 0

numero = int(input("Ingrese un numero: "))
while numero > 0:
    cantidad_numeros += 1
    numero = int(input("Ingrese un numero: "))

# Mostrar los numeros
print(f"La cantidad de numeros positivos ingresados es: {cantidad_numeros}")
