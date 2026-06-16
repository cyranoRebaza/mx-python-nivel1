"""
Unidad 04 - Ejercicio 09

Hacer un programa que solicite números enteros.El programa deberá continuar 
solicitando números mientras cada nuevo número sea menor o igual al anterior.
Cuando se ingrese un número mayor al anterior, el programa finaliza.
Al finalizar, informar:

- La cantidad de números ingresados

- El último número válido ingresado

"""
cantidad_numeros = 0

numero = int(input("Ingrese un numero: "))
numero_anterior = numero

while numero <= numero_anterior:
    cantidad_numeros += 1
    numero_anterior = numero
    numero = int(input("Ingrese un numero: "))

print(f"Cantidad de numeros ingresados: {cantidad_numeros}")
print(f"El ultimo numero valido ingresado: {numero_anterior}")
