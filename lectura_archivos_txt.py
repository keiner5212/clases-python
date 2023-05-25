
archivo = open("./ejemplo.txt", "r+")

contenido = archivo.read().replace("\n", " ").strip(" ")
contenidoSeparado = contenido.split(" ")
print(contenidoSeparado[1], contenidoSeparado[3])

archivo.close()


with open("./ejemplo.txt", "r+") as archivo:
    contenido = archivo.read().replace("\n", " ").strip(" ")
    contenidoSeparado = contenido.split(" ")
    print(contenidoSeparado[1], contenidoSeparado[3])


#modos individuales

# r (reading) modo de lectura (no podemos añadir nada al archivo) 
# (si el archivo no existe va a dar un error)

# w (writing) modo de escritura (no podemos leer la informacion) 
# (si el archivo existe lo reemplaza, y si no existe lo crea)

# a (append) modo de anexado (añade texto al final de un archivo de texto)
# (si el archivo no existe lo crea y si existe no lo reemplaza)
# no puede usar los metodos del modo r

# x (creacion exclusiva) modo de escritura (no podemos leer la informacion) 
# (si el archivo existe no lo reemplaza, y si no existe lo crea)


#modos combinados
# r+ permite lectura y escritura en un archivo pero este ya debe existir 
# (la escritura funciona como el modo a) es como combinar el modo r y el a

#modo r
# read() devuelve todo el texto del archivo como un unico str
# readline() devuelve una linea de el archivo
# readlines() devuelve una lista en la que cada elemento es una linea

#modo w
# write()
