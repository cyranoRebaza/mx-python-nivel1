"""
Unidad 03 - Ejercicio 03 (v3)

Hacer un programa para ingresar dos números y que luego emita por pantalla el
mayor de ellos o un cartel aclaratorio “Son iguales” en el caso de que así sea.

Nota: los números pueden ser iguales.

------------------------------------
criterio: buscamos directamente el mayor y porque son solo dos numeros

"""
# Pedir datos
numero_1 = int(input("Ingrese primero numero: "))
numero_2 = int(input("Ingrese segundo numero: "))

# Calcular y mostrar
if numero_1 > numero_2:    
    print(f"El mayor es el numero: {numero_1}")
    
elif numero_2 > numero_1:
    print(f"El mayor es el numero: {numero_2}")    

else:
    print("Son iguales")
    

