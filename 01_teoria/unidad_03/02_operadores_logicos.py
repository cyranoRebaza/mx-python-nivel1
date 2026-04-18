# ====================================================
# unidad 03: operadores lógicos
# ==================================================== 

# Permite evaluar multiples expreseiones booleanas en una condicion
# expresiones que resultan en True o False

# Operadores relacionales

#   - operador AND (and): devuelve True si ambas condiciones son verdaderas
#   - operador OR (or): develve True SI AL MENOS UNA de las condiciones es verdadera
#   - operador NOT (not): invierte el valor booleano de la condición


# ====================================================
# operador logico AND(and)
# ==================================================== 
numero1 = 5
numero2 = 10

resultado = numero1 > 2 and numero2 < 15
print(resultado) # imprime True, ambas condiciones son verdaderas

resultado = numero1 > 6 and numero2 < 15
print(resultado) # imprime False, una de las condiciones es falsa


# ====================================================
# operador logico OR(or)
# ==================================================== 
numero1 = 50
numero2 = 100

resultado = numero1 > 20 or numero2 < 150
print(resultado) # imprime True, una de las condiciones es verdadera

resultado = numero1 > 60 and numero2 > 150
print(resultado) # imprime False, porque ambas condiciones son falsas


# ====================================================
# operador logico NOT(not)
# ==================================================== 
numero3 = 50


resultado = not numero3 > 20
print(resultado) # imprime False, porque la expresion fue True

resultado = not numero3 > 60
print(resultado)  # imprime True, porque la expresion fue False


