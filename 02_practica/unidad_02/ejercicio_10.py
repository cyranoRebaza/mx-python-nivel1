"""
Unidad 02 - Ejercicio 10

Hacer un programa que permita ingresar por teclado dos números y que luego
muestre por pantalla la suma, la resta, la multiplicación y la división de
dichos números. Se deben mostrar cuatro resultados en pantalla. Los números deben
ser solicitados una única vez.

"""

# Pedir datos
numero1 = int(input("Ingrese el primer numero: "))
numero2 = int(input("Ingrese el segundo numero: "))

# Calcular las operaciones
suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
division = numero1 / numero2

# Mostrar valor de las operaciones
print(f"{numero1} + {numero2} = {suma}")
print(f"{numero1} - {numero2} = {resta}")
print(f"{numero1} * {numero2} = {multiplicacion}")
print(f"{numero1} / {numero2} = {division:.2f}")