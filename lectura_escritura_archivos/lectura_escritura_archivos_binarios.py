
# Los modos disponibles para abrir un archivo son:
# rb: modo de lectura. No se puede escribir en el archivo. Si el archivo no existe, se produce un error.
# wb: modo de escritura. No se puede leer el archivo. Si el archivo existe, se sobrescribe. Si no existe, se crea.
# ab: modo de anexado. Permite añadir texto al final de un archivo. Si el archivo no existe, se crea.
# xb: modo de creación exclusiva. Permite crear un nuevo archivo. Si el archivo ya existe, se produce un error.
# rb+: modo de lectura y escritura. Permite leer y escribir en un archivo existente.

#escritura
archivo = open("./recursos/ejemplo.dat", "wb")
contenido = b"hola, esto va a ir en el archivo"
archivo.write(contenido)
archivo.close()

#lectura
archivo = open("./recursos/ejemplo.dat", "rb")
contenido = archivo.read()
archivo.close()


