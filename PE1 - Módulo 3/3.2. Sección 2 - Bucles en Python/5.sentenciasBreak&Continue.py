
#TODO Sentencias Break y Continue

# Sentencia Break
"""
break - sale del bucle inmediatamente, e incondicionalmente termina 
la operación del bucle; el programa comienza a ejecutar la instrucción 
más cercana después del cuerpo del bucle.
"""

# Sentencia Continue
"""
continue - se comporta como si el programa hubiera llegado repentinamente 
al final del cuerpo; el siguiente turno se inicia y la expresión de 
condición se prueba de inmediato.
"""

# break - ejemplo

print("La instrucción break:")
for i in range(1, 6):
    if i == 3:
        break
    print("Dentro del bucle.", i)
print("Fuera del bucle.")


# continue - ejemplo

print("\nLa instrucción continue:")
for i in range(1, 6):
    if i == 3:
        continue
    print("Dentro del bucle.", i)
print("Fuera del bucle.")

