"""
Unidad 03 - Ejercicio 20

Una empresa que vende detergente desea calcular el importe final de una venta 
según la cantidad de litros vendidos:

    - Hasta 50 litros: ARS 25 por litro.
    - Entre 51 y 200 litros: ARS 20 por litro.
    - Entre 201 y 500 litros: ARS 15 por litro.
    - Más de 500 litros: ARS 10 por litro.

Además, si el cliente paga en efectivo, se aplica un recargo del 10%.

Hacer un programa que solicite la cantidad de litros vendidos y el tipo de pago
(ingresará 1 si paga en efectivo y 0 con cualquier otro medio de pago) y calcule
y emita por pantalla el monto final a abonar por el cliente.

"""

# Constante
RECARGO_10 = 0.10

# Pedir datos
cantidad_litros = int(input("Ingrese la cantidad de litros vendidos: "))
tipo_pago = int(input("Ingrese tipo de pago (1. efectivo | 0. otro medio pago): "))

# Calcular el monto final
if cantidad_litros > 500:
    precio_litro = 10
elif cantidad_litros > 200:
    precio_litro = 15
elif cantidad_litros > 50:
    precio_litro = 20
else:
    precio_litro = 25
    
monto_final = cantidad_litros * precio_litro

if tipo_pago == 1:
    monto_final += monto_final * RECARGO_10
    
# Mostrar el monto final
print(f"El monto final es: ${monto_final:.2f}")
