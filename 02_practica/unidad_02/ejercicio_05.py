"""
Unidad 02 - Ejercicio 05

Una casa de computación paga a sus empleados un sueldo fijo de ARS15000 más una
comisión del 5% sobre el total facturado por cada empleado. Hacer un programa
para ingresar el total facturado por un empleado y que luego calcule y emita por
pantalla el sueldo total a cobrar por el mismo.

"""
# Pedir datos
total_facturado = float(input("Ingrese el total facturado: "))

# Calcular sueldo total
SUELDO_FIJO = 15000
PORCENTAJE_COMISION = 5

comision = (PORCENTAJE_COMISION / 100) * total_facturado

sueldo_total = SUELDO_FIJO + comision

# Mostrar el sueldo total
print(f"El sueldo total es: $ {sueldo_total:.2f}")