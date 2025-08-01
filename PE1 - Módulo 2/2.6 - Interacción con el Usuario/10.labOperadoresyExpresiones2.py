
# ! LAB Operadores y Expresiones 2
#* Escenario:

"""
La tarea es preparar un código simple para evaluar o encontrar el tiempo final de un periodo de tiempo dado, expresándolo en horas y minutos. La hora de inicio se da como un par de horas (0..23) y minutos (0..59). El resultado debe ser mostrado en la consola.

Por ejemplo, si el evento comienza a las 12:17 y dura 59 minutos, terminará a las 13:16.

No te preocupes si tu código no es perfecto - está bien si acepta una hora invalida - lo más importante es que el código produzca una salida correcta acorde a la entrada dada.

Prueba el código cuidadosamente. Pista: utilizar el operador % puede ser clave para el éxito.
"""
#? Forma 1:
hour = int(input("Hora de inicio (horas): "))
mins = int(input("Minuto de inicio (minutos): "))
dura = int(input("Duración del evento (minutos): "))

# Escribe tu código aquí.
final_mins = (mins + dura) % 60
final_hour = (hour + (mins + dura) // 60) % 24

print("Hora final:", final_hour, "Minutos finales:", final_mins)

#? Forma 2:
hour = int(input("Hora de inicio (horas): "))
mins = int(input("Minuto de inicio (minutos): "))
dura = int(input("Duración del evento (minutos) "))
# encuentra el número total de minutos
tot_min = (mins)+(dura)
# encuentra el número de horas ocultas en los minutos y actualiza las horas
hour_tot = (tot_min//60) + hour
# corrige los minutos para que estén en un rango de (0..59)
mins = tot_min % 60
# corrige las horas para que estén en un rango de (0..23) 
hour = hour_tot % 24
print(hour, ":", mins, sep='')

