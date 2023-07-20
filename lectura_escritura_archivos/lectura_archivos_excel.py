import pandas as pd

ruta = "./recursos/excel.xlsx"

# Leer el archivo Excel utilizando pandas
lectura = pd.read_excel(ruta)

# Obtener los valores de todas las filas del archivo
filas = lectura.values

# Iterar sobre cada fila e imprimir su contenido
for fila in filas:
    print(fila)
