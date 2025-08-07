
#TODO Operadores bit a bit

"""  

Hay cuatro operadores que permiten manipular bits de datos individuales.
Se denominan bit a bit porque operan en cada bit de un número binario.

Cubren todas las operaciones que mencionamos anteriormente en el contexto
lógico, y un operador adicional es el operador xor (significa "exclusive
or", o "o exclusivo"), y se denota como ^ (signo de intercalación).

Estos operadores son:
- & (ampersand) - conjunción a nivel de bits;
- | (barra vertical) - disyunción a nivel de bits;
- ~ (tilde) - negación a nivel de bits;
- ^ (signo de intercalación) - xor a nivel de bits;

Operaciones bit a bit (&, |, y ^):

 Argumento A | Argumento B  | A & B | A | B | A ^ B
-------------|--------------|-------|-------|-------
0            | 0            | 0     | 0     | 0
0            | 1            | 0     | 1     | 1
1            | 0            | 0     | 1     | 1
1            | 1            | 1     | 1     | 0

Operación de negación a nivel de bits (~):

 Argumento A | ~A
-------------|-----
0            | 1
1            | 0

Hagámoslo más facil:

- & requeire exactamente dos 1s para proportcionar 1 como resultado;
- | requeire al menos un 1 para proportcionar 1 como resultado;
- ^ requeire exactamente un 1 para proportcionar 1 como resultado;
- ~ invierte el valor del bit, es decir, convierte 0 en 1 y 1 en 0.

Los argumentos de estos operadores deben ser entoros; no debemos usar
flotantes aquí.

La diferencia en el funcionamiento de los operadores lógicos y de bits es
importante: los operadores lógicos no penetran en el nivel de bits de su
argumento. Solo les interesa el valor entero final.

Los operadores bit a bit son más estrictos: tratan con cada bit por separado.
Si asumimos que la variable entrera ocupa 64 bits (lo que es común en los 
sistemas informáticos modernos), puede imaginar la operación a nivel de bits
como una evaluación de 64 veces del operador lógico para cada par de bits de
los argumentos. Su analogía es obviamente imperfecta, ya que en el mundo real 
todas estas 64 operaciones se realizan al mismo tiempo (simultaneamente).

"""

#? Operaciones lógicas vs operaciones bit a bit

i = 15
j = 22

""" 
Asumimos que los enteros se almacenan con 32 bits, la imgagen a nivel de bits
de las dos variables será la siguiente:

i = 00000000 00000000 00000000 00001111
j = 00000000 00000000 00000000 00010110

Se ejecuta la asignación:

"""

log = i and j

"""  

Estamos tratando con una conjunción lógica aquí. Vamos a trazar el curso de los 
cálculos. Ambas variables i y j no son ceros, por lo que se considerará que 
representan a True. Al consultar la tabla de verdad para el operador and, podemos 
ver que el resultado será True. No se realizan otras operaciones.

log = True

Ahora la operación a nivel de bits:

"""

bit = i & j

"""  

El operador & operará con cada par de bits correspondientes por separado, produciendo 
los valores de los bits relevantes del resultado. Por lo tanto, el resultado será el 
siguiente:

i = 00000000 00000000 00000000 00001111
j = 00000000 00000000 00000000 00010110
-----------------------------------
bit = 00000000 00000000 00000000 00000110

El resultado es 6, que es el valor de la variable bit.

bit = 6

Veamos ahora los operadores de negación:

"""

logneg = not i

"""

El operador not se aplica a la variable i. El valor de i es 15, que no es cero, 
por lo que se considera True. Al aplicar el operador not, obtenemos False.

logneg = False

Ahora la operación a nivel de bits:

"""

bitneg = ~i

"""El operador ~ se aplica a la variable i. El resultado de la operación será el 
complemento a nivel de bits de i, es decir, todos los bits de i se invertirán:

i = 00000000 00000000 00000000 00001111
-----------------------------------
bitneg = 11111111 11111111 11111111 11110000

El resultado es -16, que es el valor de la variable bitneg.
bitneg = -16

Cada uno de estos operadores de dos argumentos se puede utilizar en forma abreviada.
Estos son los ejemplos de sus notaciones equivalentes:

x = x & y | x &= y
x = x | y | x |= y
x = x ^ y | x ^= y

Estas formas abreviadas son especialmente útiles cuando se trabaja con grandes 
cantidades de datos, como en el caso de las operaciones con máscaras de bits.

"""

#? Cómo tratar con bits individuales?

"""  

Imagina que eres un desarrollador obligado a aescribir una pieza importante de un
sistema operativo. Se te ha dicho que puede usar una variable asignada de la
siguiente forma:

"""

flag_register = 0x1234  # valor hexadecimal → 0001 0010 0011 0100 en binario

"""  

La variable almacena la información sobre varios aspectos de la operación del 
sistema. Cada bit de la variable almacena un valor de si/no. También se te ha 
dicho que solo uno de estos bits es tuyo - el tercero (recuerda que los bits se 
numeran desde cero y el número de bits cero es el más bajo, mientras que el más 
alto es el número 31). Los bits restantes no pueden cambiar, porque están 
destinados a almacenar otros datos. Aquí está tu bit marcado con la letra x:

flag_register = 0000000000000000000000000000x000

Es posible que tengas que hacer frente a las siguientes tareas:

#? 1. Comprobar el estado de tu bit - deseas averiguar el valor de su bit; comparar 
   la variable completa con cero no hará nada, porque los bits restantes pueden 
   tener valores completamente impredecibles, pero puedes usar la siguiente propiedad 
   de conjunción:

x & 1 = x
x & 0 = 0
 
Si aplicas la operación & a la variable flag_register junto con la siguiente imagen 
de bits:

00000000000000000000000000001000

(observa el 1 en la posición de tu bit) como resultado, obtendrás una de las 
siguientes cadenas de bits:

00000000000000000000000000001000 si tu bit se estableció en 1
00000000000000000000000000000000 si tu bit se reseteo a 0

Dicha secuencia de ceros y unos, cuya tarea es tomar el valor o cambiar los bits 
seleccionados, se denomina máscara de bits.

Construyamos una máscara de bits para detectar el estado de tus bits. Debería apuntar 
a el tercer bit. Ese bit tiene el peso de 23=8. Se podría crear una máscara adecuada 
mediante la siguiente sentencia:

"""

the_mask = 0b00001000  # binario → bit 3 encendido
# equivale a decimal: 8

""" 
También puedes hacer una secuencia de instrucciones dependiendo del estado de 
tu bit, aquí está: 
"""

if flag_register & the_mask:
    print("Mi bit está encendido (1)")
else:
    print("Mi bit está apagado (0)")

"""  

¿Por qué funciona?

- & solo da 1 si ambos bits son 1.
- Si el bit 3 está encendido, el resultado será 00001000.
- Si está apagado, será 00000000.

"""

""" 

#? 2. Reiniciar el bit (ponerlo en 0, sin afectar los demás)
Usas el operador & con la máscara negada ~the_mask, para apagar solo ese bit: 

"""

flag_register &= ~the_mask  # reinicia el bit 3

""" 

Explicación:

- ~the_mask convierte 00001000 en 11110111
- Al hacer &, todo queda igual excepto el bit 3, que se pone en 0. 

"""

#? 3. Encender el bit (ponerlo en 1, sin afectar los demás)
"""
Usas el operador | con la máscara the_mask, para encender solo ese bit:
"""
flag_register |= the_mask  # enciende el bit 3

"""

Explicación:

- the_mask es 00001000
- Al hacer |, todo queda igual excepto el bit 3, que se pone en 1.

"""

#? 4. Cambiar el estado del bit (invertirlo, sin afectar los demás)
"""
Usas el operador ^ con la máscara the_mask, para cambiar el estado de ese bit:
"""
flag_register ^= the_mask  # cambia el estado del bit 3

"""

Explicación:

- the_mask es 00001000
- Al hacer ^, si el bit 3 estaba en 1, se pone en 0, y si estaba en 0, se pone en 1.

"""
