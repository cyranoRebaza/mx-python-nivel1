# ==============================================================================
# unidad 05: Ejemplo 1 - registro de temperaturas
# ==============================================================================

"""
Hacer un programa para ingresar y guardar los registros de temperaturas del mes
pasado. por cada registro se ingresa en dia (1 a 31) y la temperatura

- mostrar la mayor temperatura y en que dia fue

"""

# crear lista de 31 dias
lista = [0] * 31

# cargar la temperatura
for i in range(len(lista)):
    dia = int(input("Ingrese el dia: "))
    temperatura = int(input("Ingrese la temperatura: "))
    lista[dia - 1] = temperatura


# buscar la mayor temperatura y dia
mayor_temperatura = lista[0]
dia_mayor_temperatura = 1

for i in range(len(lista)):
    if lista[i] > mayor_temperatura:
        mayor_temperatura = lista[i]
        dia_mayor_temperatura = i + 1


# Mostrar resultados
print(f"Mayor temperatura: {mayor_temperatura}")
print(f"Dia: {dia_mayor_temperatura}")
