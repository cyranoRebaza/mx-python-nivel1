"""
Unidad 03 - Ejercicio 19

Hacer un programa para ingresar cuatro números y mostrar por pantalla si los
mismos se encuentran ordenados de forma decreciente.

"""

# Pedir datos
numero_1 = int(input("Ingrese primer numero: "))
numero_2 = int(input("Ingrese segundo numero: "))
numero_3 = int(input("Ingrese tercer numero: "))
numero_4 = int(input("Ingrese cuarto numero: "))

# Mostrar orden decreciente
if numero_1 > numero_2 and numero_2 > numero_3 and numero_3 > numero_4:
    print("Ordenado de forma decreciente")
else:
    print("No esta ordenado de forma decreciente")    
