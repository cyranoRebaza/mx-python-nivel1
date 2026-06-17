"""
Unidad 04 - Ejercicio 11 - v2

Hacer un programa que solicite números enteros.
El programa deberá continuar mientras los números ingresados alternen entre par 
e impar. El ingreso finaliza cuando se ingresan dos números consecutivos del 
mismo tipo (ambos pares o ambos impares). Al finalizar, informar:

- La cantidad de números ingresados

- Si el corte se produjo por pares o por impares

"""
cantidad_numeros = 0

numero = int(input("Ingrese un numero: "))
estado_actual = numero % 2
estado_anterior = estado_actual - 1

while estado_actual != estado_anterior:
    cantidad_numeros += 1
    numero = int(input("Ingrese un numero: "))

    estado_anterior = estado_actual
    estado_actual = numero % 2

# Mostrar la cantidad numeros
print(f"La cantidad de numeros ingresados es: {cantidad_numeros}")

# causa del corte
if estado_actual == 0:
    print("El corte se produjo por numeros pares")
else:
    print("El corte se produjo por numeros impares")
