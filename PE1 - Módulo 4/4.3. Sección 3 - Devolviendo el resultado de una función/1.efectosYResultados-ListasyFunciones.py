
#TODO Efectos y Resultados: Listas y Funciones

"""  

Las funciones pueden interactuar con listas de varias maneras. Pueden recibir listas como argumentos, 
devolver listas como resultados o modificar listas directamente.

Veamos algunos ejemplos.

"""

# Listas como argumentos
def list_sum(lst):
    s = 0

    for elem in lst:
        s += elem

    return s

print(list_sum([1, 2, 3, 4, 5]))  # Imprime: 15
print("")

# Listas como resultados
def strange_list_fun(n):
    strange_list = []
    
    for i in range(0, n):
        strange_list.insert(0, i)
    
    return strange_list

print(strange_list_fun(5)) # Imprime: [4, 3, 2, 1, 0]
