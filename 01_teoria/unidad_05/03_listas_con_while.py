# ==============================================================================
# unidad 05: listas con while  (append - pop - remove) - (len - sum)
# ==============================================================================

"""
metodos y funciones: diferencia esta en como se llaman

metodos: pertenece a un objeto y se usa con punto (.)
funcion: una funcion se llama directamente por su nombre

--------------------------------------------------------------------------------
 funcion len() --> Obtener la cantidad de elementos en una lista

ejemplo
frutas = ["Manzana", "Naranja", "Platanos"]

print(len(frutas)) # imprime: 3

funcion sum() --> sumar los elementos numericos de una lista 

ejemplo
numeros = [1, 2, 3, 4]
print(sum(numeros)) # imprime: 10


--------------------------------------------------------------------------------
Eliminar elemento de una lista

-metodo remove(): 
    Elimina el primer elemento que coincida con el valor especifico
    
numeros = [10,, 20, 30, 40]
numeros.remove(20)
print(numeros) # [10, 30, 40]


- metodo pop():
    Elimina un elemento por indice y lo devuelve, si no se indica elimina el
    ultimo
    
numeros = [10, 20, 30]
elemento_eliminado = numeros.pop(1)
print(numeros) # [10,30]

    
-del: es una instruccion
    Elimina un elemento o una porcion de la lista

elimar por indice
numeros =[10, 20, 30]
del numeros[1]
print(numeros) # [10, 30]

eliminar un rango
numeros =[10, 20, 30, 40, 50, 60]
del numeros[1:4]
print(numeros) # [10, 50, 60]

eliminar una variable
numero = 10
del numero

 
--------------------------------------------------------------------------------


"""
# Ejemplo 1: Hacer un programa para ingresar una lista de numeros que cortan con
# un cero y luego calcular el promedio, al final mostrar por pantalla aquellos
# numeros mayores al promedio

# Cargar datos en la lista
lista_numeros = []
numero = int(input("Ingrese un numero: "))
while numero != 0:
    lista_numeros.append(numero)
    numero = int(input("Ingrese un numero: "))


# Calcular el promedio
promedio = sum(lista_numeros) / len(lista_numeros)
print(f"Promedio: {promedio}")

# buscar los numeros mayores que el promedio
for i in range(len(lista_numeros)):
    if lista_numeros[i] > promedio:
        print(f"numero mayor al promedio: {lista_numeros[i]}")
