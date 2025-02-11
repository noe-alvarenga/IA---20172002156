# Crea un programa que almacene información sobre productos y sus precios en un diccionario, esta información
# debe ser ingresada desde teclado.
productos = {}

while True:
    nombre = input("Ingrese el nombre del producto (o 'salir' para terminar): ")
    if nombre.lower() == 'salir':
        break
    precio = float(input(f"Ingrese el precio de {nombre}: "))
    productos[nombre] = precio

print("Diccionario de productos:", productos)
