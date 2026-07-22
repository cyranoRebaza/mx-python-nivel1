# ==============================================================================
# unidad 05: Cadenas de Caracteres - STRING
# ==============================================================================

"""
cadenas de caracteres --> string

- Son inmutables
- son tipo str 
--------------------------------------------------------------------------------
Acceder a los caracteres 

- Cada caracter tiene una posición (indice)
 
--------------------------------------------------------------------------------
Recorrer una cadena

texto = "Python"

Recorrer con un for
for letra in texto:
    print(letra)

Recorrer por indice
for letra in range(len(texto))
    print(texto[letra])

--------------------------------------------------------------------------------
concatenacion de string

nombre = "Pepe"
apellido = "perez

nombre_completo = nombre + " " + apellido

print(nombre_completo)
--------------------------------------------------------------------------------
Repetir un string

prin("HOla " * 3)

--------------------------------------------------------------------------------
Operador in (verificar si una cadena contiene a la otra)

texto = "Python"

prin("py" in texto) # True
print("ico" in texto) # False

--------------------------------------------------------------------------------
Slicing --> Sirve para obtener un parte de la cadena

cadena[inicio:fin:paso]

invertir la cadena
cadena[::-1]


--------------------------------------------------------------------------------
Formato de cadenas --> f-strings

nombre = "Juan"
edad = 25

print(f"Me llamo {nombre} y tengo {edad} años.")

--------------------------------------------------------------------------------
Metodos mas utilizados:

- strip(): elimina espacios al principio y al final
- upper(): convierte a mayusculas
- lower(): convierte a minusculas
- capitalize(): primerea letra en mayuscula
- title(): cada palabra comienza con  mayuscula

- replace(): reemplaza texto
- split(): divide una cadena en una lista
- join(): une los elementos de una lista
- count(): cuenta cuantas veces aparece

"""
# Ejemplo 1: aceder a la primera letra de un nombre
nombre = "Juan"
print(f"La primera letra es: {nombre[0]}")
print()
# salida:
# j

# Ejemplo 2: Mostrar todos los elementos de nombre, tomando como lista y usando indices
for letra in nombre:
    print(f"Letra: {letra}")

print()
# salida:
# j
# u
# a
# n

for i in range(len(nombre)):
    print(nombre[i])

print()
# salida:
# j
# u
# a
# n

# Ejemplo 3: ver si en nombre exite la letra T
if "T" in nombre:
    print("La palabra nombre contiene T")
else:
    print("La palabra nombre NO contiene T")

print()
# salida:
# La palabra nombre NO contiene T

# Ejemplo 4: obtener un fragmento de una frase
frase = "Hola probando slicing"
fragmento = frase[1:4]

print()
# salida:
# ola

# Ejemplo 5: cuantas letras a tiene una frase y una lista de nombres
frase_larga = "cuantas veces aparece la letra a en frase larga"
lista_nombres = ["Pepe", "Juan", "Alberto", "Javier"]

# contando en una frase
cantidad = 0
for letra in frase_larga:
    if letra == "a":
        cantidad += 1

print(f"La frase tiene {cantidad},letras a.")

# contando para multiples nombres
for nombre in lista_nombres:
    cantidad = 0
    for letra in nombre:
        if letra == "a" or letra == "A":
            cantidad += 1
    print(f"El nombre tiene {cantidad}, letras a.")
