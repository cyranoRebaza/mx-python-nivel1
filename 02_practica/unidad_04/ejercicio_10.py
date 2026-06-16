"""
Unidad 04 - Ejercicio 10

Hacer un programa que solicite números enteros.
El ingreso de datos finaliza cuando el usuario ingresa dos veces seguidas el 
mismo número. Al finalizar, informar:

- Cuántos números se ingresaron en total (sin contar el segundo repetido)

- El valor que provocó el corte

"""

cantidad_numeros = 1

numero_anterior = int(input("Ingrese un numero: "))
numero = int(input("Ingrese un numero: "))


while numero != numero_anterior:
    cantidad_numeros += 1
    numero_anterior = numero
    numero = int(input("Ingrese un numero: "))

print(f"Cantidad de numeros ingresados: {cantidad_numeros}")
print(f"El valor que provoco el corte: {numero}")
