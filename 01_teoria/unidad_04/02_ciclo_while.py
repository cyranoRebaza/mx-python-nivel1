# ==============================================================================
# unidad 04: repititivas - ciclo while
# ==============================================================================

"""

sintaxis del bucle for

while condicion:
    # codigo que se ejecuta mientras la condicion es verdadera

condicion: es una expresion booleana que se evalua antes de cada iteracion
    
--------------------------------------------------------------------------------
contadores en bucles while

- sirve para darle seguimiento cuantas veces se repite

contador = 0
while contador < 5:
    print(f"contador: {contador}")
    contador += 1

--------------------------------------------------------------------------------
bucle infinito en while

- ocurre cuando la condicion nunca se vuelve false

contador = 0
while contador < 5:
    print(f"contador: {contador}")
    # aqui falta incrementar el contador

"""

# Ejemplo 1: mostrar los numeros del 1 al 5

numero = 1
while numero < 5:
    print(f"numero: {numero}")
    numero += 1

print("ejemplo 1 a terminado.")

# Ejemplo 2: solicitar un nombre de usuario con maximo de 3 intentos

intentos = 0
maximo_intentos = 3
nombre = ""

while intentos < maximo_intentos and nombre == "":
    nombre = input("Ingresa tu nombre de usuario: ")

    if nombre == "":
        print("El nombre de usuario no puede estar vacio, intente de nuevo.")
        intentos += 1

if nombre != "":
    print(f"Bienvenido {nombre}!")
else:
    print("Se agotaron los interntos, intente mas tarde.")

print("ejemplo 2 a terminado.")

# Ejemplo 3: ingresar numeros y sumar los numeros positivos, ingresa 0 para
# terminar

suma = 0
numero = int(input("Ingrese un numero: "))
while numero != 0:
    if numero > 0:
        suma += numero

    numero = int(input("Ingrese un numero: "))
print(f"la suma de numeros positivos es: {suma}")

print("ejemplo 3 a terminado.")
