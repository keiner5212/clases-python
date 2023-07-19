import matplotlib.pyplot as plt
import numpy as np

# Crear una figura de tamaño 7x5
fig = plt.figure(figsize=[7, 5])

# Agregar un subplot a la figura
ax1 = fig.add_subplot(1, 1, 1)

# Crear un arreglo de valores para el eje x
x1 = np.linspace(10, 30, 20)
# Crear tres arreglos de valores aleatorios para el eje y
y1 = np.random.normal(50, 20, 20)
y2 = .4*y1
y3 = np.random.normal(50, 20, 20)

# Inicializar listas vacías para almacenar los valores y colores de cada barra
y1Fix = []
c1 = []
y2Fix = []
c2 = []
y3Fix = []
c3 = []

# Iterar sobre los valores de y1
for i in range(0, len(y1)):
    # Crear diccionarios con los valores y colores de cada barra
    dic1 = {
        "valor": y1[i],
        "grupo": "#847edd"
    }
    dic2 = {
        "valor": y2[i],
        "grupo": "#6b6161"
    }
    dic3 = {
        "valor": y3[i],
        "grupo": "#912222"
    }
    # Ordenar los diccionarios por valor
    alturasOrdenadas = sorted([dic1, dic2, dic3], key=lambda x: x["valor"])
    # Agregar los valores y colores ordenados a las listas correspondientes
    y1Fix.append(alturasOrdenadas[2]["valor"])
    c1.append(alturasOrdenadas[2]["grupo"])
    y2Fix.append(alturasOrdenadas[1]["valor"])
    c2.append(alturasOrdenadas[1]["grupo"])
    y3Fix.append(alturasOrdenadas[0]["valor"])
    c3.append(alturasOrdenadas[0]["grupo"])

# Crear un gráfico de barras para cada conjunto de datos
ax1.bar(x1, y1Fix, color=c1, label="y1Fix")
ax1.bar(x1, y2Fix, color=c2, label="y2Fix")
ax1.bar(x1, y3Fix, color=c3, label="y3Fix")

# Establecer los límites del eje y y las marcas del eje y
ax1.set(ylim=(0, 100), yticks=np.arange(0, 100, 5))

# Agregar una leyenda al gráfico
ax1.legend(ncol=3)

# Establecer el color de los bordes del gráfico
ax1.spines["left"].set_color("k")
ax1.spines["bottom"].set_color("k")
ax1.spines["top"].set_color("k")
ax1.spines["right"].set_color("k")

# Establecer el grosor de los bordes del gráfico
ax1.spines["left"].set_linewidth(2)
ax1.spines["bottom"].set_linewidth(2)
ax1.spines["top"].set_linewidth(2)
ax1.spines["right"].set_linewidth(2)

# Establecer la visibilidad de los bordes del gráfico
ax1.spines["left"].set_visible(True)
ax1.spines["bottom"].set_visible(True)
ax1.spines["top"].set_visible(False)
ax1.spines["right"].set_visible(False)

# Establecer el estilo de línea de los bordes del gráfico
ax1.spines["left"].set_linestyle((0, [2, 2]))
ax1.spines["bottom"].set_linestyle("--")

# Establecer el color del borde izquierdo del gráfico
ax1.spines["left"].set_color("#847edd")

# Establecer el estilo del extremo del borde izquierdo del gráfico
ax1.spines["left"].set_capstyle("round")

# Agregar una cuadrícula al gráfico en el eje y
ax1.grid(True, color="k", alpha=.2, axis="y")

# Mostrar el gráfico
plt.show()
