# ====================================================
# unidad 03: operadores relacionales o de comparacion
# ==================================================== 

# comparan dos valores y devuelven un valor boleano

# Operadores relacionales

#   - igual a (==): verifican si dos valores son iguales
#   - distinto de (!=): verifican si dos valores son diferentes
#   - mayor que (>): verificar si el valor de la izquierda es mayor que el de la derecha
#   - menor que (<): verificar si el valor de la izquierda es menor que el de la derecha
#   - mayor o igual que (>=): verificar si el valor de la izquierda es mayor o igual que la derecha
#   - menor o igual que (<=): verificar si el valor de la izquierda es menor o igual que la derecha

# ====================================================
# Ejemplo1: comparando numeros
# ==================================================== 
print(3 > 4)            # False
print(2 <= 4)           # True
print(2 != 22)          # True

print(10 == 10.0)       # True

# ====================================================
# Ejemplo2: comparando cadenas (orden lexicografico)
# Las cadenas se comparan cararcter por caracter (ASCII o Unicode)
# segun ASCII mayusculas < minusculas
# ==================================================== 
print("apple" < "banana")   # True
print("apple" > "Apple")    # True
print("apple" > "Apple")    # True

print("python" == "python") # True
print("Python" != "python") # True

print("A" < "a")            # True
print("z" > "Z")            # True


# ====================================================
# Ejemplo3: comparando numeros enteros y flotantes
# ==================================================== 
a = 10
b = 10.0

print(a == b) # True, porque 10 en igual a 10.0 en valor
