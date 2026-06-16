"""
Unidad 04 - Ejercicio 10 - v2

Hacer un programa que solicite números enteros.
El ingreso de datos finaliza cuando el usuario ingresa dos veces seguidas el 
mismo número. Al finalizar, informar:

- Cuántos números se ingresaron en total (sin contar el segundo repetido)

- El valor que provocó el corte

"""
cantidad_numeros = 0

numero = int(input("Ingrese un numero: "))
cantidad_numeros_seguidos = 1

while cantidad_numeros_seguidos < 2:
    cantidad_numeros += 1
    numero_anterior = numero

    numero = int(input("Ingrese un numero: "))
    if numero == numero_anterior:
        cantidad_numeros_seguidos += 1

print(f"Cantidad de numeros ingresados: {cantidad_numeros}")
print(f"Valor que provovo el corte: {numero}")
