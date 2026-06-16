"""
Unidad 04 - Ejercicio 11

Hacer un programa que solicite números enteros.
El programa deberá continuar mientras los números ingresados alternen entre par 
e impar. El ingreso finaliza cuando se ingresan dos números consecutivos del 
mismo tipo (ambos pares o ambos impares). Al finalizar, informar:

- La cantidad de números ingresados

- Si el corte se produjo por pares o por impares

"""

cantidad_numeros = 1

numero_anterior = int(input("Ingrese un numero: "))
numero = int(input("Ingrese un numero: "))


while numero % 2 != numero_anterior % 2:
    cantidad_numeros += 1

    numero_anterior = numero
    numero = int(input("Ingrese un numero: "))

# Mostrar cantidad de numeros ingresados
print(f"La cantidad de numeros ingresados es: {cantidad_numeros}")

# Motivo de corte
if numero % 2 == 0:
    print("El corte se produjo por numeros pares")
else:
    print("El corte se produjo por numeros impares")
