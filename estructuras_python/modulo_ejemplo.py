def sayHello():
    """
    Imprime un saludo en la consola.
    """
    print("Hello")


def sumar(*a):
    """
    Suma una lista de números.

    Args:
        *a: Números a sumar.

    Returns:
        int: El resultado de la suma.
    """
    acc = 0
    for element in a:
        acc += element
    return acc


ejemplo = 5  # Ejemplo de variable global