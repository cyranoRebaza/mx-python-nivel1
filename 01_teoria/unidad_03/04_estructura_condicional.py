# ====================================================
# unidad 03: Estructura condicional: if | if-else | elif 
# ==================================================== 


"""
 sintaxis de la sentencia if
 
 if condicion:
    #codigo que se ejecuta si la condicion es verdadera
    
1- condicion: se evalua como una expresion booleana, es decir el resultado es
True o False

2- dos puntos (:) le dice a python que el bloque de codigo que sigue esta
relacionado con esa condicion

3- Bloque de codigo indentado: todo el codigo que este identado debajo del if
se va ejecutar solo si la condicion es True

----------------------------------------------------------------
sintaxis de la sentencia else

if condicion:
    # codigo que se ejecuta si la condicion es verdadera
else:
    # codigo que se ejecuta si la condicion es falsa
    
----------------------------------------------------------------
sintaxis de la sentencia elif (abreviatura del else if)

if condicion1:
    # codigo si la condicion es verdadera
elif condicion2:
    # codigo si la condicion 1 es falsa y la condicion2 es verdadera
else:
    # codigo si todas las condiciones anteriores son falsas

"""
# ejemplo condicional simple
edad = 18

if edad > 18:
    print("Eres mayor de edad.")
    
# ejemplo de condicional doble
edad = 16

if edad >= 18:
    print("Eres mayor de edad.")
    
else:
    print("Eres menor de edad.")
    
# ejemplo condicional en cadena
calificacion = 85

if calificacion >= 90:
    print("Tiene una A.")
    
elif calificacion >= 80:
    print("Tienes una B.")
    
elif calificacion >= 70:
    print("Tienes una C.")
    
else:
    print("Tienes una D o menos.")
    
# ejemplo condicional anidado
calificacion = 60

if calificacion >= 90:
    print("Tiene una A.")
    
else:
    if calificacion >= 80:
        print("Tiene una B.")
    
    else:
        if calificacion >= 70:
            print("Tiene una C.")
        else:
            print("Tiene una D o menos")
    



