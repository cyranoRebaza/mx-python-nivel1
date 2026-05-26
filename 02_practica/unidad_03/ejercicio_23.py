"""
Unidad 03 - Ejercicio 23

Hacer un programa para ingresar tres números y mostrarlos ordenados de menor a
mayor.

Nota: resolver el ejercicio utilizando estructuras condicionales e intercambios
(sin usar listas ni funciones de ordenamiento).

"""

# Pedir datos
numero_1 = int(input("Ingrese el numero 1: "))
numero_2 = int(input("Ingrese el numero 2: "))
numero_3 = int(input("Ingrese el numero 3: "))

# Ordenar de menor a mayor
if numero_1 <= numero_2 and numero_1 <= numero_3:
    menor = numero_1    
    if numero_2 <= numero_3:
        medio = numero_2
        mayor = numero_3
    else:
        medio = numero_3
        mayor = numero_2
        
if numero_2 <= numero_1 and numero_2 <= numero_3:
    menor = numero_2
    if numero_1 <= numero_3:
        medio = numero_1
        mayor = numero_3
    else:
        medio = numero_3
        mayor = numero_1
        
if numero_3 <= numero_1 and numero_3 <= numero_2:      
    menor = numero_3
    if numero_1 <= numero_2:
        medio = numero_1
        mayor = numero_2
    else:
        medio = numero_2
        mayor = numero_1
        
# Mostrar menor a mayor
print(f"menor: {menor}")
print(f"medio: {medio}")
print(f"mayor: {mayor}")

    