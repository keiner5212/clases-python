# Importa las bibliotecas matplotlib.pyplot y numpy
import matplotlib.pyplot as plt
import numpy as np

# Define una función que toma un valor x y devuelve 2*x+5


def funcion1(x):
    return (2*x+5)


# Establece el estilo de la gráfica como "ggplot"
plt.style.use("bmh")
# los estilos basicos disponibles para los estilos de grafica son:
# 'bmh'
# 'classic'
# '_mpl-gallery'
# 'dark_background'
# 'fast'
# 'fivethirtyeight'
# 'ggplot'
# 'grayscale'
# 'seaborn-v0_8'
# 'seaborn-v0_8-bright'
# 'seaborn-v0_8-colorblind'
# 'seaborn-v0_8-dark'
# 'seaborn-v0_8-darkgrid'
# 'seaborn-v0_8-deep'
# 'seaborn-v0_8-muted'
# 'seaborn-v0_8-notebook'
# 'seaborn-v0_8-paper'
# 'seaborn-v0_8-pastel'
# 'seaborn-v0_8-poster'
# 'seaborn-v0_8-talk'
# 'seaborn-v0_8-ticks'
# 'seaborn-v0_8-white'
# 'seaborn-v0_8-whitegrid'
# 'Solarize_Light2'
# 'tableau-colorblind10'

# Crea un array de 100 valores equiespaciados entre 0 y 2*pi
x = np.linspace(0, 2*np.pi, 50)

# Calcula el seno y el coseno de cada valor en el array x
y1 = np.sin(x)
y2 = np.cos(x)
# Calcula el valor de la función1 para cada valor en el array x

# Crea una gráfica con los valores de x e y1, y1 y y3
plt.plot(x, y1, label="sen(x)", linewidth=2.0,
         color="#42ab49", linestyle=(5,[10,10]))
plt.plot(x, y2, label="cos(x)", linewidth=2.0)

# importante

# label: Una cadena que especifica la etiqueta para la leyenda de la gráfica.

# linewidth: Un valor numérico que especifica el ancho de la línea en puntos.

# color: Una cadena o tupla que especifica el color de la línea. Los colores
# pueden especificarse como una cadena con un nombre de color reconocido por
# Matplotlib (por ejemplo, 'red', 'blue', 'green', etc.), como una cadena con
# un código de color hexadecimal (por ejemplo, '#FF0000' para rojo), o como
# una tupla con valores RGB o RGBA (por ejemplo, (1, 0, 0) para rojo).

# linestyle: Una cadena que especifica el estilo de línea. Los estilos de línea
# disponibles son:
# '-' o 'solid': línea sólida
# '--' o 'dashed': línea discontinua
# '-.' o 'dashdot': línea a puntos y rayas
# ':' o 'dotted': línea punteada
# 'None', ' ' o '': sin línea


# Dibuja una línea horizontal en la posición y=0
plt.axhline(y=0, color='#6b6161')
# Dibuja una línea vertical en la posición x=0
plt.axvline(x=0, color='#6b6161')

# Establece el título, las etiquetas de los ejes x e y, y la leyenda de la gráfica
plt.title("Graficas simples")
plt.xlabel("x (radianes)")
plt.ylabel("y1(x) y y2(x)")
plt.legend()

# Muestra la gráfica en pantalla
plt.show()
