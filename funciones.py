# Una función es un bloque de código reutilizable que realiza una tarea específica.
# Las funciones se definen utilizando la palabra clave def seguida del nombre de
# la función y una lista de parámetros entre paréntesis. Los parámetros son valores
# que se pasan a la función cuando se llama. Dentro de la función, los parámetros se
# comportan como variables locales.

# Definimos una función llamada saludar que recibe un parámetro llamado nombre
def saludar(nombre):
    # Dentro de la función, utilizamos el parámetro nombre para mostrar un mensaje personalizado
    print(f"Hola, {nombre}!")


# Llamamos a la función saludar y le pasamos el valor "Juan" como parámetro
saludar("Juan")

# Las funciones también pueden devolver valores utilizando la palabra clave return


def sumar(a, b):
    # Calculamos la suma de los parámetros a y b y la devolvemos como resultado de la función
    resultado = a + b
    return resultado


# Llamamos a la función sumar y le pasamos los valores 3 y 4 como parámetros
suma = sumar(3, 4)
# Imprimimos el resultado devuelto por la función
print(suma)
