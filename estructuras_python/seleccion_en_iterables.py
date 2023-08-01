# Definición de una lista con diferentes elementos
lista = ["keiner", None, "Karen", "juan", "pedro"]

# Definición de una variable "nombre" con el valor "keiner"
nombre = "keiner"

# Acceso a un elemento específico en el iterable "nombre"
print(nombre[1])  # Imprime el elemento en la posición 1, en este caso el carácter "e"

# Acceso a un subconjunto de elementos en el iterable "nombre"
print(nombre[1:4])  # Imprime los elementos desde la posición 1 hasta la posición 3, en este caso "ein"

# Acceso a un subconjunto de elementos en el iterable "nombre" con un salto
print(nombre[0:6:2])  # Imprime los elementos desde la posición 0 hasta la posición 5 con un salto de 2, en este caso "kie"


# ten en cuenta que puedes usar lo anterior con cualquier iterable, en este caso con listas y con strings