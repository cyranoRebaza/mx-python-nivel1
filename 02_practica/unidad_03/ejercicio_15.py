"""
Unidad 03 - Ejercicio 15

Hacer un programa para ingresar dos números y emitir por pantalla el resultado
de la división del primero por el segundo.

Nota: si el segundo número es cero, mostrar un cartel aclaratorio indicando que
no se puede dividir por cero.

"""

# Pedir los datos
numero_1 = int(input("Ingrese un numero: "))
numero_2 = int(input("Ingrese un numero: "))

# Calcular y mostrar
if numero_2 == 0:
    print("No se puede dividir por cero")
    
else:
    resultado = numero_1 / numero_2
    print(f"El resultado de la division es: {resultado:.2f}")
    