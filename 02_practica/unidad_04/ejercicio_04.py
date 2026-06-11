"""
Unidad 04 - Ejercicio 04

Hacer un programa que solicite UN número y luego calcule y emita un cartel 
aclaratorio si el mismo es primo o no es primo.  

Nota: un número es primo cuando es divisible únicamente por 1 y por sí mismo.

"""
# Pedir un numero
numero = int(input("Ingrese un numero: "))

# Buscar divisores
divisores = 0
for n in range(1, numero + 1):
    if numero % n == 0:
        divisores += 1

# Mostrar resultado
if divisores == 2:
    print(f"El numero {numero} es primo")
else:
    print(f"El numero {numero} no es primo")
