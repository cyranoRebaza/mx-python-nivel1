"""
Unidad 04 - Ejercicio 12

Hacer un programa que solicite números enteros positivos.
El programa deberá continuar solicitando números mientras la suma acumulada no 
supere los 100. Cuando la suma supere 100, el programa finaliza.
Al finalizar, informar:

- Cuántos números se ingresaron

- El valor total acumulado antes de superar 100

"""
cantidad_numeros = 0
suma_acumulada = 0

numero = int(input("Ingrese un numero: "))

while numero + suma_acumulada <= 100:
    cantidad_numeros += 1
    suma_acumulada += numero
    numero = int(input("Ingrese un numero: "))

print(f"Cantidad numeros ingresados: {cantidad_numeros}")
print(f"La suma acumulada es: {suma_acumulada}")
