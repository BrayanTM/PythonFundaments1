
#TODO Quiz de Sección

#? Pregunta 1
"""  

Pregunta 1: Crea un bucle for que cuente de 0 a 10, e imprima números 
impares en la pantalla. Usa el esqueleto de abajo:

for i in range(1, 11):
    # Línea de código.
        # Línea de código.

"""

for i in range(1, 11):
    # Línea de código.
    if i % 2 != 0:
        # Línea de código.
        print(i)

print()
#? Pregunta 2

"""  

Pregunta 2: Crea un bucle while que cuente de 0 a 10, e imprima números 
impares en la pantalla. Usa el esqueleto de abajo:

x = 1
while x < 11:
    # Línea de código.
        # Línea de código.
    # Línea de código.

"""

x = 1
while x < 11:
    # Línea de código.
    if x % 2 != 0:
        # Línea de código.
        print(x)
    # Línea de código.
    x += 1

print()
#? Pregunta 3

"""  

Pregunta 3: Crea un programa con un bucle for y una sentencia break. El 
programa debe iterar sobre los caracteres en una dirección de correo 
electrónico, salir del bucle cuando llegue al símbolo @ e imprimir la 
parte antes de @ en una línea. Usa el esqueleto de abajo:

for ch in "john.smith@pythoninstitute.org":
    if ch == "@":
        # Línea de código.
    # Línea de código.

"""

for ch in "john.smith@pythoninstitute.org":
    if ch == "@":
        # Línea de código.
        break
    # Línea de código.
    print(ch, end="")

print()
print()
#? Pregunta 4

"""  

Pregunta 4: Crea un programa con un bucle for y una sentencia continue. 
El programa debe iterar sobre una cadena de dígitos, reemplazar cada 0 
con x, e imprimir la cadena modificada en la pantalla. Usa el esqueleto 
de abajo:

for digit in "0165031806510":
    if digit == "0":
        # Línea de código.
        # Línea de código.
    # Línea de código.

"""

for digit in "0165031806510":
    if digit == "0":
        # Línea de código.
        print("x", end="")
        # Línea de código.
        continue
    # Línea de código.
    print(digit, end="")

print()
