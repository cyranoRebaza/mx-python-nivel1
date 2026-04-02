"""
Unidad 02 - Ejercicio 03

Hacer un programa que permita ingresar el año actual y el año de la fecha de
nacimiento de una persona y luego calcule y emita por pantalla su edad.

Nota: no hay que tener en cuenta si la persona cumplió años o no, simplemente
calcular.

"""

# Pedir datos
anio_actual = int(input("Ingrese el año actual: "))
anio_nacimiento = int(input("Ingrese el año de nacimiento: "))

# Calcular la edad
edad = anio_actual - anio_nacimiento

# Mostrar la edad
print(f"La edad de la persona es: {edad}")