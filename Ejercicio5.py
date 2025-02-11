# Dado el siguiente diccionario:
#data = {
#'Ciudad': ['Nueva York', 'Los Ángeles', 'Nueva York', 'Chicago'],
#'Ventas': [100, 150, 200, 50]
#}
#Agrupe los datos por ciudad y mostrar la suma por ciudades.
from collections import defaultdict

data = {
    'Ciudad': ['Nueva York', 'Los Ángeles', 'Nueva York', 'Chicago'],
    'Ventas': [100, 150, 200, 50]
}

ventas_por_ciudad = defaultdict(int)

for ciudad, venta in zip(data['Ciudad'], data['Ventas']):
    ventas_por_ciudad[ciudad] += venta

print("Ventas por ciudad:", dict(ventas_por_ciudad))
