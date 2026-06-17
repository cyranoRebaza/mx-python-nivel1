"""
Unidad 04 - Ejercicio 13

Hacer un programa para ingresar 10 números. El mismo debe analizar y mostrar por 
pantalla cuántos de esos números son primos.

"""
cantidad_primos = 0

for i in range(10):
    numero = int(input("Ingrese un numero: "))

    # buscar primos
    cantidad_divisores = 0
    for j in range(1, numero + 1):
        if numero % j == 0:
            cantidad_divisores += 1

    if cantidad_divisores == 2:
        cantidad_primos += 1

# Mostrar la cantidad de primos
print(f"La cantidad de primos es: {cantidad_primos}")
