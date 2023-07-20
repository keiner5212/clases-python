import pandas as pd

# Define la ruta del archivo CSV
ruta="./recursos/LSV-0&001.csv"

# Utiliza pandas para leer el archivo CSV y crear un DataFrame
lectura=pd.read_csv(ruta)
# Imprime las primeras 60 filas del DataFrame
# print(lectura.head(60))

# Convierte el DataFrame a un array de numpy
filas=lectura.values

# Recorre cada fila del array de numpy
for fila in filas:
    # Imprime la fila
    print((fila))
