import easygui as eg

# Muestra un cuadro de texto con texto predefinido.
respuesta = eg.textbox(msg="Escribe algo",text="Texto predefinido")
print(respuesta)

# Muestra un cuadro de código con código predefinido.
respuesta = eg.codebox(msg="Código",text="print('xd')")
print(respuesta)
