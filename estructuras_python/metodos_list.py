# 1. append() - Agrega un elemento al final de la lista.
mi_lista = [1, 2, 3]
mi_lista.append(4)
print(mi_lista)  # [1, 2, 3, 4]

# 2. clear() - Elimina todos los elementos de la lista.
mi_lista = [1, 2, 3]
mi_lista.clear()
print(mi_lista)  # []

# 3. copy() - Devuelve una copia de la lista.
mi_lista = [1, 2, 3]
copia_lista = mi_lista.copy()
print(copia_lista)  # [1, 2, 3]

# 4. count() - Devuelve el número de veces que aparece un elemento en la lista.
mi_lista = [1, 2, 2, 3]
conteo = mi_lista.count(2)
print(conteo)  # 2

# 5. extend() - Agrega los elementos de una lista (o cualquier iterable) al final de la lista actual.
mi_lista = [1, 2, 3]
otra_lista = [4, 5]
mi_lista.extend(otra_lista)
print(mi_lista)  # [1, 2, 3, 4, 5]

# 6. index() - Devuelve el índice del primer elemento en la lista que coincide con el valor especificado.
mi_lista = [1, 2, 3]
indice = mi_lista.index(2)
print(indice)  # 1

# 7. insert() - Agrega un elemento en la posición especificada de la lista.
mi_lista = [1, 2, 3]
mi_lista.insert(1, "nuevo")
print(mi_lista)  # [1, 'nuevo', 2, 3]

# 8. pop() - Elimina y devuelve el último elemento de la lista.
mi_lista = [1, 2, 3]
ultimo_elemento = mi_lista.pop()
print(ultimo_elemento)  # 3
print(mi_lista)  # [1, 2]

# 9. remove() - Elimina el primer elemento de la lista que coincide con el valor especificado.
mi_lista = [1, "nuevo", "nuevo", "otro"]
mi_lista.remove("nuevo")
print(mi_lista)  # [1, 'nuevo', 'otro']

# 10. reverse() - Invierte el orden de los elementos en la lista.
mi_lista = [1, "nuevo", "otro"]
mi_lista.reverse()
print(mi_lista)  # ['otro', 'nuevo', 1]

# 11. sort() - Ordena los elementos de la lista en orden ascendente.
mi_lista = ["3", "1", "otro", "nuevo"]
mi_lista.sort()
print(mi_lista)  # ['1', '3', 'nuevo', 'otro']

# 12. copy() - Devuelve una copia superficial (shallow copy) de la lista.
mi_lista = [[1], [2], [3]]
copia_superficial = mi_lista.copy()
copia_superficial[0][0] = "nuevo"
print(copia_superficial)  # [['nuevo'], [2], [3]]
print(mi_lista)  # [['nuevo'], [2], [3]]

# 13. count() - Devuelve el número de veces que aparece un elemento en la lista.
mi_lista = ["a", "b", "c", "a"]
conteo_a = mi_lista.count("a")
conteo_d = mi_lista.count("d")
print(conteo_a)  # 2
print(conteo_d)  # 0

# 14. index() - Devuelve el índice del primer elemento en la lista que coincide con el valor especificado.
mi_lista = ["a", "b", "c", "a"]
indice_a = mi_lista.index("a")
# indice_d = mi_lista.index("d")  Genera ValueError
print(indice_a)  # 0

# 15. pop() - Elimina y devuelve el elemento en la posición especificada de la lista.
mi_lista = ["a", "b", "c"]
elemento_eliminado = mi_lista.pop(1)
print(elemento_eliminado)  # b
print(mi_lista)  # ['a', 'c']

# 16. remove() - Elimina el primer elemento en la lista que coincide con el valor especificado.
mi_lista = ["a", "b", "c"]
mi_lista.remove("b")
print(mi_lista)  # ['a', 'c']

# 17. reverse() - Invierte el orden de los elementos en la lista.
mi_lista = ["a", "b", "c"]
mi_lista.reverse()
print(mi_lista)  # ['c', 'b', 'a']

# 18. sort() - Ordena los elementos de la lista en orden ascendente.
mi_lista = [3, 1, 4, 1, 5, 9, 2]
mi_lista.sort()
print(mi_lista)  # [1, 1, 2, 3, 4, 5, 9]

# 19. sort() - Ordena los elementos de la lista en orden descendente.
mi_lista = [3, 1, 4, 1, 5, 9, 2]
mi_lista.sort(reverse=True)
print(mi_lista)  # [9, 5, 4, 3, 2, 1, 1]

# 20. sort() - Ordena los elementos de la lista utilizando una función personalizada.
mi_lista = ["hola", "adios", "buenos dias"]
mi_lista.sort(key=len)
print(mi_lista)  # ['hola', 'adios', 'buenos dias']

# Creamos una lista de diccionarios
lista_diccionarios = [
    {"nombre": "Juan", "edad": 25},
    {"nombre": "María", "edad": 30},
    {"nombre": "Pedro", "edad": 20}
]

# Ordenamos la lista de diccionarios por edad
lista_ordenada = sorted(lista_diccionarios, key=lambda x: x["edad"])

# Imprimimos la lista ordenada
print(lista_ordenada)
