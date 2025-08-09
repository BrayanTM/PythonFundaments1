
#TODO Listas - Algunos Programas Simples

# El primero de ellos intenta encontrar el valor mayor en la lista. Mira el código:

my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
largest = my_list[0]

for i in range(1, len(my_list)):
    if my_list[i] > largest:
        largest = my_list[i]

print(largest)

"""  

El código puede ser reescrito para hacer uso de la forma recién introducida del bucle for:

my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
largest = my_list[0]
 
for i in my_list:
    if i > largest:
        largest = i
 
print(largest)

El programa anterior realiza una comparación innecesaria, cuando el primer elemento se 
compara consigo mismo, pero esto no es un problema en absoluto.

El código da como resultado el 17 también (nada inusual).

Si necesitas ahorrar energía de la computadora, puedes usar una rebanada:

my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
largest = my_list[0]

for i in my_list[1:]:
    if i > largest:
        largest = i

print(largest)

La pregunta es: ¿Cuál de estas dos acciones consume más recursos informáticos - solo una 
comparación o rebanar casi todos los elementos de una lista?

Ahora encontremos la ubicación de un elemento dado dentro de una lista:

"""

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
to_find = 5
found = False

for i in range(len(my_list)):
    found = my_list[i] == to_find
    if found:
        break

if found:
    print("Elemento encontrado en el índice", i)
else:
    print("ausente")

"""  

Nota:

- el valor buscado se almacena en la variable to_find;
- el estado actual de la búsqueda se almacena en la variable found (True/False).
- cuando found se convierte en True, se sale del bucle for.

Supongamos que has elegido los siguientes números en la lotería: 3, 7, 11, 42, 34, 49.

Los números que han salido sorteados son: 5, 11, 9, 42, 3, y 49.

La pregunta es: ¿A cuántos números le has atinado?

Este programa te dará la respuesta:

"""

drawn = [5, 11, 9, 42, 3, 49]
bets = [3, 7, 11, 42, 34, 49]
hits = 0

for number in bets:
    if number in drawn:
        hits += 1

print(hits)

"""  

Nota:

- la lista drawn almacena todos los números sorteados;
- La lista bets almacena los números con que se juega;
- la variable hits cuenta tus aciertos.

la output del programa es: 4.

"""