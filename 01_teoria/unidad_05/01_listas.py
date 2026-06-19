# ==============================================================================
# unidad 05: listas
# ==============================================================================

"""
Listas en pyhton

- es una coleccion ordenada y mutable(modificar despues de ser creados)
- los elementos se define entre corchetes [] y separados por comas
- almacenar multiples valores del mismo tipo o diferentes tipos
--------------------------------------------------------------------------------
Lista en otros lenguaje comparado con python

c++
- vector estatico: 
- tipo de dato es estatico y unico
int numeros[10]

python
- el tipo de dato y elementos es dinamico
 
--------------------------------------------------------------------------------
crear una lista vacia
    lista_vacia = []

crear una lista con elementos
- colocar los elementos entre corchetes, separados por comas

ejemplo de una lista de numeros
numeros = [1, 2, 3, 4, 5]

ejemplo de una lista de cadenas
frutas = ["manzana", "pera", "platano"]

ejemplo de una lista mixta
lista_mixta = [1, "Hola", True, 3.14]
    
--------------------------------------------------------------------------------
acceder a los elementos
frutas = ["manzana", "pera", "platano"]

elemento_1 = frutas[0] 
elemento_2 = frutas[1]
elemento_3 = frutas[2]

aceder a elementos con indices negativos
print(frutas[-1]) # imprime: platano
--------------------------------------------------------------------------------
Modificar los elementos de una lista (mutables)
numeros = [1, 2, 3, 4, 5]

cambiar el tercer elemento
numeros[2] = 10

--------------------------------------------------------------------------------

"""
# Ejemplo 1: aceder a una lista de numeros y mostrar usando indice
lista_numeros = [1, 2, 3, 4, 5]

print(f"El elemento 1 es: {lista_numeros[0]}")
print(f"El elemento 1 es: {lista_numeros[1]}")
print(f"El elemento 1 es: {lista_numeros[2]}")
print(f"El elemento 1 es: {lista_numeros[3]}")
print(f"El elemento 1 es: {lista_numeros[4]}")

print()
# salida:
# 1
# 2
# 3
# 4
# 5

# Ejemplo 2: mostrar los valores de la lista de numeros usando range()
for i in range(5):
    print(f"El elemento {i} es: {lista_numeros[i]}")

print()
# salida:
# 1
# 2
# 3
# 4
# 5
