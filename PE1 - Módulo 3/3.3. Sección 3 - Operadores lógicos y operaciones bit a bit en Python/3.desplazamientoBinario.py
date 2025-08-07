
#TODO Desplazamiento binario a la izquierda y a la derecha

"""  

Python ofrece otra operación relacionada con los bits individuales: shifting. 
Esto se aplica solo a los valores de número entero, y no debe usar flotantes 
como argumentos para ello.

La computadora realiza el mismo tipo de operación, pero con una diferencia: 
como dos es la base para los números binarios (no 10), desplazar un valor un 
bit a la izquierda corresponde a multiplicarlo por dos; respectivamente, 
desplazar un bit a la derecha es como dividir entre dos (observa que se 
pierde el bit más a la derecha).

Los operadores de cambio en Python son un par de dígrafos: < < y > >, 
sugiriendo claramente en qué dirección actuará el cambio.

"""

var = 17
var_right = var >> 1
var_left = var << 2
print(var, var_left, var_right)

"""  

Nota:

- 17 >> 1 → 17 // 2 (17 dividido entre 2 a la potencia de 1) → 8 (desplazarse 
  hacia la derecha en un bit equivale a la división entera entre dos)
- 17 << 2 → 17 * 4 (17 multiplicado por 2 a la potencia de 2) → 68 (desplazarse 
  hacia la izquierda dos bits es lo mismo que multiplicar números enteros por 
  cuatro)

"""
