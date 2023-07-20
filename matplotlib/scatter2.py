import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Utiliza el estilo 'bmh' para el gráfico (opcional, puedes cambiarlo a otro estilo si prefieres)
plt.style.use('bmh')

# Crea una figura y un objeto de ejes (subplot)
fig, ax = plt.subplots()

# Lee los datos desde un archivo CSV
informacion = pd.read_csv("./recursos/LSV-0&001.csv")
x = informacion["Cell Potential[V]"].tolist()
y = informacion[' "Cell Current[A]"'].tolist()

# Grafica los datos x e y como una línea con estilo de puntos y dos puntos de separación
ax.plot(x, y, linestyle=":")

# Genera tamaños aleatorios para los puntos basado en la cantidad de puntos en x
sizes = np.random.uniform(20, 80, len(x))

# Genera colores aleatorios para los puntos basado en la cantidad de puntos en x
colors = sorted(np.random.normal(0, 100, len(x)).tolist(), reverse=False)

# Grafica los puntos utilizando scatter plot
ax.scatter(x, y, s=sizes, c=colors, cmap="inferno")

# Muestra el gráfico
plt.show()
