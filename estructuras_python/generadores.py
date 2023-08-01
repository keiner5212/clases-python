# Definimos una función generadora llamada numerosPares que recibe un número entero como parámetro
def numerosPares(n):
    # Dentro de la función, utilizamos un bucle for para generar números pares
    for i in range(n):
        if i % 2 == 0:
            # Utilizamos la palabra clave yield para devolver el valor generado
            yield i


# Llamamos a la función generadora numerosPares y le pasamos un valor como parámetro
generador = numerosPares(10)

# Utilizamos un bucle for para iterar sobre los valores generados por el generador
for numero in generador:
    print(numero)


# También podemos utilizar la palabra clave yield from para delegar parte de la generación de valores a otra función generadora
def numerosImpares(n):
    # Dentro de la función, utilizamos un bucle for para generar números impares
    for i in range(n):
        if i % 2 != 0:
            # Utilizamos la palabra clave yield para devolver el valor generado
            yield i


def numeros(n):
    # Dentro de la función, utilizamos yield from para delegar la generación de números pares a la función numerosPares
    yield from numerosPares(n)
    # También utilizamos yield from para delegar la generación de números impares a la función numerosImpares
    yield from numerosImpares(n)


# Llamamos a la función generadora numeros y le pasamos un valor como parámetro
generador = numeros(10)

# Utilizamos un bucle for para iterar sobre los valores generados por el generador
for numero in generador:
    print(numero)
