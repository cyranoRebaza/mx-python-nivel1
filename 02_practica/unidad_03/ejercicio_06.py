"""
Unidad 03 - Ejercicio 06

Una casa de video juegos otorga un descuento dependiendo del importe de la
compra realizada según los siguientes valores:

    - Si el importe es menor a ARS 1000, no hay descuento.
    - Si el importe es ARS 1000 o más pero menor a ARS 5000, aplica un descuento del 10%.
    - Si el importe es ARS 5000 o más, aplica un descuento del 18%.

Hacer un programa para ingresar un importe de venta y luego muestre por
pantalla el importe final con el descuento que corresponda.

"""
# Pedir datos
importe_venta = float(input("ingrese el importe de la venta: "))

PORCENTAJE_DESCUENTO_10 = 0.10
PORCENTAJE_DESCUENTO_18 = 0.18

IMPORTE_LIMITE_1 = 5000
IMPORTE_LIMITE_2 = 1000

# proceso
if importe_venta >= IMPORTE_LIMITE_1:
    descuento = importe_venta * PORCENTAJE_DESCUENTO_18
    importe_final = importe_venta - descuento

elif importe_venta >= IMPORTE_LIMITE_2:
    descuento = importe_venta * PORCENTAJE_DESCUENTO_10
    importe_final = importe_venta - descuento

else:
    importe_final = importe_venta


# Mostrar importe final
print(f"El importe final es: $ {importe_final:.2f}")

