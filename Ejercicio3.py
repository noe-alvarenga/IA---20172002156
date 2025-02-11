# Crea un programa que devuelva una lista con todos los elementos únicos de otra lista.
def elementos_unicos(lista):
    return list(set(lista))

lista = [1, 2, 2, 3, 4, 4, 5]
print("Elementos únicos:", elementos_unicos(lista))
