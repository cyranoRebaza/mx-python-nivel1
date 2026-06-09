"""
Unidad 04 - Ejercicio 03

Hacer un programa que solicite 20 edades y luego calcule el promedio de edad de 
aquellas personas mayores a 18 años.

"""
# Pedir edades acumular y contar
cantidad_edad = 0
suma_edad = 0
for i in range(20):
    edad = int(input("Ingrese una edad: "))
    if edad > 18:
        cantidad_edad += 1
        suma_edad += edad

# Calcular el promedio de edades
if cantidad_edad > 0:
    promedio_edades = suma_edad / cantidad_edad
    # Mostrar el promedio de edades
    print(f"El promedio de edades es: {promedio_edades:.2f}")
else:
    print("Todas las edades ingresadas fueron menor o iguales a 18 años")
