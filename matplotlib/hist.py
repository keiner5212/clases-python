import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Lee los datos desde un archivo Excel llamado "data.xlsx" y guarda la columna "Age" en una lista llamada 'edades'.
data = pd.read_excel("data.xlsx")
edades = data["Age"].tolist()

# Lista de colores para colorear las barras del histograma.
colors = [
    # Lista de colores en formato hexadecimal.

    "#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd",
    "#8c564b", "#e377c2", "#7f7f7f", "#bcbd22", "#17becf",
    "#aec7e8", "#ffbb78", "#98df8a", "#ff9896", "#c5b0d5",
    "#c49c94", "#f7b6d2", "#c7c7c7", "#dbdb8d", "#9edae5",
    "#c6dbef", "#fdd0a2", "#b3e2cd", "#fdae6b", "#d0d1e6",
    "#e9e1f3", "#737373", "#d9d9d9", "#a6cee3", "#1f78b4",
    "#b2df8a", "#33a02c", "#fb9a99", "#e31a1c", "#fdbf6f",
    "#ff7f00", "#cab2d6", "#6a3d9a", "#ffff99", "#b15928"
]

# Crea una nueva figura con un tamaño de 8x5 pulgadas.
fig = plt.figure(figsize=[8, 5])

# Añade un único subplot (gráfico) a la figura. 1, 1, 1 indica una cuadrícula de 1 fila, 1 columna y este es el primer subplot.
ax1 = fig.add_subplot(1, 1, 1)

# Crea un histograma con los datos 'edades'.
# n: número de datos en cada bin (histograma).
# bins: bordes de los bins (rango de cada barra del histograma).
# patches: colección de objetos de las barras dibujadas.
n, bins, patches = ax1.hist(edades, edgecolor="k", bins=8)

# Itera sobre las barras del histograma y asigna colores aleatorios de la lista 'colors' a cada una.
for patch in patches:
    patch.set_facecolor(np.random.choice(colors))

# Configura las etiquetas y las posiciones de los ticks del eje x.
xticks = []
xticksLabels = []
for i in range(len(n)):
    medio = (bins[i] + bins[i + 1]) / 2
    # Calcula el punto medio de cada bin para colocar el tick.
    xticks.append(medio)
    # Crea etiquetas para cada bin en el formato "inicio-fin".
    xticksLabels.append(str(int(bins[i])) + "-" + str(int(bins[i + 1])))
    # Agrega un texto en la parte superior de cada barra con la altura de la barra (frecuencia).
    ax1.text(medio, n[i], str(n[i]), ha="center", va="bottom")

# Configura los ticks del eje x y asigna las etiquetas creadas anteriormente.
ax1.set_xticks(xticks)
ax1.set_xticklabels(xticksLabels)

# Etiquetas para los ejes x e y y título del gráfico.
ax1.set_xlabel("Valores")
ax1.set_ylabel("Frecuencias")
ax1.set_title("Histograma")

# Muestra el gráfico.
plt.show()
