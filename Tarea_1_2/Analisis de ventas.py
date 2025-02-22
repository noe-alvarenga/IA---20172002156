# -*- coding: utf-8 -*-
"""Untitled3.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/19_cbb3vo2upnKRtvr4MVSj6Pbt0KrAQ0
"""

import pandas as pd

ventas_df = pd.read_csv('ventas.csv')

print(ventas_df)

# 1. Calcular la cantidad total de productos vendidos por categoria
cantidad_por_producto = ventas_df.groupby('Producto')['Cantidad'].sum()
print("Cantidad total de productos vendidos por categoría:")
print(cantidad_por_producto)

# 2 Determine cuál es el producto con el mayor total de ventas.
ventas_df['Total_Ventas'] = ventas_df['Cantidad'] * ventas_df['Precio_Unitario']
producto_mayor_ventas = ventas_df.groupby('Producto')['Total_Ventas'].sum().idxmax()
print("\nProducto con el mayor total de ventas:", producto_mayor_ventas)

# 3 Encuentre el precio promedio de los productos vendidos.
precio_promedio = (ventas_df['Cantidad'] * ventas_df['Precio_Unitario']).sum() / ventas_df['Cantidad'].sum()
precio_promedio = round(precio_promedio, 2)
print("\nPrecio promedio de los productos vendidos:", precio_promedio)



