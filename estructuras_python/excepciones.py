# En Python, una excepción es un evento que ocurre durante la ejecución de un programa y que interrumpe el curso normal de las instrucciones del programa. Cuando un código de Python se encuentra con una condición que no puede manejar, genera una excepción. Un objeto en Python que describe un error se llama excepción.

# Puedes usar la estructura try-except para manejar excepciones en Python. Por ejemplo:
try:
    # Intenta hacer algo que podría generar una excepción.
    x = 1 / 0
except ZeroDivisionError:
    # Si se genera una excepción ZeroDivisionError, maneja la excepción aquí.
    print("No puedes dividir entre cero.")

# Puedes usar la estructura try-except-finally para manejar excepciones y realizar acciones de limpieza. Por ejemplo:
try:
    # Intenta hacer algo que podría generar una excepción.
    x = 1 / 0
except ZeroDivisionError:
    # Si se genera una excepción ZeroDivisionError, maneja la excepción aquí.
    print("No puedes dividir entre cero.")
finally:
    # Realiza acciones de limpieza aquí, como cerrar archivos o conexiones de red.
    print("Limpiando...")

# Puedes crear tus propias excepciones personalizadas en Python. Por ejemplo:


class MiExcepcion(Exception):
    pass


try:
    # Intenta hacer algo que podría generar una excepción personalizada.
    raise MiExcepcion("Este es mi mensaje de error.")
except MiExcepcion as e:
    # Si se genera una excepción personalizada, maneja la excepción aquí.
    print(f"Se generó una excepción personalizada: {e}")
