from striprtf.striprtf import rtf_to_text

# Ruta del archivo RTF a leer
archivo_rtf = "archivo.rtf"

# Abrir el archivo en modo lectura y utilizar 'with' para asegurarse de que se cierre correctamente
with open(archivo_rtf, "r") as archivo:
    # Leer el contenido del archivo RTF y convertirlo a texto sin formato
    contenido = rtf_to_text(archivo.read())

# Imprimir el contenido obtenido
print(contenido)
