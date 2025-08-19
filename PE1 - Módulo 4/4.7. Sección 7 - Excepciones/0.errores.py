
#TODO Excepciones

#? Errores - El Pan Diario del Desarrollador

"""  

Los errores son situaciones inesperadas que pueden ocurrir durante la ejecución de un programa. En 
Python, los errores se manejan mediante excepciones, que son eventos que interrumpen el flujo normal 
de un programa. Cuando se produce un error, Python genera una excepción que puede ser capturada y 
manejada por el programador.

"""


#? Cuando los datos no son lo que deberían ser

"""  

Cuando los datos no son lo que deberían ser, pueden producirse errores. Por ejemplo, si un programa 
espera un número y recibe texto, se generará un error. Es importante validar los datos antes de 
procesarlos para evitar estos problemas.

"""

#? La Rama try-except

"""  

La rama try-except es una estructura de control que permite manejar excepciones en Python. El código 
que puede generar un error se coloca dentro del bloque try, y el código que maneja el error se 
coloca en el bloque except. De esta manera, el programa puede continuar ejecutándose incluso si se 
produce un error.

try:
	# Es un lugar donde
	# tu puedes hacer algo 
    # sin pedir permiso.
except:
	# Es un espacio dedicado  
    # exclusivamente para pedir perdón.

Puedes ver dos bloques aquí:

- el primero, comienza con la palabra clave reservada try este es el lugar donde se coloca el código 
  que se sospecha que es riesgoso y puede terminar en caso de un error; nota: este tipo de error lleva 
  por nombre excepción, mientras que la ocurrencia de la excepción se le denomina generar - podemos 
  decir que se genera (o se generó) una excepción;
- el segundo, la parte del código que comienza con la palabra clave reservada except esta parte fue 
  diseñada para manejar la excepción; depende de ti lo que quieras hacer aquí: puedes limpiar el 
  desorden o simplemente puede barrer el problema debajo de la alfombra (aunque se prefiere la primera 
  solución)

Entonces, podríamos decir que estos dos bloques funcionan así:

- la palabra clave reservada try marca el lugar donde intentas hacer algo sin permiso;
- la palabra clave reservada except comienza un lugar donde puedes mostrar tu talento para disculparte 
  o pedir perdón.
    
"""

#? La Excepción Confirma la Regla

try:
    value = int(input('Ingresa un número natural: '))
    print('El recíproco de', value, 'es', 1/value)        
except:
    print('No se que hacer con', value)

"""  

Resumamos lo que hemos hablado:

- cualquier fragmento de código colocado entre try y except se ejecuta de una manera muy 
  especial: cualquier error que ocurra aquí dentro no terminará la ejecución del programa. 
  En cambio, el control saltará inmediatamente a la primera línea situada después de la 
  palabra clave reservada except, y no se ejecutará ninguna otra línea del bloque try;
- el código en el bloque except se activa solo cuando se ha encontrado una excepción dentro 
  del bloque try. No hay forma de llegar por ningún otro medio;
- cuando el bloque try o except se ejecutan con éxito, el control vuelve al proceso normal 
  de ejecución y cualquier código ubicado más allá en el archivo fuente se ejecuta como si 
  no hubiera pasado nada.

Ahora queremos hacerte una pregunta: ¿Es ValueError la única forma en que el control podría 
caer dentro del bloque except?

"""