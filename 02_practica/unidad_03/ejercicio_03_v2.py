"""
Unidad 03 - Ejercicio 03 (v2)

Hacer un programa para ingresar dos números y que luego emita por pantalla el
mayor de ellos o un cartel aclaratorio “Son iguales” en el caso de que así sea.

Nota: los números pueden ser iguales.

"""
# Pedir datos
numero_1 = int(input("Ingrese primero numero: "))
numero_2 = int(input("Ingrese segundo numero: "))

# Calcular y mostrar
if numero_1 == numero_2:
    print("Son iguales")
    
elif numero_1 > numero_2:
    print(f"El mayor es el numero: {numero_1}")    

else:
    print(f"El mayor es el numero: {numero_2}")
    

