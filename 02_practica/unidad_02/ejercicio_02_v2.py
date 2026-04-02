"""
Unidad 02 - Ejercicio 02 (v2)

Hacer un programa para solicitar por teclado un número (base) y una potencia, y 
luego mostrar el resultado.

"""
# Pedir datos
base = int(input("Ingrese la base: "))
potencia = int(input("Ingrese la potencia: "))

# Calcular la potencia
resultado = base ** potencia

# Mostrar resultado
print(f"El resultado es: {resultado}")