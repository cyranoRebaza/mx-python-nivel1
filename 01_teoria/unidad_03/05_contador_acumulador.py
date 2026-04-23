# ====================================================
# unidad 03: Contadores y acumuladores
# ==================================================== 


"""
 CONTADORES:
 
 - En una variable que sirve par contar
 - Por lo general se inicializa en cero
 - contar el agregar una unidad a una variable
 
a = 0
a = a + 1
a = a + 1
a = a + 1   # a += 1 (operador de acumulacion +=)
print(a) 

----------------------------------------------------------------
 ACUMULADORES:
 
 - En una variable que sirve para acumular
 - Por lo general se inicializa en cero
 - no se suma una unidad, sino distinto valores
 
a = 0
a = a + 10  # a += 10
a = a + 3
a = a + 5
print(a)  

"""

# Ejemplo: inicializar 4 edades con distintos valores y determinar:

# cuantas personas son mayores a 30
# calcular el promedio
# calcular el porcentaje

# inicializar variables
edad1 = 25
edad2 = 27
edad3 = 33
edad4 = 39


cantidad_personas = 4
contador = 0
acumulador = 0

# acumular y contar

if edad1 > 30:
    contador += 1
    acumulador += edad1
    
    
if edad2 > 30:
    contador += 1
    acumulador += edad2
    
if edad3 > 30:
    contador += 1
    acumulador += edad3
    
if edad4 > 30:
    contador += 1
    acumulador += edad4
    
# calcular promedio y porcentaje
if contador > 0:
    promedio = acumulador / contador
else:
    promedio = 0
    
porcentaje = contador * 100 / cantidad_personas
    
# mostrar 
    
print(f"mayores a 30: {contador}")
print(f"promedio: {promedio:.2f}")
print(f"porcentaje: {porcentaje:.2f} %")

