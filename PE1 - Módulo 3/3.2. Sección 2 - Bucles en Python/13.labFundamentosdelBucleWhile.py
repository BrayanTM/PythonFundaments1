
#TODO Fundamentos del Bucle While

#? Escenario:

""" 

Escucha esta historia: Un niño y su padre, un programador de computadoras,
 juegan con bloques de madera. Están construyendo una pirámide.

Su pirámide es un poco rara, ya que en realidad es una pared en forma de 
pirámide - es plana. La pirámide se apila de acuerdo con un principio 
simple: cada capa inferior contiene un bloque más que la capa superior.


La figura ilustra la regla utilizada por los constructores:

Tu tarea es escribir un programa que lea la cantidad de bloques que tienen 
los constructores, y generar la altura de la pirámide que se puede 
construir utilizando estos bloques.

Nota: La altura se mide por el número de capas completas - si los 
constructores no tienen la cantidad suficiente de bloques y no pueden 
completar la siguiente capa, terminan su trabajo inmediatamente.

Prueba tu código con los datos que hemos proporcionado.

Datos de Prueba

Entrada de muestra:
6

Salida esperada:
Output
La altura de la pirámide es: 3

Entrada de muestra:
20

Salida esperada:
Output
La altura de la pirámide: 5

Entrada de muestra:
1000

Salida esperada:
Output
La altura de la pirámide: 44

Entrada de muestra:
2

Salida esperada:
Output
La altura de la pirámide: 1

blocks = int(input("Ingresa el número de bloques: "))

#
# Escribe tu código aquí.
#	

print("La altura de la pirámide:", height)

"""

blocks = int(input("Ingresa el número de bloques: "))

#
# Escribe tu código aquí.
#	
bloques_capa = 1
height = 0

while blocks >= bloques_capa:
    blocks -= bloques_capa
    height += 1
    bloques_capa += 1

print("La altura de la pirámide:", height)