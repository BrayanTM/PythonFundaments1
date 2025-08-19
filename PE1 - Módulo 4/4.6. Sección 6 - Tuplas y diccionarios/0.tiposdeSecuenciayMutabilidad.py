
#TODO Tipos de secuencias y mutabilidad

"""  

Antes de comenzar a hablar acerca de tuplas y diccionarios, se deben introducir dos conceptos 
importantes: tipos de secuencia y mutabilidad.

Un tipo de secuencia es un tipo de dato en Python el cual es capaz de almacenar más de un valor 
(o ninguno si la secuencia esta vacía), los cuales pueden ser secuencialmente (de ahí el nombre) 
examinados, elemento por elemento.

Debido a que el bucle for es una herramienta especialmente diseñada para iterar a través de las 
secuencias, podemos definirlas de la siguiente manera: una secuencia es un tipo de dato que puede 
ser escaneado por el bucle for.

Hasta ahora, has trabajado con una secuencia en Python - la lista. La lista es un clásico ejemplo 
de una secuencia de Python. Aunque existen otras secuencias dignas de mencionar, las cuales se 
presentaran a continuación.

La segunda noción - la mutabilidad - es una propiedad de cualquier tipo de dato en Python que 
describe su disponibilidad para poder cambiar libremente durante la ejecución de un programa. 
Existen dos tipos de datos en Python: mutables e inmutables.

Los datos mutables pueden ser actualizados libremente en cualquier momento - a esta operación se 
le denomina "in situ".

In situ es una expresión en Latín que se traduce literalmente como en posición, en el lugar o 
momento. Por ejemplo, la siguiente instrucción modifica los datos "in situ":

"""

list.append(1)

"""  

Los datos inmutables no pueden ser modificados de esta manera.

Imagina que una lista solo puede ser asignada y leída. No podrías adjuntar ni remover un elemento 
de la lista. Si se agrega un elemento al final de la lista provocaría que la lista se cree desde 
cero.

Se tendría que crear una lista completamente nueva, la cual contenga los elementos ya existentes 
más el nuevo elemento.

El tipo de datos que se desea tratar ahora se llama tupla. Una tupla es una secuencia inmutable. 
Se puede comportar como una lista pero no puede ser modificada en el momento.

"""
