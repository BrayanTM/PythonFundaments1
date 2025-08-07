
#TODO Funciones vs Métodos

"""  

En Python, las funciones y los métodos son dos conceptos relacionados pero 
distintos. Ambos se utilizan para encapsular código que puede ser reutilizado, 
pero tienen diferencias clave en su uso y contexto.

Un método es un tipo específico de función - se comporta como una función y se
parece a una fucnión, pero difiere en la forma en que actúa y en su estilo de
invocación.

Una función no pertenece a ningun lado - obtiene datos, puede crear nuevos datos
y (generalmente) produce un resultado.

Un método hace todas estas cosas, pero también puede cambiar el estado de una
entidad seleccionada.

Un método es propiedad de los datos para los que trabaja, mientras que una
función es propiedad de todo el código.

En general, una invocación de función típica puede tener este aspecto:

result = function(arg)

La función toma un argumento y devuelve un resultado.

En cambio, una invocación de método se ve así:

result = object.method(arg)

Aquí, el método es llamado en un objeto específico y puede acceder a los datos
de ese objeto, además de tomar argumentos adicionales.

En resumen, las funciones son independientes y pueden ser llamadas en cualquier
parte del código, mientras que los métodos están asociados a objetos y pueden
interactuar con sus datos internos. Ambos son fundamentales para la programación
en Python y se utilizan según el contexto y la necesidad.

"""