"""
Unidad 04 - Ejercicio 07

Hacer un programa que solicite al usuario un número entero entre 1 y 10 inclusive.

Si el número ingresado no cumple la condición, el programa deberá volver a 
solicitarlo tantas veces como sea necesario hasta que el valor sea válido.
Una vez ingresado un número correcto, mostrar por pantalla:

- “Número válido ingresado”.

"""
# version 1- mientras el numero este fuera del rango
numero = int(input("Ingrese un numero: "))
while numero < 1 or numero > 10:
    print("Numero invalido. Ingrese un numero entre 1 y 10.")
    numero = int(input("Ingrese un numero: "))

print("Numero valido ingresado.")
print()

# version 2 - mientras no cumplas la condicion
numero = int(input("Ingrese un numero: "))
while not (numero >= 1 and numero <= 10):
    print("Numero invalido. Ingrese un numero entre 1 y 10.")
    numero = int(input("Ingrese un numero: "))

print("Numero valido ingresado.")
