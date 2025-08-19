
#TODO Creación de Funciones Multiparámetro

#? Ejemplos de Funciones: Cálculo del IMC

"""  

Definamos una función que calcula el Índice de Masa Corporal (IMC).

Como puedes observar, la formula ocupa dos valores:

- peso (originalmente en kilogramos)
- altura (originalmente en metros)

La nueva función tendrá dos parámetros. Su nombre será bmi, pero si prefieres utilizar otro 
nombre, adelante.

"""

def bmi(weight, height):
    return weight / height ** 2


print(bmi(52.5, 1.65))

"""  

La función hace lo que deseamos, pero es un poco sencilla - asume que los valores de ambos 
parámetros son significativos. Se debe comprobar que son confiables.

Vamos a comprobar ambos y regresar None si cualquiera de los dos es incorrecto.

"""

#? Calcular el IMC y Convertir Unidades del Sistema Inglés al Sistema Métrico

# Función para convertir pies y pulgadas a metros
def ft_and_inch_to_m(ft, inch = 0.0):
    return ft * 0.3048 + inch * 0.0254

# Función para convertir libras a kilogramos
def lb_to_kg(lb):
    return lb * 0.4535923

# Función para calcular el IMC
def bmi(weight, height):
    if height < 1.0 or height > 2.5 or weight < 20 or weight > 200:
        return None

    return weight / height ** 2


print(bmi(weight = lb_to_kg(176), height = ft_and_inch_to_m(5.75)))