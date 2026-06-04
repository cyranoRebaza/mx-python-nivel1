# ==============================================================================
# unidad 04: repititivas - ciclo for
# ==============================================================================

"""
bucle for en otros leguajes

iterar--> reloj
(inicializacion; condicion; incremento)
i = 0; i < 5; i += 1
i = 0; i < 10; i += 2

inicio-fin-paso
--------------------------------------------------------------------------------

bucle for en python
 
es una estructura de control que se utiliza para iterar sobre una secuencia 
(como rango numero, listas, tuplas, conjuntos, diccionarios, o cadenas de texto) 
y realizar una acción por cada elemento de la secuencia.

--------------------------------------------------------------------------------
sintaxis del bucle for

for variable in secuencia:
    # codigo que se ejecuta para cada elemento en la secuencia

variable: representa el elemento actual de la secuencia en cada iteracion
secuencia: cualquier objeto iterable --> lista,tupla,cadena
    
--------------------------------------------------------------------------------
que es range()

es una clase sirve para generar secuencia de numeros

sintaxis basica: range(inicio, fin, paso)
    - inicio: Es el número donde comienza la secuencia (es opcional, por defecto 
    es 0).
    - fin: Es el número donde termina la secuencia (no incluye este valor).
    - paso: Es el intervalo entre cada número de la secuencia (opcional, por 
    defecto es su valor es 1).

uso de range()
    - range(fin)
    - range(inicio,fin)
    - range(inicio,fin,paso)

--------------------------------------------------------------------------------


"""
# Ejemplo 1: iterando sobre una lista de nombre
nombres = ["Ana", "Carlos", "Beatriz"]

for nombre in nombres:
    print(f"Hola, {nombre}!")

print()
# salida:
# Hola, Ana!
# Hola, Carlos!
# Hola, Beatriz!

# Ejemplo 2: iterar sobre una cadena de texto
palabra = "python"

for letra in palabra:
    print(f"letra: {letra}")

print()
# salida:
# Letra: P
# Letra: y
# Letra: t
# Letra: h
# Letra: o
# Letra: n


# Ejemplo 3: uso basico de range()
for i in range(5):
    print(f"Iteración número {i}")

print()
# salida:
# Iteración número 0
# Iteración número 1
# Iteración número 2
# Iteración número 3
# Iteración número 4

# bucle itera sobre los numeros del 0 al 4, genera los numeros 0,1,2,3,4
# cada numero se asigna a la variable i
# bloque imprime el numero de la iteracion


# Ejemplo 4: range(inicio,fin) con valor de inicio y fin
for i in range(3, 7):
    print(i)

print()
# salida:
# 3
# 4
# 5
# 6

# range(3, 7) genera los numeros del 3 al 6, porque 7 es el limte superior, pero
# no esta incluido


# Ejemplo 5: el parametro paso
for i in range(0, 10, 2):
    print(i)

print()
# salida:
# 0
# 2
# 4
# 6
# 8

# range(0, 10, 2) genera numeros desde 0 hasta 8, saltando de 2 en 2


# Ejemplo 6: secuencia decreciente
for i in range(10, 0, -2):
    print(i)

print()
# salida:
# 10
# 8
# 6
# 4
# 2

# range(10, 0, -2) genera numeros desde 10 hasta 2, restando de 2 en 2


# Ejemplo 7: uso range() para recorrer listas
frutas = ["manzana", "banana", "naranja"]

for i in range(len(frutas)):
    print(f"Fruta {i + 1}: {frutas[i]}")

print()
# salida
# Fruta 1: manzana
# Fruta 2: banana
# Fruta 3: naranja
