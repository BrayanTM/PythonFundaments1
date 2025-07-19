# Input conversion de tipos
# Este código solicita al usuario que ingrese un número, lo convierte a tipo float,
# calcula su cuadrado y muestra el resultado.

# Ejemplo de conversión de tipos en Python
anything = float(input("Ingresa un número: "))
something = anything ** 2.0
print(anything, "a la potencia de 2 es", something)

# Ejemplo de conversión de tipos para calcular la hipotenusa
# de un triángulo rectángulo dados los catetos.
leg_a = float(input("Ingresa la longitud del primer cateto: "))
leg_b = float(input("Ingresa la longitud del segundo cateto: "))
hypo = (leg_a**2 + leg_b**2) ** .5
print("La longitud de la hipotenusa es:", hypo)

# Ejemplo de conversión de tipos para calcular la hipotenusa
# de un triángulo rectángulo dados los catetos.
leg_a = float(input("Ingresa la longitud del primer cateto: "))
leg_b = float(input("Ingresa la longitud del segundo cateto: "))
print("La longitud de la hipotenusa es:", (leg_a**2 + leg_b**2) ** .5)