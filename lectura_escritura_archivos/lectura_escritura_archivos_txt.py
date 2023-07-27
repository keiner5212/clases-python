# Abre un archivo en modo lectura y escritura (r+)
archivo = open("./recursos/ejemplo.txt", "r+")

# Lee el contenido del archivo y reemplaza los saltos de línea por espacios
contenido = archivo.read().replace("\n", " ").strip(" ")
# Divide el contenido en una lista de palabras
contenidoSeparado = contenido.split(" ")
# Imprime la segunda y cuarta palabra del contenido
print(contenidoSeparado[1], contenidoSeparado[3])

# Cierra el archivo
archivo.close()

# Abre un archivo en modo lectura y escritura (r+) utilizando la sintaxis with
with open("./recursos/ejemplo.txt", "r+") as archivo:
    # Lee el contenido del archivo y reemplaza los saltos de línea por espacios
    contenido = archivo.read().replace("\n", " ").strip(" ")
    # Divide el contenido en una lista de palabras
    contenidoSeparado = contenido.split(" ")
    # Imprime la segunda y cuarta palabra del contenido
    print(contenidoSeparado[1], contenidoSeparado[3])

# Los modos disponibles para abrir un archivo son:
# r: modo de lectura. No se puede escribir en el archivo. Si el archivo no existe, se produce un error.
# w: modo de escritura. No se puede leer el archivo. Si el archivo existe, se sobrescribe. Si no existe, se crea.
# a: modo de anexado. Permite añadir texto al final de un archivo. Si el archivo no existe, se crea.
# x: modo de creación exclusiva. Permite crear un nuevo archivo. Si el archivo ya existe, se produce un error.
# r+: modo de lectura y escritura. Permite leer y escribir en un archivo existente.

# En modo de lectura (r), se pueden utilizar los siguientes métodos:
# read(): devuelve todo el contenido del archivo como una cadena.
# readline(): devuelve una línea del archivo.
# readlines(): devuelve una lista donde cada elemento es una línea del archivo.

# En modo de escritura (w), se puede utilizar el método write() para escribir en el archivo.
