# ====================================================
# unidad 02: funcion type()
# ==================================================== 

# La funcion type()
#   - retorna el tipo del valor asignado a la variable
#   - nos devuelve su clase (<class>) asignando su nombre como argumento
#   - detectando que tipo de dato es el objeto



# ===========================================================
# Ejemplo con tipo de datos simples
# ===========================================================


numero = 42
print(type(numero))           # <class 'int'>

precio = 19.99
print(type(precio))           # <class 'float'>

mensaje = "Hola, Mundo"
print(type(mensaje))          # <class 'str'>

es_mayor_de_edad = True
print(type(es_mayor_de_edad)) # <class 'bool'>