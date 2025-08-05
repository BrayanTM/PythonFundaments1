
#TODO Bucles con For

"""
Otro tipo de bucle disponible en Python proviene de la observación 
de que a veces es más importante contar los "giros o vueltas" del 
bucle que verificar las condiciones.

Imagina que el cuerpo de un bucle debe ejecutarse exactamente cien 
veces. Si deseas utilizar el bucle while para hacerlo, puede tener 
este aspecto:

i = 0
while i < 100:
    # do_something()
    i += 1

Sería bueno si alguien pudiera hacer esta cuenta aburrida por ti. 
¿Es eso posible?

Por supuesto que lo es - hay un bucle especial para este tipo de 
tareas, y se llama for.

En realidad, el bucle for está diseñado para realizar tareas más 
complicadas, puede "explorar" grandes colecciones de datos elemento 
por elemento. Te mostraremos como hacerlo pronto, pero ahora 
presentaremos una variante más sencilla de su aplicación.

Observa el fragmento de código:

for i in range(100):
    # do_something()
    pass
    
Existen algunos elementos nuevos. Déjanos contarte sobre ellos:

- la palabra reservada for abre el bucle for; nota - No hay condición 
  después de eso; no tienes que pensar en las condiciones, ya que se 
  verifican internamente, sin ninguna intervención.
- cualquier variable después de la palabra reservada for es la variable 
  de control del bucle; cuenta los giros del bucle y lo hace 
  automáticamente.
- la palabra reservada in introduce un elemento de sintaxis que describe 
  el rango de valores posibles que se asignan a la variable de control.
- la función range() (esta es una función muy especial) es responsable 
  de generar todos los valores deseados de la variable de control; en 
  nuestro ejemplo, la función creará (incluso podemos decir que 
  alimentará el bucle con) valores subsiguientes del siguiente conjunto: 
  0, 1, 2 .. 97, 98, 99; nota: en este caso, la función range() comienza 
  su trabajo desde 0 y lo finaliza un paso (un número entero) antes del 
  valor de su argumento.
- nota la palabra clave pass dentro del cuerpo del bucle - no hace nada 
  en absoluto; es una instrucción vacía - la colocamos aquí porque la 
  sintaxis del bucle for exige al menos una instrucción dentro del cuerpo 
  (por cierto - if, elif, else y while expresan lo mismo).

"""
# Ejemplo de bucle for en Python con un argumento de range()
for i in range(10): #<-- Inicializamos i con 0 y lo incrementamos hasta 9
    print("El valor de i es", i)

# Ejemplo de bucle for en Python con dos argumentos de range()
for i in range(2, 8): #<-- Inicializamos i con 2 y lo incrementamos hasta 7
    print("El valor de i es", i)

# Ejemplo de bucle for en Python con tres argumentos de range()
for i in range(2, 8, 3): #<-- Inicializamos i con 2 y lo incrementamos hasta 7 en pasos de 3
    print("El valor de i es", i)

#? Nota: Si el conjunto generado por la función range() no contiene
#? ningún valor, el bucle for no se ejecutará ni una sola vez.
for i in range(0): #<-- No hay valores en el rango, por lo que no se ejecuta
    print("Esto no se imprimirá porque el rango está vacío")

for i in range(1, 1): #<-- No hay valores en el rango, por lo que no se ejecuta
    print("El valor de i es", i)

#? Nota: el conjunto generado por range() debe ordenarse en un orden 
#? ascendente. No hay forma de forzar el range() para crear un conjunto 
#? en una forma diferente. Esto significa que el segundo argumento de 
#? range() debe ser mayor que el primero.

for i in range(2, 1): #<-- No hay valores en el rango, por lo que no se ejecuta
    print("El valor de i es", i)

# Echemos un vistazo a un programa corto cuya tarea es escribir algunas 
# de las primeras potencias de dos:

power = 1
for expo in range(16):
    print("2 a la potencia de", expo, "es", power)
    power *= 2