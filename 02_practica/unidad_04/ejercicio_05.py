"""
Unidad 04 - Ejercicio 05

Hacer un programa que solicite 20 números y luego emitir por pantalla el máximo 
de los números pares y el mínimo de los números impares.

"""

# Inicializar variables
hay_par = False
hay_impar = False

# Pedir los numeros
for n in range(20):
    numero = int(input("Ingrese un numero: "))

    if numero % 2 == 0:
        if not hay_par:
            maximo_par = numero
            hay_par = True
        elif numero > maximo_par:
            maximo_par = numero

    else:
        if not hay_impar:
            minimo_impar = numero
            hay_impar = True
        elif numero < minimo_impar:
            minimo_impar = numero

# Mostrar el maximo par y minimo impar
if hay_par:
    print(f"El maximo par es: {maximo_par}")
else:
    print("No se ingresaron numeros pares")

if hay_impar:
    print(f"El minimo impar es: {minimo_impar}")
else:
    print("No se ingresaron numeros impares")
