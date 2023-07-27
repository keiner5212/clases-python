# Importa las bibliotecas matplotlib.pyplot y numpy
import matplotlib.pyplot as plt
import numpy as np

# Crea un array de 100 valores equiespaciados entre 0 y 2*pi
x = np.linspace(0, 2*np.pi, 100)

# Calcula el seno y el coseno de cada valor en el array x
y1 = np.sin(x)
y2 = np.cos(x)

# Crea una gráfica con los valores de x e y1 y y2
plt.plot(x, y1, label="sen(x)")
plt.plot(x, y2, label="cos(x)")

# Establece el título, las etiquetas de los ejes x e y, y la leyenda de la gráfica
plt.title("Gráfica de sen(x) y cos(x)")
plt.xlabel("x (radianes)")
plt.ylabel("y")
plt.legend()

# Agrega un texto en la gráfica
plt.text(np.pi, -1.05, "Mínimo local", ha="center")


# La función annotate se utiliza para agregar anotaciones a la gráfica
plt.annotate('Máximo local',  # El texto que se va a mostrar en la anotación
             xy=(np.pi/2, 1),  # La posición del punto que se va a anotar
             # La posición donde se va a colocar el texto
             xytext=(np.pi/2+0.5, 1),
             arrowprops=dict(facecolor='black', shrink=0.05))  # Propiedades de la flecha que señala el punto anotado

"""
arrowprops: Un diccionario que especifica las propiedades de la flecha que se va a 
dibujar para señalar el punto anotado.

facecolor: Una cadena o tupla que especifica el color de la flecha. Los colores pueden 
especificarse como una cadena con un nombre de color reconocido por Matplotlib 
(por ejemplo, "red", "blue", "green", etc.), como una cadena con un código de color hexadecimal 
(por ejemplo, "#FF0000" para rojo), o como una tupla con valores RGB o RGBA (por ejemplo, (1, 0, 0)
para rojo).

shrink: Un valor numérico que especifica cuánto se debe reducir la longitud de la flecha. 
Un valor de 0 significa que no se reduce la longitud, mientras que un valor de 1 significa 
que se reduce completamente.
"""


# Muestra la gráfica en pantalla
plt.show()
