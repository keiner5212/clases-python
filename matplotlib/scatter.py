import matplotlib.pyplot as plt
import numpy as np

# Utiliza el estilo 'bmh' para el gráfico (opcional, puedes cambiarlo a otro estilo si prefieres)
plt.style.use('bmh')

# Crea una figura y un objeto de ejes (subplot)
fig, ax = plt.subplots()

# Genera datos para x e y
x = np.linspace(0, 5, 100)
y = np.random.normal(0, 5, 100)

# Genera tamaños aleatorios para los puntos
sizes = np.random.uniform(20, 80, 100)

# Crea una lista vacía para los colores de los puntos
colors = []

# Asigna colores a los puntos en base a los valores de y
for valor in y:
    if valor >= 5:
        colors.append(50)
    elif valor > 0:
        colors.append(80)
    else:
        colors.append(np.random.randint(0, 100))

# Grafica los puntos utilizando scatter plot
ax.scatter(x, y, s=sizes, c=colors, cmap="inferno")

# Muestra el gráfico
plt.show()
