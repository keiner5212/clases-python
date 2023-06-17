import csv
listaValores=[]

# Abre el archivo CSV en modo lectura
archivo=open("./LSV-0&001.csv","r")
# Crea un objeto reader para leer el contenido del archivo CSV
contenido=csv.reader(archivo,delimiter=",")
# Recorre cada fila del archivo CSV
for fila in contenido:
    # Si la fila es la primera fila (encabezados), la omite
    if(fila==['Cell Potential[V]', ' "Cell Current[A]"']):
        continue

    # Recorre cada valor de la fila
    for i in fila:
        # Elimina los espacios en blanco y convierte el valor a float
        listaValores.append(float(i.strip(" ")))

# Cierra el archivo CSV
archivo.close()

# Imprime la suma de todos los valores del archivo CSV
print(sum(listaValores))

import pandas as pd

# Define la ruta del archivo CSV
ruta="./LSV-0&001.csv"

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
