# ====================================================
# unidad 03: match-case (python 3.10)
# ==================================================== 


"""
match-case:
 
 - proporciona un SISTEMA DE COINCIDENCIA DE PATRONES
 - es similar a switch-case(compara valores) match-case(comparar estructura de datos)

sintaxis de match-case

match variable:
    case patron1:
        # codigo que se ejecuta si el patron1 coincide
    case patron2:
        # codigo que se ejecuta si el patron2 coindice
    case _:
        # codigo que se ejecuta si no coincide ningun patron
 
    - match variable: el la variable o expresion que se evalua para hacer
    coincidir con uno o mas patrones
    
    - case patron1: define cada patron y bloque de codigo que se ejecutar si el valor
    coincide con el patron
    
    - _(guion bajo): es un comodin(caso por defecto) que coincide con cualquier valor y se usa para CAPTURAR
    TODOS LOS CASOS que no coinciden con ningun patron anterior
    similiar al default en switch-case



"""

# ejemplo1: 

# 1. La variable fruta es evaluada por match.
# 2. Cada case especifica un valor posible para fruta.
# 3. Si no hay coincidencia, se ejecuta el bloque del caso _.

fruta = input("Ingrese una fruta: ")

match fruta:
    case "manzana":
        print("Es una fruta roja y verde")
    
    case "banana":
        print("Es una fruta amarilla")
        
    case "naranja":
        print("Es una fruta anaranjada")
    
    case _:
        print("No tengo informacion sobre esa fruta")
        

# ejemplo2: comparar elif con match
 
# escribir un programa que reciba el número de un día de la semana (donde 1 corresponde a
# Lunes, 2 a Martes, 3 a Miércoles, y así sucesivamente) e imprima el nombre del día
# correspondiente. Si el número ingresado no corresponde a un día válido, el programa debe
# mostrar el mensaje: "Día no válido".

# con if...elif...else:
dia = int(input("Ingrese un dia de semana: "))

if dia == 1:
    print("Lunes")
    
elif dia == 2:
    print("Martes")
    
elif dia == 3:
    print("Miercoles")
    
elif dia == 4:
    print("Jueves")

elif dia == 5:
    print("Viernes")
    
elif dia == 6:
    print("Sabado")
    
elif dia == 7:
    print("Domingo")

else:
    print("Dia no valido")
    
# con match
dia = int(input("Ingrese un dia de semana: "))

match dia:
    case 1:
        print("Lunes")
    case 2:
        print("Martes")
    case 3:
        print("Miercoles")
    case 4:
        print("Jueves")
    case 5:
        print("Viernes")
    case 6:
        print("Sabado")
    case 7:
        print("Domingo")
    case _:
        print("Dia no valido")
