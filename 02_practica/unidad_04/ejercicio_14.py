"""
Unidad 04 - Ejercicio 14

Se dispone de una lista de 5 listas de números enteros separados entre ellos por
ceros. Se pide determinar e informar:

- El número de grupo con mayor porcentaje de números impares respecto al total 
de números que forman el grupo.

- Informar cuántos grupos están formados por todos números ordenados de mayor a 
menor.

"""
# Punto a)
mayor_porcentaje_impares = 0
cantidad_grupos_ordenados = 0
numero_grupo = 0

for i in range(5):
    # Punto a)
    cantidad_impares = 0
    cantidad_numeros_grupo = 0

    numero = int(input("Ingrese un numero: "))
    # Punto b)
    numero_anterior = numero
    esta_ordenado = True

    while numero != 0:
        # Punto a)
        cantidad_numeros_grupo += 1
        if numero % 2 != 0:
            cantidad_impares += 1

        # Punto b)
        if numero <= numero_anterior:
            numero_anterior = numero
        else:
            esta_ordenado = False
        numero = int(input("Ingrese un numero: "))

    # Punto a)
    porcentaje_impares = cantidad_impares * 100 / cantidad_numeros_grupo
    if porcentaje_impares > mayor_porcentaje_impares:
        mayor_porcentaje_impares = porcentaje_impares
        numero_grupo = i + 1

    # Punto b)
    if esta_ordenado:
        cantidad_grupos_ordenados += 1

# Punto a)
print(f"El numero de grupo con mayor porcentaje de impares es: {numero_grupo}")
# punto b)
print(f"La cantidad de grupos ordenados: {cantidad_grupos_ordenados}")
