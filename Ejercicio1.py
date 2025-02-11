# 1. Crea un programa que sume todos los números de una lista (sin usar el método nativo de Python “sum”).
def suma_lista(numeros):
    total = 0
    for num in numeros:
        total += num
    return total

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("La suma es:", suma_lista(lista))
