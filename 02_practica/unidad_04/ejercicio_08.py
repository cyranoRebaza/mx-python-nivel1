"""
Unidad 04 - Ejercicio 08

Hacer un programa que solicite números enteros al usuario.
El programa deberá finalizar cuando se ingresen dos números positivos 
consecutivos. Una vez finalizado el ingreso, informar:

- La cantidad total de números ingresados

"""
cantidad_numeros = 0
cantidad_positivos = 0

while cantidad_positivos < 2:
    numero = int(input("Ingrese un numero: "))
    cantidad_numeros += 1
    if numero > 0:
        cantidad_positivos += 1
    else:
        cantidad_positivos = 0

print(f"Cantidad de numeros ingresados es: {cantidad_numeros}")
