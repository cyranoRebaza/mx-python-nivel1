"""
Unidad 04 - Ejercicio 02

Hacer un programa que solicite el ingreso de 10 números y que muestre el mayor 
de ellos por pantalla. Solo se debe emitir UN valor por pantalla.

"""

# Pedir los numeros y buscar el mayor
for i in range(10):
    numero = int(input("Ingrese un numero: "))
    if i == 0:
        mayor = numero
    elif numero > mayor:
        mayor = numero

# Mostrar el numero mayor
print(f"El numero mayor es: {mayor}")
