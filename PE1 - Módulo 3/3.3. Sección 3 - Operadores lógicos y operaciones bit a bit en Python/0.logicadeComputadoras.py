
#TODO Operadores lógicos y operaciones bit a bit en Python
#TODO Lógica de Computadoras

#? El operador lógico AND

"""  

Un operador de conjunción lógica en python es la palabra and. Es un operador
binario con una prioridad inferior a la expresada por los operadores de
comparación. Nos permite codificar condiciones complejas sin el uso de
paréntesis como este.

#* counter > 0 and value == 100

El operador and devuelve True si ambos operandos son verdaderos, de lo
contrario devuelve False. En el caso de que uno de los operandos sea
falso, el operador and devuelve el valor del operando falso. Si ambos
operandos son verdaderos, devuelve el valor del último operando.

El resultado proporcionado por el operador and se puede determinar sobre la
base de la tabla de verdad.

| A     | B     | A and B |
|-------|-------|---------|
| True  | True  | True    |
| True  | False | False   |
| False | True  | False   |
| False | False | False   |

En Python, el operador and se puede utilizar con cualquier tipo de objeto,
no solo con valores booleanos. Por ejemplo, si uno de los operandos es un
número cero, el operador and devolverá ese número cero como resultado.
Si ambos operandos son números distintos de cero, el operador and devolverá
el último operando. Esto se debe a que en Python, los valores numéricos
cero se consideran falsos, mientras que cualquier número distinto de cero
se considera verdadero.



"""

#? El operador lógico OR

"""  

Un operador de disyunción es la palabra or. Es un operador binario con una
prioridad más baja que and (al igual que + en comparación con *). Su tabala
de verdad es la siguiente:

| A     | B     | A or B  |
|-------|-------|---------|
| True  | True  | True    |
| True  | False | True    |
| False | True  | True    |
| False | False | False   |

El operador or devuelve True si al menos uno de los operandos es verdadero.
Si ambos operandos son falsos, devuelve False. En el caso de que uno de los
operandos sea verdadero, el operador or devuelve el valor del operando
verdadero. Si ambos operandos son verdaderos, devuelve el valor del último
operando.

Al igual que con and, el operador or se puede utilizar con cualquier tipo
de objeto. Si uno de los operandos es un número distinto de cero, el
operador or devolverá ese número como resultado. Si ambos operandos son
números cero, el operador or devolverá el último operando (cero).

"""

#? El operador lógico NOT

"""  

Además, hay otro operador que se puede aplicar para condicones de construcción.
Es un operador unario que realiza una negación lógica. Su funcionamiento es
simple: convierte la verdad en falso y lo falso en verdad.

Este operador se escribe con la palabra not, y su prioridad es muy alta: igual
que el unario + y -. Su tabla de verdad es la siguiente:

| A     | not A |
|-------|-------|
| True  | False |
| False | True  |

El operador not se puede utilizar con cualquier tipo de objeto. Devuelve
False si el operando es un valor verdadero y True si el operando es un
valor falso. En Python, los valores numéricos cero se consideran falsos,
mientras que cualquier número distinto de cero se considera verdadero.

"""