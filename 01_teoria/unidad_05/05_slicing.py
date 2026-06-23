# ==============================================================================
# unidad 05: slicing
# ==============================================================================

"""
slicing: sirve para obtener una parte de una secuencia(lista,string, tupla)

sintaxis
secuencia[inicio:fin:paso]

- inicio: indice desde donde empieza(incluye)
- fin: indice donde termina (no incluye)
- paso: de cuanto en cuanto avanza

resumen:
lista[a:b] # desde a hasta b-1
lista[:b] # desde inicio hasta b-1
lista[a:] # desde a hasta el final
lista[::n] # saltando de  n
lista[::-1] # invertir

lista[:] # copia superficial

--------------------------------------------------------------------------------

"""
lista_numeros = [10, 20, 30, 40, 50]

# tomar desde indice 1 hasta 3
print(lista_numeros[1:4])  # [20, 30, 40]

# omitir el inicio
print(lista_numeros[:3])  # [10, 20, 30]

# omitir el fin
print(lista_numeros[2:])  # [30, 40, 50]

# usando paso
print(lista_numeros[::2])  # [10, 30, 50]

# invertir la secuencia
print(lista_numeros[::-1])  # [50, 40, 30, 20, 10]
