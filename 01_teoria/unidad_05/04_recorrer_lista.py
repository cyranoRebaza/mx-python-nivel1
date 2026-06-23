# ==============================================================================
# unidad 05: recorrido de listas
# ==============================================================================

"""
1. usando for range() e indice

numeros = [10, 20, 30, 40, 50]

for i range(len(numeros)):
    print(f" indice {i}: elemento {numeros[i]})

--------------------------------------------------------------------------------
2. usando for --> el numero va tomando el valor de la lista

numeros = [10, 20, 30, 40, 50]

for numero in numeros:
    print(numero)

--------------------------------------------------------------------------------
2. usando while --> 

numeros = [10, 20, 30, 40, 50]

i = 0
while i < len(numeros):
    print(numeros[i])
    i += 1


--------------------------------------------------------------------------------
len(numeros) --> cantidad de elementos
range(...) --> genera indices
numeros[i] --> acede al elemento en esa posicion
 
--------------------------------------------------------------------------------


"""
lista = [10, 20, 30, 40, 50]

# usando los indices
print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])
print(lista[4])

print()

# aceder al ultimo elemento usando indices negativos
print(lista[-1])  # imprime: 50
print(lista[-2])  # imprime: 40
print(lista[-3])  # imprime: 30
print(lista[-4])  # imprime: 20
print(lista[-5])  # imprime: 10

print()

# acceder al ultimo elemento usando la funcion len()
print(lista[len(lista) - 1])  # imprime: 50

print()

# recorrer una lista conociendo la cantidad de elementos
for i in range(5):
    print(f"poscion {i}: {lista[i]}")

print()

# recorrer una lista usando range y len e indices
for i in range(len(lista)):
    print(f"poscion {i}: {lista[i]}")

print()

# recorrer una lista desde ultimo elemento usando for y range
for i in range(-1, (len(lista) + 1) * -1, -1):
    print(f"poscion {i}: {lista[i]}")

#  recorrer directamente cada elemento
for elemento in lista:
    print(elemento)
