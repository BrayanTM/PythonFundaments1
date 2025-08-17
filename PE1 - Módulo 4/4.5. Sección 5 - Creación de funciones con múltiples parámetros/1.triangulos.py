
#? Ejemplos de Funciones: Triángulos

"""  

Ahora trabajaremos con triángulos. Comenzaremos con una función que verifique si tres lados 
de ciertas longitudes pueden formar un triángulo.

En la escuela aprendimos que la suma arbitraria de dos lados tiene que ser mayor que la 
longitud del tercer lado.

No será algo difícil. La función tendrá tres parámetros - uno para cada lado.

Regresará True si todos los lados pueden formar un triángulo, y False de lo contrario. En 
este caso, is_a_triangle es un buen nombre para dicha función.

"""

def is_a_triangle(a, b, c):
    return a + b > c and b + c > a and c + a > b


print(is_a_triangle(1, 1, 1))
print(is_a_triangle(1, 1, 3))
print("")


#? Triángulos y el Teorema de Pitágoras

"""  

Para verificar si es un triángulo rectángulo, podemos usar el Teorema de Pitágoras.

"""

def is_a_triangle(a, b, c):
    return a + b > c and b + c > a and c + a > b


def is_a_right_triangle(a, b, c):
    if not is_a_triangle(a, b, c):
        return False
    if c > a and c > b:
        return c ** 2 == a ** 2 + b ** 2
    if b > a and b > c:
        return b ** 2 == a ** 2 + c ** 2
    if a > b and a > c:
        return a ** 2 == b ** 2 + c ** 2
print(is_a_right_triangle(5, 3, 4))
print(is_a_right_triangle(1, 3, 4))
print("")


#? Evaluando el Área de un Triángulo

"""  

Para calcular el área de un triángulo, podemos usar la fórmula de Herón.
Vamos a emplear el operador de exponenciación para caluclar la raíz cuadrada.

"""

def is_a_triangle(a, b, c):
    return a + b > c and b + c > a and c + a > b


def heron(a, b, c):
    p = (a + b + c) / 2
    return (p * (p - a) * (p - b) * (p - c)) ** 0.5


def area_of_triangle(a, b, c):
    if not is_a_triangle(a, b, c):
        return None
    return heron(a, b, c)


print(area_of_triangle(1., 1., 2. ** .5))
print("")
