
#TODO Ordenamiento Burbuja

"""  

El algoritmo de ordenamiento burbuja es un método sencillo para ordenar una lista de elementos.
Consiste en recorrer la lista repetidamente, comparando elementos adyacentes y 
cambiándolos de lugar si están en el orden incorrecto. Este proceso se repite hasta que 
la lista está ordenada.

El algoritmo tiene una complejidad temporal de O(n^2) en el peor caso, lo que lo hace 
ineficiente para listas grandes, pero es fácil de entender e implementar.

A continuación se muestra una implementación del algoritmo de ordenamiento burbuja en Python.

"""

#? Ordenando un lista

"""  

Cuántos pases necesitamos para ordenar la lista completa?

Resolvamos estre problema de la siguiente manera: introducimos otra variable, su tarea
es obsercar si se ha realizado algún intercambio durante el pase o no. Si no hay
intercambio, entonces la lista ya está ordenada, y no hay que hacer nada más. Creamos
una variable llamada swapped, y le asignamos un valor de false para indicar que no hay
intercambios. De lo contrario, se le asignará True.

my_list = [8, 10, 6, 2, 4]  # lista a ordenar

for i in range(len(my_list) - 1):  # necesitamos (5 - 1) comparaciones
    if my_list[i] > my_list[i + 1]:  # compara elementos adyacentes
        my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]  # Si terminamos aquí, tenemos que intercambiar elementos.

Deberías poder leer y comprender este programa sin ningún problema:

my_list = [8, 10, 6, 2, 4]  # lista a ordenar
swapped = True  # Lo necesitamos verdadero (True) para ingresar al bucle while.

while swapped:
    swapped = False  # no hay intercambios hasta ahora
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            swapped = True  # ¡ocurrió el intercambio!
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

print(my_list)

"""

#? El ordenamiento burbuja - versión interactiva

my_list = []
swapped = True
num = int(input("¿Cuántos elementos deseas ordenar?: "))

for i in range(num):
    val = float(input("Ingresa un elemento de la lista: "))
    my_list.append(val)

while swapped:
    swapped = False
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            swapped = True
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

print("\nOrdenada:")
print(my_list)


"""  

Python sin embargo, tiene sus propios mecanismos de clasificación. Nadie necesita escribir
sus propias clases, ya que hay un número suficiente de herramientas listas para usar.

Si quieres que Python ordene tu lista, puedes hacerlo de la siguiente manera:

my_list = [8, 10, 6, 2, 4]
my_list.sort()
print(my_list)

Como puedes ver, todas las listas tienen un método denominado sort(), que las ordena lo más
rápido posible. 

"""