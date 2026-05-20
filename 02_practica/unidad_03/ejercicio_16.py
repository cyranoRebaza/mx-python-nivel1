"""
Unidad 03 - Ejercicio 16

Una empresa que vende desinfectantes necesita un programa para calcular el
importe final de una venta. Se ingresan el importe total y la cantidad de litros
vendidos. Aplicar los siguientes descuentos según la cantidad de litros:

    - Menos de 100 litros: sin descuento.
    - Entre 100 y 300 litros inclusive: 10% de descuento.
    - Entre 301 y 500 litros inclusive: 15% de descuento.
    - Más de 500 litros: 25% de descuento.

Mostrar el importe final con el descuento aplicado.

"""
# Constantes
PORCENTAJE_25 = 0.25
PORCENTAJE_15 = 0.15
PORCENTAJE_10 = 0.10


# Pedir datos
importe_total = float(input("Ingrese el importe total: "))
cantidad_litros = int(input("Ingrese la cantidad de litros: "))


# Calcular descuento
descuento = 0

if cantidad_litros > 500:
    descuento = importe_total * PORCENTAJE_25    
elif cantidad_litros > 300:
    descuento = importe_total * PORCENTAJE_15
elif cantidad_litros >= 100:
    descuento = importe_total * PORCENTAJE_10    
    
# Calcular importe final
importe_final = importe_total - descuento
    
# Mostrar el resultado
print(f"El importe final es: ${importe_final:.2f}")
    
    