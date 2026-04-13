"""
Unidad 02 - Ejercicio 07

Hacer un programa para ingresar por teclado los metros cuadrados totales de un
predio y los metros cuadrados cubiertos; luego calcular y mostrar por pantalla
el porcentaje de metros cuadrados cubiertos y el porcentaje de metros cuadrados
descubiertos.

"""

# Pedir datos
metros_totales = float(input("Ingrese los metros cuadrados totales: "))
metros_cubiertos = float(input("Ingrese los metros cubiertos: "))

# Calcular porcentajes

porcentaje_metros_cubiertos = metros_cubiertos * 100 / metros_totales
porcentaje_metros_descubiertos = 100 - porcentaje_metros_cubiertos

# Mostrar porcentajes
print(f"metros cubiertos: {porcentaje_metros_cubiertos:.2f} %")
print(f"metros descubiertos: {porcentaje_metros_descubiertos:.2f} %")