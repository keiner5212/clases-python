matriz = [
    [1, 4, 8, 3],
    [10, 14, 48, 32],
    [3, 6, 0, 8]
]

archivo = open("ejemplo.txt", "w")

contenido = ""
for lista in matriz:
    for elemento in lista:
        contenido += str(elemento)+","
    contenido = contenido.strip(",")
    contenido += "\n"

archivo.write(contenido)

archivo.close()


