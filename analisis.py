import pandas as pd

# 1. Cargar datos
df_clientes = pd.read_csv('data/clientes.csv')
df_ventas = pd.read_csv('data/ventas.csv')

print("--- Clientes Info ---")
df_clientes.info()
print("\n--- Ventas Info ---")
df_ventas.info()

# 2. Limpiar datos (Estandarizar Ciudad)
df_clientes['Ciudad'] = df_clientes['Ciudad'].str.upper()

# 3. Unir datos (mantener todas las ventas → LEFT JOIN)
df_completo = pd.merge(df_ventas, df_clientes, on='ID_Cliente', how='left')

print("\n--- DataFrame Combinado ---")
print(df_completo)

# 4. Análisis: ¿qué ciudad compra más?
df_agrupado = df_completo.groupby('Ciudad')['Cantidad'].sum().sort_values(ascending=False)

print("\n--- Ventas por Ciudad ---")
print(df_agrupado)
