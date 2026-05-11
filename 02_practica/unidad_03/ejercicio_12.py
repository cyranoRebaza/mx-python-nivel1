"""
Unidad 03 - Ejercicio 12

Hacer un programa para ingresar un valor que estará expresado en minutos. Si
los minutos superan los 60, pasar el valor a horas, de lo contrario dejarlo en
minutos. Mostrar el resultado en pantalla aclarando si se muestran minutos u
horas.

"""

# Pedir datos
minutos = int(input("Ingrese los minutos: "))

# calcular y mostrar
if minutos >= 60:
    horas = minutos // 60
    minutos_restante = minutos % 60

    print(f"Hora: {horas} h")
    print(f"Minutos: {minutos_restante} min")
    
else:
    print(f"Minutos: {minutos} min")
    