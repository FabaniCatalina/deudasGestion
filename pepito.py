import pandas as pd

# Lee el archivo CSV y selecciona las columnas 0, 1 y 2
df = pd.read_csv('transacciones_simple.txt', sep=" " ,usecols=[0, 1, 2])

# Imprime las primeras 5 filas del DataFrame
print(df.head())
