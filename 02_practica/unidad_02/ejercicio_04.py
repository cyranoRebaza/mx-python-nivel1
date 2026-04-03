"""
Unidad 02 - Ejercicio 04

Hacer un programa que permita ingresar los kilómetros existentes entre dos
ciudades y la velocidad promedio de un vehículo. Calcular y emitir por pantalla
el tiempo aproximado que demandará llegar de un punto a otro teniendo en cuenta
los datos ingresados.

nota:
se usa : .2f formatea el numero para mostrar(no cambia el valor)
round() redondea el numero y devuelve un nuevo valor

"""

# Pedir datos
kilometros = int(input("Ingrese la distancia (km): "))
velocidad_promedio = int(input("Ingrese la velocidad promedio (km/h): "))

# Calcular el tiempo
tiempo = kilometros / velocidad_promedio
tiempo_redondeado = round(tiempo, 2)

# Mostrar el tiempo
print(f"El tiempo aproximado es: {tiempo} horas")
print(f"El tiempo aproximado es: {tiempo:.2f} horas")
print(f"El tiempo aproximado es: {tiempo_redondeado} horas")