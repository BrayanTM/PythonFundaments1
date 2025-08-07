
#TODO Haciendo uso de las listas

"""  

El bucle for tiene una variante muy especial que puede procesar las listas de manera muy
efectiva.

"""

my_list = [10, 1, 8, 3, 5]
total = 0

for i in range(len(my_list)):
    total += my_list[i]

print(total)

#? El segundo aspecto del bucle for

"""  

El bucle for puede hacer mucho más. Puede ocultar todas las acciones conectadas
a la indexación de la lista y entregar todos los elementos de la lista de 
manera práctica.

"""

my_list = [10, 1, 8, 3, 5]
total = 0

for i in my_list:
    total += i

print(total)

#? Listas en acción

"""  

Imagina que necesitas reorganizar los elementos de una lista, es decir, revertir el
orden de los elementos: el primero y el quinto, así como el segundo y cuatro elementos
serán intercambiados. El tercer elemento permanecerá en su lugar.

Pregunta: ¿Cómo se pueden intercambiar los valores de dos variables?

variable_1 = 1
variable_2 = 2

variable_2 = variable_1
variable_1 = variable_2

Si haces algo como esto, perderás el valor preciamente almacenado en variable2. Cambiar
el orden de las tareas no ayudará. Necesitas una tercera variable que sirva como 
almacenamiento auxiliar.

Así es como se puede hacer:

variable_1 = 1
variable_2 = 2

auxiliary = variable_1
variable_1 = variable_2
variable_2 = auxiliary

Python ofrece una forma más conveninete de hacer el intercamvio de valores:

variable_1 = 1
variable_2 = 2

variable_1, variable_2 = variable_2, variable_1

Claro, efectivo y elegante.

Ahora podemos intercambiar fácilmente los elementos de la lista para revertir su orden:

my_list = [10, 1, 8, 3, 5]

my_list[0], my_list[4] = my_list[4], my_list[0]
my_list[1], my_list[3] = my_list[3], my_list[1]

print(my_list)

Se ve bien con cinco elementos, pero ¿qué pasa si la lista tiene 100 elementos? ¿O 1000?

¿Puedes usar el bucle for para hacer lo mismo automáticamente, independientemente de la 
longitud de la lista? Si, si puedes.

for i in range(length // 2):
    my_list[i], my_list[length - i - 1] = my_list[length - i - 1], my_list[i]

print(my_list)

Ahora, la lista se ha revertido correctamente, sin importar cuántos elementos tenga.

"""

my_list = [10, 1, 8, 3, 5]

length = len(my_list)

for i in range(length // 2):
    my_list[i], my_list[length - i - 1] = my_list[length - i - 1], my_list[i]

print(my_list)

"""

EXPLICACIÓN DEL ALGORITMO DE INVERSIÓN:

Este código invierte una lista intercambiando elementos desde los extremos hacia el centro:

1. length = 5 (longitud de la lista)
2. range(length // 2) = range(2), por lo que i toma valores 0 y 1
3. En cada iteración intercambiamos:
   - i=0: my_list[0] ↔ my_list[4] → intercambia 10 y 5
   - i=1: my_list[1] ↔ my_list[3] → intercambia 1 y 3
   - El elemento central (índice 2, valor 8) no se mueve

4. La fórmula length - i - 1 calcula el índice "espejo":
   - Cuando i=0: 5 - 0 - 1 = 4 (último elemento)
   - Cuando i=1: 5 - 1 - 1 = 3 (penúltimo elemento)

5. Resultado: [10, 1, 8, 3, 5] → [5, 3, 8, 1, 10]

¿Por qué solo length // 2 iteraciones?
- Porque intercambiamos pares de elementos desde los extremos
- Con 5 elementos, necesitamos 2 intercambios para invertir toda la lista
- Si iteráramos más, volveríamos a intercambiar los mismos elementos

"""