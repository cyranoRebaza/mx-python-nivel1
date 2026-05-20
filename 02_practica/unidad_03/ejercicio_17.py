"""
Unidad 03 - Ejercicio 17

Hacer un programa para ingresar las notas del primer y segundo parcial de un
alumno y mostrar por pantalla:

    - “Aprobación directa” si ambas notas son 8 o más.
    - “Rinde examen final” si ambas notas son 6 o más, pero no cumple la condición anterior.
    - “Debe recuperar” si alguna de las notas es menor a 6.

"""

# Pedir datos
primer_parcial = int(input("Ingrese la nota del primer parcial: "))
segundo_parcial = int(input("Ingrese la nota del segundo parcial: "))

# Mostrar regularidad del alumno
if primer_parcial >= 8 and segundo_parcial >= 8:
    print("Aprobacion directa")
elif primer_parcial >= 6 and segundo_parcial >= 6:
    print("Rinde examen final")
else:
    print("Debe recuperar")