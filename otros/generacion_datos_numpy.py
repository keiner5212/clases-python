import numpy as np

# Generar 100 números aleatorios con distribución estándar normal
data = np.random.standard_normal(100)
print("Números aleatorios con distribución estándar normal:")
print(data)

# Generar 50 números aleatorios con distribución normal personalizada
media = 10
ds = 2
data = np.random.normal(media, ds, 50)
print("\nNúmeros aleatorios con distribución normal personalizada:")
print(data)

# Generar una matriz 3x3 con valores aleatorios
data = np.random.randn(3, 3)
print("\nMatriz aleatoria 3x3:")
print(data)

# Generar una lista de 101 números enteros aleatorios entre 0 y 100
np.random.seed(3)
data = np.random.randint(0, 101, 101)
print("\nLista de números enteros aleatorios:")
print(data)

# Generar 50 números aleatorios en el rango [0, 1) con distribución uniforme
data = np.random.uniform(0, 1, 50)
print("\nNúmeros aleatorios con distribución uniforme:")
print(data)

# Generar 20 números aleatorios con distribución exponencial
data = np.random.exponential(scale=1/0.5, size=20)
print("\nNúmeros aleatorios con distribución exponencial:")
print(data)

# Generar un arreglo de 50 números espaciados uniformemente en el rango [0, 2π]
data = np.linspace(0, 2*np.pi, 50)
print("\nArreglo de números espaciados uniformemente:")
print(data)

# Crear un arreglo de números enteros en un rango específico
data = np.arange(0, 10, 2)
print("\nArreglo de números enteros usando arange:")
print(data)

# Reshape de un arreglo unidimensional a una matriz
data = np.arange(12).reshape(3, 4)
print("\nMatriz generada a partir de un arreglo unidimensional:")
print(data)

# Operaciones matemáticas con arreglos
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
suma = np.add(a, b)
resta = np.subtract(a, b)
producto_punto = np.dot(a, b)
print("\nOperaciones matemáticas con arreglos:")
print("Suma:", suma)
print("Resta:", resta)
print("Producto punto:", producto_punto)

# Funciones matemáticas en arreglos
data = np.array([0, np.pi/2, np.pi])
seno = np.sin(data)
coseno = np.cos(data)
exponencial = np.exp(data)
print("\nFunciones matemáticas en arreglos:")
print("Seno:", seno)
print("Coseno:", coseno)
print("Exponencial:", exponencial)

# Estadísticas en arreglos
data = np.array([1, 2, 3, 4, 5])
promedio = np.mean(data)
mediana = np.median(data)
desviacion_estandar = np.std(data)
print("\nEstadísticas en arreglos:")
print("Promedio:", promedio)
print("Mediana:", mediana)
print("Desviación estándar:", desviacion_estandar)

# Redondeo de valores en un arreglo
data = np.array([1.3, 2.7, 4.1])
redondeo = np.round(data)
print("\nRedondeo de valores en un arreglo:")
print(redondeo)

# Ordenar elementos de un arreglo
data = np.array([3, 1, 4, 2, 5])
ordenado = np.sort(data)
print("\nOrdenar elementos de un arreglo:")
print(ordenado)

# Obtener el índice del valor máximo y mínimo en un arreglo
data = np.array([3, 1, 4, 2, 5])
indice_maximo = np.argmax(data)
indice_minimo = np.argmin(data)
print("\nObtener el índice del valor máximo y mínimo en un arreglo:")
print("Índice máximo:", indice_maximo)
print("Índice mínimo:", indice_minimo)
