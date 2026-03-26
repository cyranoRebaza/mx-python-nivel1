#============================================
# unidad 02: entrada - proceso - salida
#============================================
# La funcion print()
#   - es utilizada para imprimir datos en la terminal
#   - acepta variables y literales o una combinacion
#   - se invoca print() sin argumentos, imprime linea blanco


# La funcion input()
#   - utilizar datos introducidos por teclado
#   - cuando se ejecuta pausa la ejecucion del programa y espera escriba algo
#   - lo que escribe por teclado retorna como cadena de texto(string)
#   - sintaxis:
#       variable = input(prompt)  
#       prompt es un string, una cadena de caracteres que se muestra en consola

# entrada de datos
numero1 = int(input("Ingrese un numero: "))
numero2 = int(input("Ingrese un numero: "))

# procesamiento de datos
resultado = numero1 + numero2

# salida
print("El resultado es: ", resultado)