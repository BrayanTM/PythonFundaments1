
#TODO Funciones 
#? Por qué necesitamos funciones?

"""  
Las funciones son bloques de código reutilizables que realizan una tarea específica. Nos ayudan
a organizar nuestro código, hacerlo más legible y evitar la repetición. Al encapsular la lógica 
en funciones, podemos llamar a esa lógica desde diferentes partes de nuestro programa sin tener
 que reescribir el mismo código una y otra vez.

"""

#? Descomposición de problemas
""" 

La descomposición es el proceso de dividir un problema grande y complejo en partes más pequeñas y 
manejables. Las funciones son una herramienta clave en este proceso, ya que nos permiten encapsular 
la lógica de una tarea específica en un bloque de código reutilizable. Al hacerlo, podemos abordar 
problemas complejos de manera más efectiva y centrarnos en una parte a la vez.

"""

#? De dónde provienen las funciones?
"""

Las funciones provienen de la necesidad de organizar y reutilizar el código de manera eficiente. A 
medida que los programas se vuelven más complejos, se hace evidente la importancia de dividir la 
lógica en partes más pequeñas y manejables. Las funciones nos permiten hacer precisamente eso, 
encapsulando la lógica en bloques reutilizables que pueden ser llamados desde diferentes partes 
del programa. Esta práctica no solo mejora la legibilidad del código, sino que también facilita su 
mantenimiento y actualización.

En general, las funciones provienen de al menos tres lugares:

Python:
De python mismo; varias funciones (como print(), len(), etc.) son una parte integral de python, y 
siempre están disponibles sin algún esfuerzo adicional del programador; se les llama aestas 
funciones integradas.

Módulos:
De los módulos preinstalados de python; muchas de las funciones, las cuales comúnmente son menos
utilizadas que las integradas, están disponibles en módulos instalados juntamente con Python; para 
poder utilizar estas funciones el programador debe realizar algunos pasos adicionales.

Code:
Directamente del código; tu puedes escribir tus propias funciones, colocarlas dentro del código, 
y usarlas libremente.

Existe una posibilidad más, pero se relaciona con clases, se omitirá por ahora.

"""

#? Tu primera función

""" 

Así es como se ve la definición más simple de una función: 

def function_name(parameters):
    # Cuerpo de la función

- Siempre comienza con la palabra reservada def (que significa definir)
- después de def va el nombre de la función (las reglas para darle nombre a las funciones son las 
  mismas que para las variables)
- después del nombre de la función, hay un espacio para un par de paréntesis (ahorita no contienen 
  algo, pero eso cambiará pronto)
- la línea debe de terminar con dos puntos;
- la línea inmediatamente después de def marca el comienzo del cuerpo de la función - donde varias 
  o (al menos una) instrucción anidada, será ejecutada cada vez que la función sea invocada; nota: 
  la función termina donde el anidamiento termina, se debe ser cauteloso.

"""

def message():
    print("Ingresar valor: ")

print("Inicia aqui.")
message()
print("Termina aqui.")

#? Cómo funcionan las funciones?

"""  

- cuando se invoca una función, Python recuerda el lugar donde esto ocurre y salta hacia dentro 
  de la función invocada;
- el cuerpo de la función es entonces ejecutado;
- al llegar al final de la función, Python regresa al lugar inmediato después de donde ocurrió 
  la invocación.

Existen dos consideraciones muy importantes, la primera de ella es:

- No se debe invocar una función antes de que haya sido definida.

Recuerda - Python lee el código de arriba hacia abajo. No va a adelantarse en el código para 
determinar si la función invocada está definida más adelante, (el lugar "correcto" para definirla 
es "antes de ser invocada".)

La segunda consideración es más sencilla:

- Una función y una variable no pueden compartir el mismo nombre.

"""

def message():
    print("Ingresar valor: ")

message()
a = int(input())
message()
b = int(input())
message()
c = int(input())

