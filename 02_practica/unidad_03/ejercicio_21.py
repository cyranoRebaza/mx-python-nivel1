"""
Unidad 03 - Ejercicio 21

Una casa de computación arma PCs a medida según la siguiente configuración:

         	i5 (1)	    i7 (2)	    i9 (3)
8 RAM (1)	USD 800	    USD 900	    USD 1200
16 RAM (2)	USD 900	    USD 1000	USD 1400
32 RAM (3)	USD 1000	USD 1400	USD 2000

Además, el equipo viene con un disco que permite almacenar 500 GB de información
y que se puede ampliar a 1 TB si así lo desea, lo cual tiene un costo adicional
de USD 300.

Hacer un programa que solicite la opción de procesador, la opción de
memoria RAM, y si extiende el disco o no (se ingresa 1 para exender y 0 para no 
extender) y calcule y emita por pantalla el monto de la máquina a seleccionada.

"""
# Constantes
PRECIO_EXTENSION_DISCO = 300

# Menu de opciones
print("************************")
print("**** MENU PRINCIPAL ****")
print("************************")
print()
print("**** OPCIONES DE PROCESADOR ****")
print("1. procesador i5")
print("2. procesador i7")
print("3. procesador i9")

procesador = int(input("Ingrese el procesador: "))

print()

print("**** OPCIONES DE MEMORIA RAM ****")
print("1. 8 GB RAM")
print("2. 16 GB RAM")
print("3. 32 GB RAM")

memoria_ram = int(input("Ingrese la memoria ram: "))

print()

print("**** OPCIONES EXTENDER DISCO ****")
print("0. no extender disco")
print("1. extender disco")

extender_disco = int(input("Extender disco: "))

# calcular precio base
match procesador:
    case 1:
        match memoria_ram:
            case 1:
                precio_base = 800
            case 2:
                precio_base = 900
            case 3:
                precio_base = 1000
                
    case 2:
        match memoria_ram:
            case 1:
                precio_base = 900
            case 2:
                precio_base = 1000
            case 3:
                precio_base = 1400
                
    case 3:
        match memoria_ram:
            case 1:
                precio_base = 1200
            case 2:
                precio_base = 1400
            case 3:
                precio_base = 2000
                
# Calcular precio final
if not extender_disco:
    precio_final = precio_base
else:
    precio_final = precio_base + PRECIO_EXTENSION_DISCO
    
# Mostrar precio final
print()
print(f"El precio final es ${precio_final}")
                
                