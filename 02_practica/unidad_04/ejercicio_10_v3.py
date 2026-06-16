"""
Unidad 04 - Ejercicio 10 - v3

Hacer un programa que solicite números enteros.
El ingreso de datos finaliza cuando el usuario ingresa dos veces seguidas el 
mismo número. Al finalizar, informar:

- Cuántos números se ingresaron en total (sin contar el segundo repetido)

- El valor que provocó el corte

"""
cantidad_numeros = 0
numero = int(input("Ingrese un numero: "))

while True:
    cantidad_numeros += 1
    numero_anterior = numero

    numero = int(input("Ingrese un numero: "))
    if numero == numero_anterior:
        break

print(f"La cantidad de numeros ingresados es: {cantidad_numeros}")
print(f"El valor que provoco el corte es: {numero}")
