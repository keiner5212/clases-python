import numpy as np
import matplotlib.pyplot as plt

# Datos para el eje x
x = np.linspace(0, 10, 100)

# Datos para el primer eje y
y1 = np.sin(x)

# Datos para el segundo eje y
y2 = np.exp(x)

# Crear la figura y los ejes
fig, ax1 = plt.subplots()

# Graficar los datos en el primer eje y
ax1.plot(x, y1, 'b-', label='Función seno')
ax1.set_xlabel('Eje x')
ax1.set_ylabel('Función seno', color='b')
ax1.tick_params('y', colors='b')

# Crear el segundo eje y compartiendo el eje x
ax2 = ax1.twinx()

# Graficar los datos en el segundo eje y
ax2.plot(x, y2, 'r-', label='Función exponencial')
ax2.set_ylabel('Función exponencial', color='r')
ax2.tick_params('y', colors='r')

# Agregar leyendas y título
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')
plt.title('Gráfico con dos ejes y')

# Mostrar la gráfica
plt.show()
