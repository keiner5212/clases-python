# Definimos una función llamada saludarGente que recibe un número variable de parámetros
def saludarGente(*nombres, otro="nada"):
    # Dentro de la función, el parámetro nombres es una tupla que contiene todos los valores pasados
    print(otro)
    for nombre in nombres:
        print(f"Hola, {nombre}")


# Llamamos a la función saludarGente y le pasamos varios valores como parámetros
saludarGente("Juan", "Keiner", "Pedro", "Javier", "Ana", otro="Este es otro atributo")

# También podemos definir una función que reciba un número variable de parámetros con nombre utilizando el caracter "**"


def saludarGenteConEdad(**nombresYEdades):
    # Dentro de la función, el parámetro nombresYEdades es un diccionario que contiene todos los valores pasados
    for nombre, edad in nombresYEdades.items():
        print(f"Hola, {nombre}. Tienes {edad} años.")


# Llamamos a la función saludarGenteConEdad y le pasamos varios valores con nombre como parámetros
saludarGenteConEdad(Juan=30, Keiner=25, Pedro=40)
