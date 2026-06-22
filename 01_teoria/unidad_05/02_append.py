# ==============================================================================
# unidad 05: listas con for - metodo append()
# ==============================================================================

"""
metodo append()

- sirve para agregar un elemento al final de la lista

sintaxis
lista.append(elemento)

- lista: la lista donde se agrega algo
- elemento: el valor que se agrega al final
--------------------------------------------------------------------------------
ejemplo: agregar un numero

numeros = [1, 2, 3]
numeros.append(4)
print(numeros)

salida: [1, 2, 3, 4]
 
--------------------------------------------------------------------------------


"""
# Ejemplo 1: Hacer un programa para ingresar 10 numeros en una lista, luego
# calcular el promedio luego mostrar por pantalla aquellos numeros mayores
# al promedio


# Cargar dato en  la lista
lista = []
for i in range(10):
    numero = int(input("Ingrese un numero: "))
    lista.append(numero)

# Recorrer la lista para obtener la suma
suma_elementos = 0
for i in range(10):
    suma_elementos += lista[i]

# calular el promedio
promedio = suma_elementos / 10

# Buscar el mumero mayor que el promedio
for i in range(10):
    if lista[i] > promedio:
        print(f"El numero {lista[i]} es mayor que el promedio {promedio}")
