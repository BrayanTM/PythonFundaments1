
#TODO Condiciones y Ejecución Condicional
"""

Ya sabemos como hacer preuntas a Python, pero no sabemos como
hacer uso razonable de las respuestas. Se debe tener un 
mecanismo que le permita hacer algo si se cumple una condición,
y no hacer si no se cumple.

Para tomar tales decisiones, Python ofrece una instrucción 
especial. Debido a su naturaleza y aplicación, se le conoce como
instrucción condicional. Esta instrucción permite que el 
programa tome decisiones basadas en condiciones lógicas.

"""

#TODO Ejecución Condicional: la sentencia if

"""

Esta sentencia condicional consta de los siguientes elementos, 
estrictamente necesarios en este orden:

- La palabra clave reservada if;
- Uno o más espacios en blanco;
- Una expresión (una pregunta o una respuesta) cuyo valor se 
  interpretar únicamente en términos de True (cuando su valor 
  no sea cero) y False (cuando sea igual a cero);
- Unos dos puntos seguidos de una nueva línea;
- Una instrucción con sangría o un conjunto de instrucciones 
  (se requiere absolutamente al menos una instrucción); la 
  sangría se puede lograr de dos maneras: insertando un 
  número particular de espacios (la recomendación es usar 
  cuatro espacios de sangría), o usando el tabulador; nota: 
  si hay mas de una instrucción en la parte con sangría, la 
  sangría debe ser la misma en todas las líneas; aunque puede 
  parecer lo mismo si se mezclan tabuladores con espacios, es 
  importante que todas las sangrías sean exactamente iguales 
  Python 3 no permite mezclar espacios y tabuladores para 
  la sangría.

if true_or_not:
    do_this_if_true

"""

#TODO Ejecución Condicional: la sentencia if - else

"""

Si se desea que el programa realice una acción alternativa 
cuando la condición no se cumple, se puede usar la sentencia
if - else. Esta sentencia permite definir un bloque de código
que se ejecutará si la condición es falsa.

if true_or_false_condition:
    perform_if_condition_true
else:
    perform_if_condition_false

"""

#TODO Sentencias if - else anidadas

"""

Lee lo que hemos planeado para este Domingo. Si hay buen clima, 
saldremos a caminar. Si encontramos un buen restaurante, 
almorzaremos allí. De lo contrario, vamos a comer un sandwich. 
Si hay mal clima, iremos al cine. Si no hay boletos, iremos de 
compras al centro comercial más cercano.   


if the_weather_is_good:
    if nice_restaurant_is_found:
        have_lunch()
    else:
        eat_a_sandwich()
else:
    if tickets_are_available:
        go_to_the_theater()
    else:
        go_shopping()

Aquí hay dos puntos importantes:

- Este uso de la sentencia if se conoce como anidamiento;
  recuerda que cada else se refiere al if que se encuentra en 
  el mismo nivel de sangría; se necesita saber esto para 
  determinar cómo se relacionan los ifs y los else;
- Considera como la sangría mejora la legibilidad y hace que 
  el código sea más fácil de entender y rastrear.

"""

#TODO La sentencia elif

"""

El segundo caso especial presenta otra nueva palabra clave de 
python: elif. Esta palabra clave es una abreviatura de "else if"
y se utiliza para verificar más de una condición, y para 
detener cuando se encuentra la primera condición verdadera.

if the_weather_is_good:
    go_for_a_walk()
elif tickets_are_available:
    go_to_the_theater()
elif table_is_available:
    go_for_lunch()
else:
    play_chess_at_home()

Se debe prestar atención adicional a este caso:

- No debes usar else sin un if precedente;
- else siempre es la última rama de la cascada, 
  independientemente de si has usado elif o no;
- else es una parte opcional de la cascada, y 
  puede omitirse;
- Si hay una rama else en la cascada, solo se 
  ejecuta una de todas las ramas;
- Si no hay una rama else, es posible que no se 
  ejecute ninguna de las opciones disponibles.

"""