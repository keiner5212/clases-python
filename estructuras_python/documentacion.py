# Para agregar documentación a tus clases y funciones en Python, puedes usar docstrings. 
# Un docstring es una cadena de caracteres que aparece como el primer elemento lógico en una definición de función o clase. 
# El propósito de un docstring es proporcionar una documentación legible por humanos para la función o clase.

# Aquí hay un ejemplo de cómo agregar un docstring a una función en Python:
def suma(a, b):
    """
    Esta función toma dos números como argumentos y devuelve su suma.
    """
    return a + b

# Aquí hay otro ejemplo de cómo agregar un docstring a una clase en Python:


class Persona:
    """
    Esta clase representa a una persona con un nombre y una edad.
    """

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        """
        Esta función imprime un saludo personalizado para la persona.
        """
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")


# También puedes agregar docstrings a tus variables en Python. Por ejemplo:
mi_variable = 42
"""
Esta variable representa la respuesta a la pregunta última sobre la vida, el universo y todo lo demás.
"""
