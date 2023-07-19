import sympy as sp  # Importamos la librería sympy

x = sp.Symbol("x")  # Definimos un símbolo x
y = sp.Function("y")(x)  # Definimos una función y de x

f_texto = "x**2 + 2*x - 3"  # Definimos una expresión matemática en forma de texto

# Convertimos la expresión en texto a una expresión simbólica
f = sp.sympify(f_texto)

fPrima = sp.diff(f, x)  # Calculamos la derivada de f con respecto a x
print(fPrima)  # Imprimimos el resultado

# Calculamos la integral indefinida de f con respecto a x
fIntegral = sp.integrate(f, x)
print(fIntegral)  # Imprimimos el resultado

# Calculamos la integral definida de f con respecto a x entre los límites 5 y 8
fIntegral_definida = sp.integrate(f, (x, 5, 8))
print(fIntegral_definida)  # Imprimimos el resultado

# Simplificar expresiones
expr = (x**2 + 2*x + 1)/(x + 1)  # Se define una expresión matemática
# Se utiliza la función sp.simplify para simplificar la expresión
expr_simplificado = sp.simplify(expr)
# Se imprime el resultado de la simplificación
print(f"Expresión simplificada: {expr_simplificado}")

# Resolver ecuaciones
# Se utiliza la función sp.solve para resolver la ecuación x**2 + 2*x - 3 = 0
solucion = sp.solve(x**2 + 2*x - 3, x)
# Se imprime el resultado de la solución
print(f"Solución de la ecuación: {solucion}")

# Calcular límites
# Se utiliza la función sp.limit para calcular el límite de sin(x)/x cuando x tiende a 0
limite = sp.limit(sp.sin(x)/x, x, 0)
print(f"Límite: {limite}")  # Se imprime el resultado del límite

# Series de Taylor
# Se utiliza la función sp.series para calcular la serie de Taylor de exp(x) alrededor del punto x=0 con un orden de 5
serie = sp.series(sp.exp(x), x, 0, 5)
# Se imprime el resultado de la serie de Taylor
print(f"Serie de Taylor: {serie}")
