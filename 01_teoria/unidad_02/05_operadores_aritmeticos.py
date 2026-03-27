# ====================================================
# unidad 02: operadores aritmeticos
# ==================================================== 

# Operadores aritmeticos

#   - suma (+): suma dos valores
#   - resta (-): resta el segundo valor del primero
#   - multiplicacion (*): multiplica dos valores
#   - division (/): divide el primer valor entre el segundo (siempre retorna flotante)
#   - division entera (//): divide el primer valor entre el segundo y redondea hacia abajo para obtener numero entero
#   - modulo (%): retorna o devuelve el sobrante de la division entre el primer y segundo valor 
#   - exponente (**): Eleva el primer valor a la potencia del segundo 

#   nota: convertir el valor de input() a numero (int o float)


# ====================================================
# operador de suma (+)
# ==================================================== 

numero1 = 5
numero2 = 3

resultado = numero1 + numero2

print(resultado)    # imprime 8

# ====================================================
# operador de resta (-)
# ==================================================== 

numero1 = 10
numero2 = 4

resultado = numero1 - numero2

print(resultado)    # imprime 6

# ====================================================
# operador de multiplicacion (*)
# ==================================================== 

numero1 = 7
numero2 = 3

resultado = numero1 * numero2

print(resultado)    # imprime 21

# ====================================================
# operador de division (/)
# ==================================================== 
# el resultado de la divisionn devuelve un flotante

numero1 = 10
numero2 = 2

resultado = numero1 / numero2

print(resultado)    # imprime 5.0

# ====================================================
# operador de division entera (//)
# ==================================================== 
# devuelve solo la parte entera del cociente

numero1 = 10
numero2 = 3

resultado = numero1 // numero2

print(resultado)    # imprime 3

# ====================================================
# operador de division (%)
# ==================================================== 
# devuelve el resto de la division

numero1 = 10
numero2 = 3

resultado = numero1 % numero2

print(resultado)    # imprime 1

# ====================================================
# operador de exponente (**)
# ==================================================== 
# devuelve el resto de la division

base = 2
exponente = 3

resultado = base ** exponente

print(resultado)    # imprime 8