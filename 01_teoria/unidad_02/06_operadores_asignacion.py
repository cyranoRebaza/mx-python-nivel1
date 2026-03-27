# ====================================================
# unidad 02: operadores de asignacion
# ==================================================== 

# Operadores de asignacion

#   - asignacion simple (=): asigna un valor a una variable
#   - asignacion con suma (+=): suma y asigna el resultado
#   - asignacion con resta (-=): resta y asigna el resultado
#   - asignacion con multiplicacion (*=): multiplica y asigna el resultado
#   - asignacion con division (/=): divide y asigna el resultado
#   - asignacion con division entera (//=): realiza una division entera y asigna el resultado
#   - asignacion con modulo (%): calcula el modulo y asigna el resultado 
#   - asignacion con exponente (**): Eleva a la potencia y asigna el resultado 


# ====================================================
# asignacion simple (=)
# ==================================================== 

variable = 5 # asigna el valor 5 a la variable x

print(variable)    # imprime 5


# ====================================================
# asignacion con suma (+=)
# ==================================================== 

numero = 5
numero += 3   # equivale a numero = numero + 3

print(numero)    # imprime 8

# ====================================================
# asignacion con resta (-=)
# ==================================================== 

numero = 10
numero -= 3   # equivale a numero = numero - 3

print(numero)    # imprime 7

# ====================================================
# asignacion con multiplicacion (*=)
# ==================================================== 

numero = 10
numero *= 3   # equivale a numero = numero * 3

print(numero)    # imprime 30

# ====================================================
# asignacion con division (/=)
# ==================================================== 

numero = 10
numero /= 2   # equivale a numero = numero / 2

print(numero)    # imprime 7

# ====================================================
# asignacion con division entera (//=)
# ==================================================== 

numero = 10
numero //= 3   # equivale a numero = numero // 3

print(numero)    # imprime 3

# ====================================================
# asignacion con modulo (%)
# ==================================================== 

numero = 10
numero %= 3   # equivale a numero = numero % 3

print(numero)    # imprime 1


# ====================================================
# asignacion con exponente (**)
# ==================================================== 

numero = 2
numero **= 3   # equivale a numero = numero ** 2

print(numero)    # imprime 8




# ====================================================
# Ejemplo:
# ==================================================== 
print("-----------------------------------------------")
# inicilizar variables
cantidad = 50
descuento = 10
interes = 5

# aplicar descuento e interes
cantidad -= descuento
cantidad += cantidad * (interes / 100)

# mostrar el precio final
print(f"El precio final con descuento e interes es: {cantidad}")