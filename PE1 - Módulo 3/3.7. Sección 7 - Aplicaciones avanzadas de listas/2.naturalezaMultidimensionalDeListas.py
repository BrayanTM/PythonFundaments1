
#TODO Naturaleza Multidimensional de las Listas: Aplicaciones Avanzadas

"""  

Para encontrar cualquier elemento de una lista bidimensional, debes usar dos coordenadas:

- Una vertical (numero de fila)
- Una horizontal (numero de columna)

"""

#? Ejemplo 1

"""  

Imagina que desarrollas una pieza de software para una estación meteorológica automática. 
El dispositivo registra la temperatura del aire cada hora y lo hace durante todo el mes. 
Esto te da un total de 24 × 31 = 744 valores. Intentemos diseñar una lista capaz de 
almacenar todos estos resultados.

Primero, debes decidir qué tipo de datos sería adecuado para esta aplicación. En este caso, 
sería mejor un float, ya que este termómetro puede medir la temperatura con una precisión 
de 0.1 ℃.

Luego tomarás la decisión arbitraria de que las filas registrarán las lecturas cada hora 
exactamente (por lo que la fila tendrá 24 elementos) y cada una de las filas se asignará 
a un día del mes (supongamos que cada mes tiene 31 días, por lo que necesita 31 filas). 
Aquí está el par apropiado de comprensiones (h es para las horas, d para el día):

#* temps = [[0.0 for h in range(24)] for d in range(31)]
 
Toda la matriz está llena de ceros ahora. Puede suponer que se actualiza automáticamente 
utilizando agentes de hardware especiales. Lo que tienes que hacer es esperar a que la 
matriz se llene con las mediciones.
____________________________________________________________________________________________

Ahora es el momento de determinar la temperatura promedio mensual del mediodía. Suma las 
31 lecturas registradas al mediodía y divida la suma por 31. Puedes suponer que la 
temperatura de medianoche se almacena primero. Aquí está el código:

"""

temps = [[0.0 for h in range(24)] for d in range(31)]
#
# La matriz se actualiza aquí.
#
 
total = 0.0
 
for day in temps:
    total += day[11]
 
average = total / 31
 
print("Temperatura promedio al mediodía:", average)

"""  

Nota: La variable day utilizada por el bucle for no es un escalar - cada paso a través 
de la matriz temps lo asigna a la siguiente fila de la matriz; Por lo tanto, es una lista. 
Se debe indexar con 11 para acceder al valor de temperatura medida al mediodía.
____________________________________________________________________________________________

Ahora encuentra la temperatura más alta durante todo el mes - analiza el código:

"""

temps = [[0.0 for h in range(24)] for d in range(31)]
#
# La matriz se actualiza aquí.
#

highest = -100.0

for day in temps:
    for temp in day:
        if temp > highest:
            highest = temp

print("La temperatura más alta fue:", highest)

"""  

Note:

- la variable day itera en todas las filas de la matriz temps;
- la variable temp itera a través de todas las mediciones tomadas en un día.
___________________________________________________________________________________________

Ahora cuenta los días en que la temperatura al mediodía fue de al menos 20 ℃:

"""

temps = [[0.0 for h in range(24)] for d in range(31)]
#
# La matriz se actualiza aquí.
#

hot_days = 0

for day in temps:
    if day[11] > 20.0:
        hot_days += 1

print(hot_days, "fueron los días calurosos.")


#? Ejemplo 2

"""  

Python no limita la profundidad de la inclusión lista en lista. Aquí puedes ver un ejemplo 
de un arreglo tridimensional:

rooms = [[[False for r in range(20)] for f in range(15)] for t in range(3)]

Imagina un hotel. Es un hotel enorme que consta de tres edificios, de 15 pisos cada uno. 
Hay 20 habitaciones en cada piso. Para esto, necesitas un arreglo que pueda recopilar y 
procesar información sobre las habitaciones ocupadas/libres.

Primer paso - El tipo de elementos del arreglo. En este caso, sería un valor Booleano 
(True/False).

Paso dos - análisis de la situación. Resume la información disponible: tres edificios, 
15 pisos, 20 habitaciones.

Ahora puedes crear el arreglo:

"""

rooms = [[[False for r in range(20)] for f in range(15)] for t in range(3)]

"""  

El primer índice (0 a 2) selecciona uno de los edificios; el segundo (0 a 14) selecciona 
el piso, el tercero (0 a 19) selecciona el número de habitación. Todas las habitaciones 
están inicialmente desocupadas.

Ahora ya puedes reservar una habitación para dos recién casados: en el segundo edificio, 
en el décimo piso, habitación 14:

"""

rooms[1][9][13] = True

"""  

y desocupar el segundo cuarto en el quinto piso ubicado en el primer edificio:

"""

rooms[0][4][1] = False

"""  

Verifica si hay disponibilidad en el piso 15 del tercer edificio:

"""

vacancy = 0

for room_number in range(20):
    if not rooms[2][14][room_number]:
        vacancy += 1

"""  

La variable vacancy contiene 0 si todas las habitaciones están ocupadas, o en dado caso 
el número de habitaciones disponibles.

"""