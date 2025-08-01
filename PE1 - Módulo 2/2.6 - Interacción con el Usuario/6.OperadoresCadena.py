# Los operadores de cadena en Python permiten manipular texto de diversas formas.
# A continuación se presentan algunos ejemplos de cómo utilizar estos operadores.

# Ejemplo de concatenación de cadenas
# El signo de + (más), al ser aplicado a dos cadenas, se convierte en un operador de concatenación:
fnam = input("¿Me puedes dar tu nombre por favor? ")
lnam = input("¿Me puedes dar tu apellido por favor? ")
print("Gracias. ")
print("\nTu nombre es " + fnam + " " + lnam + ".")

# Ejemplo de repetición de cadenas
# El operador * (asterisco) se utiliza para repetir una cadena un número específico de veces:
print("+" + 10 * "-" + "+") # Imprime una línea de separación
print(("|" + " " * 10 + "|\n") * 5, end="") # Imprime un cuadro de 5 líneas con espacios
print("+" + 10 * "-" + "+") # Imprime otra línea de separación

# Ejemplo de acceso a caracteres individuales
texto = "Python"
print(texto[0])  # Imprime 'P'
print(texto[-1])  # Imprime 'n'

# Ejemplo de slicing (rebanado) de cadenas
print(texto[1:4])  # Imprime 'yth'