"""
Unidad 02 - Ejercicio 06

Hacer un programa para ingresar por teclado las tres notas de exámenes de un
alumno y luego calcule y emita por pantalla el promedio final.

"""

# Pedir datos
nota1 = int(input("Ingrese la nota 1: "))
nota2 = int(input("Ingrese la nota 2: "))
nota3 = int(input("Ingrese la nota 3: "))

# Calcular el promedio
suma_notas = nota1 + nota2 + nota3
cantidad_notas = 3
promedio_notas = suma_notas / cantidad_notas

# Mostrar el promedio
print(f"El promedio final es: {promedio_notas:.2f}")