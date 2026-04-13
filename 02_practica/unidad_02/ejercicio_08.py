"""
Unidad 02 - Ejercicio 08

Una importante cadena de delivery cuenta con una promoción por tiempo
limitado en la que otorga un 15% de descuento sobre el total del valor de la
compra realizada. Hacer un programa para solicitar el monto total y el mismo
calcule y emita por pantalla el total a cobrar con el descuento aplicado.

"""


# Perdir datos
monto_total = float(input("Ingrese el monto total de la compra: "))

# Calcular el total a cobrar
PORCENTAJE_DESCUENTO = 15
descuento = monto_total * PORCENTAJE_DESCUENTO / 100
total_cobrar = monto_total - descuento

# Mostrar el total a cobrar
print(f"El total a cobrar es: ${total_cobrar:.2f}")