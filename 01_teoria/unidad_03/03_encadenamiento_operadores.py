# ====================================================
# unidad 03: encadenamiento de operadores 
# ==================================================== 

# orden de precedencia:
# parentesis - orden precedencia(not-and-or) - izq a der(mismo nivel)


# ====================================================
# encadenamiento de comparacion(relacional)
# ==================================================== 
numero = 5

resultado = 1 < numero and numero < 10
print(resultado)  #imprime True

# equivalente
print(1 < numero < 10)  #imprime True, porque 5 esta entre 1 y 10


# ====================================================
# encadenamiento de operadodores logicos
# orden prioridad: not - and - or
# en operadores del mismo nivel de izq a der
# ==================================================== 

numero1 = 4
numero2 = 8
numero3 = 16

# usando multiples operadores logicos
#      (     True   and      True)    or      (True)
print((numero1 > 2 and numero2 < 20) or (numero3 == 15))  # imprime True

# por precedencia primero and, no se evalua de izquierda a derecha
#          (True)   or (       True   and      False)         
print((numero1 > 2) or (numero2 < 20 and numero3 == 15))  # imprime True

 


