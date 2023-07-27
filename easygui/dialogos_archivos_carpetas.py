import easygui as eg

# Muestra un cuadro de diálogo para seleccionar una carpeta.
respuesta = eg.diropenbox(msg="Selecciona una carpeta", default="/")
print(respuesta)

# Muestra un cuadro de diálogo para seleccionar uno o varios archivos.
respuesta = eg.fileopenbox(msg="Selecciona un archivo", default="*.txt", filetypes=["*.txt", "*.csv"])
print(respuesta)

# Muestra un cuadro de diálogo para guardar un archivo.
respuesta = eg.filesavebox(msg="Guardar", default="./archivo.txt", filetypes=["*.txt"])
print(respuesta)
