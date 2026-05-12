"""
Unidad 03 - Ejercicio 14

Hacer un programa para ingresar dos números y luego calcular:
    - La resta si el primero es mayor que el segundo.
    - La suma si son iguales.
    - El producto si el primero es menor que el segundo.

Mostrar el resultado por pantalla según corresponda.

"""

# Pedir datos
numero_1 = int(input("Ingrese un numero: "))
numero_2 = int(input("Ingrese un numero: "))

# Calcular y mostrar
if numero_1 > numero_2:
    resultado = numero_1 - numero_2
    print(f"Resta: {resultado}")
    
elif numero_1 == numero_2:
    resultado = numero_1 + numero_2
    print(f"Suma: {resultado}")
    
else:
    resultado = numero_1 * numero_2
    print(f"Producto: {resultado}")
