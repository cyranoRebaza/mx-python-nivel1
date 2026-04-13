"""
Unidad 02 - Ejercicio 09

Una universidad desea conocer los porcentajes de mujeres y hombres en las
carreras de ciencias exactas. Se solicita un programa para cargar la cantidad de
mujeres y la cantidad de hombres y que el mismo calcule y emita por pantalla los
porcentajes correspondientes.

"""
# Pedir datos
cantidad_hombres = int(input("Ingrese la cantidad de hombres: "))
cantidad_mujeres = int(input("Ingrese la cantidad de mujeres: "))

# Calcular el porcentaje
cantidad_total = cantidad_hombres + cantidad_mujeres
porcentaje_hombres = cantidad_hombres * 100 / cantidad_total
porcentaje_mujeres = 100 - porcentaje_hombres

# Mostrar el porcentaje
print(f"El porcentaje de hombres es: {porcentaje_hombres:.2f} %")
print(f"El porcentaje de mujeres es: {porcentaje_mujeres:.2f} %")
