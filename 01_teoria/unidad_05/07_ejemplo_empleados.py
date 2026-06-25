# ==============================================================================
# unidad 05: Ejemplo 2 - Lista de empleados
# ==============================================================================

"""
Hacer un programa para cargar el legajo (entero de 5 digitos) y el sueldo de los 
empleados de un comercio, corta con legajo igual a cero

- mostrar el legajo y el sueldo de aquellos empleados con sueldo mayor al
promedio

"""

# crear lista paralela
lista_legajos = []
lista_sueldos = []

# cargar los datos
legajo = int(input("Ingrese el legajo (0 para terminar): "))

while legajo != 0:
    sueldo = float(input("Ingrese el sueldo: "))
    lista_legajos.append(legajo)
    lista_sueldos.append(sueldo)

    legajo = int(input("Ingrese el legajo (0 para terminar): "))

# calcular el promedio
cantidad_elementos = len(lista_sueldos)
suma_sueldos = sum(lista_sueldos)
promedio_sueldos = suma_sueldos / cantidad_elementos
print(f"Promedio: {promedio_sueldos}")

# buscar el sueldo mayor
for i in range(len(lista_sueldos)):
    if lista_sueldos[i] > promedio_sueldos:
        print(f"Sueldo mayor al promedio: {lista_sueldos[i]} ")
        print(f"Legajo: {lista_legajos[i]} ")
