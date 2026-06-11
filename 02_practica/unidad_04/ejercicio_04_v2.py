"""
Unidad 04 - Ejercicio 04 - v2

Hacer un programa que solicite UN número y luego calcule y emita un cartel 
aclaratorio si el mismo es primo o no es primo.  

Nota: un número es primo cuando es divisible únicamente por 1 y por sí mismo.

------------------------------------------
- usar raiz del numero --> buscar hasta raiz cuadrada del numero, porque si un 
numero tiene divisores, siempre aparece un par de divisores

numero = 10
1 * 10
2 * 5
5 * 2 -->  empieza a repetir pares a partir de la raiz de 10

10 * 1 



"""
# Pedir un numero
numero = int(input("Ingrese un numero: "))

if numero < 2:
    print(f"El numero {numero} no es primo")
else:
    es_primo = True

    # Buscar divisores hasta la raiz cuadrada del numero
    for n in range(2, int(numero ** 0.5) + 1):
        if numero % n == 0:
            es_primo = False
            break

# Mostrar resultado
    if es_primo:
        print(f"El numero {numero} es primo")
    else:
        print(f"El numero {numero} no es primo")
