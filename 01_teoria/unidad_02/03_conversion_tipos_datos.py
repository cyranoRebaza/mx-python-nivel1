# ====================================================
# unidad 02: conversion entre tipos de datos (casting)
# ==================================================== 

# conversion entre numeros enteros y numeros decimales
#   - int a float: usar funcion float(entero) 
#   - float a int: usar funcion int(decimal)


# conversion de numeros a cadenas de caracteres y viceversa
#   - int a str: usar funcion str(edad) 
#   - str a int: usar funcion int(cadena_numerica)


# conversion de numeros a cadenas de caracteres y viceversa
#   - bool a int: usar funcion int(valor_verdadero)
#   - int a bool: usar funcion bool(numero)

#-------------------------------------------------------------------------

# ===========================================================
# conversion entre numeros enteros y numeros decimales
# ===========================================================
# Ejemplo de int a float
entero = 10
decimal = float(entero)

print(decimal) # 10.0

# Ejemplo de float a int
decimal = 3.14
entero = int(decimal)

print(entero) # 3

# ===========================================================
# conversion de numeros a cadenas de caracteres y viceversa
# ===========================================================
# Ejemplo de int a str
edad = 25
mensaje = "Tengo " + str(edad) + " anios."

print(mensaje) # Tengo 25 anios.

# Ejemplo de str a int
cadena_numerica = "123"
numero = int(cadena_numerica)

print(numero + 7) # 130

# ===========================================================
# conversion de numeros a cadenas de caracteres y viceversa
# ===========================================================
# Ejemplo de int a bool
valor_verdadero = True
valor_falso = False

print(int(valor_verdadero)) # 1
print(int(valor_falso))     # 0

# Ejemplo de bool a int
numero = 0
print(bool(numero)) # False

numero = 5
print(bool(numero)) # True, cualquier numero distinto de 0 se convierte en True