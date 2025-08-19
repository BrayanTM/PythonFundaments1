
#TODO Cómo lidiar con más de una excepción

#? Dos excepciones después de un try

"""  

Por ejemplo, si tenemos un bloque try que puede lanzar dos tipos de excepciones diferentes, 
podemos manejarlas de la siguiente manera:

try:
    # Código que puede lanzar dos tipos de excepciones
except ValueError:
    # Manejo de la excepción ValueError
except TypeError:
    # Manejo de la excepción TypeError

"""

try:
    user_input = input('Ingresa un número natural: ')
    value = int(user_input)
    print('El recíproco de', value, 'es', 1/value)        
except ValueError:
    print('No se que hacer con', user_input)    
except ZeroDivisionError:
    print('La división entre cero no está permitida en nuestro Universo.') 


#? La excepción predeterminada y cómo usarla.

"""  

La excepción predeterminada se utiliza para capturar cualquier excepción que no haya sido 
manejada por los bloques except anteriores.

"""

try:
    user_input = input('Ingresa un número natural: ')
    value = int(user_input)
    print('El recíproco de', value, 'es', 1/value)        
except ValueError:
    print('No se que hacer con', user_input)    
except ZeroDivisionError:
    print('La división entre cero no está permitida en nuestro Universo.')   
except:
    print('Ha sucedido algo extraño, ¡lo siento!')


#? Algunas Excepciones Útiles

"""  

Analicemos con más detalle algunas excepciones útiles (o más bien, las más comunes) que puedes 
llegar a experimentar.

- ZeroDivisionError: Se produce cuando se intenta dividir un número entre cero.
- ValueError: Se produce cuando se pasa un argumento de tipo inapropiado a una función.
- TypeError: Se produce cuando se intenta realizar una operación en un tipo de dato inapropiado.
- IndexError: Se produce cuando se intenta acceder a un índice que está fuera del rango de una 
  lista o tupla.
- AttributeError: Se produce cuando se intenta acceder a un atributo que no existe en un objeto.
- SyntaxError: Se produce cuando hay un error de sintaxis en el código.

"""


#? Por qué no puedes evitar probar tu código?

"""  

Probar tu código es esencial para garantizar su correcto funcionamiento y para detectar 
posibles errores o excepciones que puedan surgir durante su ejecución. Aunque hayas 
implementado un manejo de excepciones adecuado, siempre existe la posibilidad de que 
ocurran errores inesperados. Por lo tanto, es importante realizar pruebas exhaustivas 
para asegurarte de que tu código se comporte como se espera en diferentes situaciones.

"""

# Rastreando las rutas de ejecución.

"""  
Supón que acabas de terminar de escribir este fragmento de código:
"""

temperature = float(input('Ingresa la temperatura actual:'))

if temperature > 0:
    print("Por encima de cero")
elif temperature < 0:
    print("Por debajo de cero")
else:
    print("Cero")

"""  

Existen tres rutas o caminos de ejecución independientes en el código - ¿puedes verlas? Están 
determinadas por las sentencias if-elif-else. Por supuesto, las rutas de ejecución pueden 
construirse mediante muchas otras sentencias como bucles, o incluso bloques try-except.

Si vas a probar tu código de manera justa y quieres dormir profundamente y soñar sin pesadillas 
(las pesadillas sobre errores pueden ser devastadoras para el rendimiento de un desarrollador), 
estás obligado a preparar un conjunto de datos de prueba que obligará a tu código a negociar 
,todos los posibles caminos.

En nuestro ejemplo, el conjunto debe contener al menos tres valores flotantes: uno positivo, uno 
negativo y cero.

"""

#? Cuando Python cierra los ojos.

"""  
Tal prueba es crucial. Queremos mostrarte por qué no debes omitirlo. Observa el siguiente código:
"""

temperature = float(input('Ingresa la temperatura actual:'))

if temperature > 0:
    print("Por encima de cero")
elif temperature < 0:
    prin("Por debajo de cero")
else:
    print("Cero")

"""  

Introdujimos intencionalmente un error en el código - esperamos que tus ojos atentos lo noten 
de inmediato. Sí, eliminamos solo una letra y, en efecto, la invocación válida de la función 
print() se convierte en la obviamente inválida invocación "prin()". No existe tal función 
como "prin()" en el alcance de nuestro programa, pero ¿es realmente obvio para Python?

Ejecuta el código e ingresa un 0.

Como puedes ver, el código finaliza su ejecución sin ningún obstáculo.

¿Cómo es eso posible? ¿Por qué Python pasa por alto un error de desarrollador tan evidente?

¿Puedes encontrar las respuestas a estas preguntas fundamentales?

"""

#? Pruebas, pruebas y más pruebas.

"""  

La respuesta es más simple de lo esperado y también un poco decepcionante. Python - 
como seguramente sabes - es un lenguaje interpretado. Esto significa que el código 
fuente se analiza y ejecuta al mismo tiempo. En consecuencia, es posible que Python no 
tenga tiempo para analizar las líneas de código que no están sujetas a ejecución. Como 
dice un antiguo dicho de los desarrolladores: "es una característica, no un error" (no 
utilices esta frase para justificar el comportamiento extraño de tu código).

¿Entiendes ahora por qué el pasar por todos los caminos de ejecución es tan vital e 
inevitable?

Probar tu código es esencial para garantizar su correcto funcionamiento y para detectar 
posibles errores o excepciones que puedan surgir durante su ejecución. Aunque hayas 
implementado un manejo de excepciones adecuado, siempre existe la posibilidad de que 
ocurran errores inesperados. Por lo tanto, es importante realizar pruebas exhaustivas 
para asegurarte de que tu código se comporte como se espera en diferentes situaciones.

Ya sabes que tu código contiene un error o errores (lo segundo es más probable). Ahora, 
¿cómo los localizas y cómo arreglas tu código?

"""

# Error frente a depuración (Bug vs Debug)

"""  

La medida básica que un desarrollador puede utilizar contra los errores es - como era de 
esperarse - un depurador, mientras que el proceso durante el cual se eliminan los errores 
del código se llama depuración. Según un viejo chiste, la depuración es un complicado 
juego de misterio en el que eres simultáneamente el asesino, el detective y - la parte más 
dolorosa de la intriga - la víctima. ¿Estás listo para interpretar todos estos roles? 
Entonces debes armarte con un depurador.

Un depurador es una herramienta que te permite ejecutar tu código paso a paso, inspeccionar 
variables y evaluar expresiones en tiempo de ejecución. Con un depurador, puedes identificar 
la ubicación exacta de un error y comprender mejor el flujo de ejecución de tu programa.

"""

#? print debugging (depuración)

"""  

Esta forma de depuración, que se puede aplicar a tu código mediante cualquier tipo de 
depurador, a veces se denomina depuración interactiva. El significado del término se 
explica por sí mismo - el proceso necesita su interacción (la del desarrollador) para 
que se lleve a cabo.

Algunas otras técnicas de depuración se pueden utilizar para cazar errores. Es posible 
que no puedas o no quieras usar un depurador (las razones pueden variar). ¿Estás entonces 
indefenso? ¡Absolutamente no!

Puedes utilizar una de las tácticas de depuración más simples y antiguas (pero aún útil) 
conocida como la depuración por impresión. El nombre habla por sí mismo - simplemente 
insertas varias invocaciones print() adicionales dentro de tu código para generar datos 
que ilustran la ruta que tu código está negociando actualmente. Puedes imprimir los valores 
de las variables que pueden afectar la ejecución.

"""

