
#TODO Retornando el Resultado de una Función

#? Efectos y Resultados: La Instrucción return

"""  

Las funciones al igual que las funciones matemáticas pueden tener resultados.

Para lograr que las funciones devuelvan un valor (pero no solo para ese propósito) se utiliza
la instrucción `return` (regresar o retornar).

La instrucción `return` se utiliza para devolver un valor desde una función. Cuando se ejecuta 
`return`, la función finaliza su ejecución y el valor especificado se envía de vuelta al lugar 
donde se llamó a la función.

La instrucción `return` tiene dos variantes diferentes:

1. `return` sin valor: En este caso, la función simplemente termina su ejecución y no devuelve 
   ningún valor. Esto es útil cuando se desea que la función realice una acción, pero no se 
   necesita un resultado.

2. `return` con valor: Aquí, la función devuelve un valor específico. Este valor puede ser de 
   cualquier tipo de dato, como un número, una cadena de texto, una lista, etc. El valor devuelto 
   puede ser utilizado en el lugar donde se llamó a la función.

"""

# return sin una expresión

def happy_new_year(wishes = True):
    print("Tres...")
    print("Dos...")
    print("Uno...")
    if not wishes:
        return

    print("¡Feliz año nuevo!")

happy_new_year()
happy_new_year(False)
print("")

# return con una expresión

def boring_function():
    return 123

x = boring_function()

print("La función boring_function ha devuelto su resultado. Es:", x)
print("")

"""  

La instrucción return, enriquecida con la expresión (la expresión es muy simple aquí), "transporta" 
el valor de la expresión al lugar donde se ha invocado la función.

El resultado se puede usar libremente aquí, por ejemplo, para ser asignado a una variable.

También puede ignorarse por completo y perderse sin dejar rastro.

"""

def boring_function():
    print("'Modo aburrimiento' ON.")
    return 123

print("¡Esta lección es interesante!")
boring_function()
print("Esta lección es aburrida...")
print("")

"""  

¿Está mal? De ninguna manera.

La única desventaja es que el resultado se ha perdido irremediablemente.

No olvides:

- siempre se te permite ignorar el resultado de la función y estar satisfecho con el efecto de la 
  función (si la función tiene alguno)
- si una función intenta devolver un resultado útil, debe contener la segunda variante de la 
  instrucción return.

Espera un segundo - ¿significa esto que también hay resultados inútiles? Sí, en cierto sentido.

"""

#? Unas pocas palabras sobre None

"""  

La instrucción return puede devolver un valor útil o no útil. En el caso de que no se devuelva un 
valor útil, la función devolverá None.

Sus datos no representan valor razonable alguno, en realidad, no es un valor en lo absoluto; por
lo tanto, no debe participar en ninguna expresión.

Nota: 'None' es una palabra clave reservada.

Solo existen dos tipos de circunstancias en las que 'None' se puede utilizar de manera segura:

1. Cuando se le asigna a una variable (o se devuelve como el resultado de una función)
2. Cuando se compara con una variable para diagnosticar su estado interno.

"""

value = None
if value is None:
    print("Lo siento, no contienes ningún valor")
print("")

"""  

No olvides esto: si una función no devuelve un cierto valor utilizando una cláusula de expresión 
return, se asume que devuelve implícitamente None.

Vamos a probarlo.

Echa un vistazo al código en el editor.

"""

def strange_function(n):
    if(n % 2 == 0):
        return True
    
print(strange_function(2))
print(strange_function(1))

"""  

La función strange_function devuelve un valor útil (True) cuando se le pasa un número par.
En caso contrario, devuelve None implícitamente.

"""