import pandas as pd

# Crear un DataFrame de ejemplo
data = {
    'Nombre': ['Juan', 'María', 'Pedro', 'Ana'],
    'Edad': [25, 30, 21, 28],
    'Ciudad': ['Madrid', 'Barcelona', 'Sevilla', 'Valencia']
}

df = pd.DataFrame(data)

# Imprimir el DataFrame
print("DataFrame original:")
print(df)

# Métodos comunes de los DataFrames de Pandas

# head(): Muestra las primeras filas del DataFrame (por defecto, muestra las 5 primeras filas)
print("\nPrimeras filas del DataFrame:")
print(df.head())

# tail(): Muestra las últimas filas del DataFrame (por defecto, muestra las 5 últimas filas)
print("\nÚltimas filas del DataFrame:")
print(df.tail())

# describe(): Proporciona estadísticas descriptivas del DataFrame
print("\nEstadísticas descriptivas del DataFrame:")
print(df.describe())

# info(): Muestra información sobre el DataFrame, como el tipo de dato de cada columna y el uso de memoria
print("\nInformación del DataFrame:")
df.info()

# shape: Devuelve las dimensiones del DataFrame (número de filas, número de columnas)
print("\nDimensiones del DataFrame:")
print(df.shape)

# columns: Devuelve el nombre de las columnas del DataFrame
print("\nColumnas del DataFrame:")
print(df.columns)

# loc[]: Acceso a filas y columnas mediante etiquetas
print("\nAcceso a filas y columnas por etiquetas:")
print(df.loc[1:2, 'Nombre':'Edad'])

# iloc[]: Acceso a filas y columnas mediante índices enteros
print("\nAcceso a filas y columnas por índices enteros:")
print(df.iloc[1:3, 0:2])

# groupby(): Agrupa el DataFrame por una o más columnas y permite realizar operaciones de agregación
print("\nAgrupación y agregación del DataFrame:")
grupo_ciudad = df.groupby('Ciudad')
print(grupo_ciudad)
print("\nOperaciones de agregación:")
# Excluir la columna 'Nombre' del cálculo de la media
print(grupo_ciudad['Edad'].mean())

# sort_values(): Ordena el DataFrame según los valores de una o más columnas
print("\nOrdenamiento del DataFrame:")
df_ordenado = df.sort_values(by='Edad', ascending=False)
print(df_ordenado)

# drop(): Elimina filas o columnas del DataFrame
print("\nEliminación de filas y columnas:")
df_reducido = df.drop(columns=['Ciudad'])
print(df_reducido)

# set_index(): Establece una columna como índice del DataFrame
print("\nEstablecimiento de índice:")
df_con_indice = df.set_index('Nombre')
print(df_con_indice)

# Acceder a los valores del DataFrame utilizando el atributo df.values
print("\nvalores del DataFrame utilizando el atributo df.values:")
array_values = df.values
print(array_values)

# unique(): Devuelve los valores únicos de una columna
print("\nValores únicos de la columna 'Ciudad':")
print(df['Ciudad'].unique())

# value_counts(): Cuenta la frecuencia de cada valor único en una columna
print("\nFrecuencia de valores en la columna 'Ciudad':")
print(df['Ciudad'].value_counts())

# dropna(): Elimina las filas que contienen valores NaN
print("\nEliminación de filas con valores NaN:")
df_sin_nan = df.dropna()
print(df_sin_nan)

# replace(): Reemplaza valores en el DataFrame
print("\nReemplazo de valores en el DataFrame:")
df_reemplazado = df.replace({'Madrid': 'MAD', 'Barcelona': 'BCN'})
print(df_reemplazado)

# astype(): Cambia el tipo de datos de una columna
print("\nCambio de tipo de datos de la columna 'Edad':")
df['Edad'] = df['Edad'].astype(float)
df.info()
