import easygui as eg

# Muestra un cuadro de excepción con información sobre una excepción.
try:
    x = 1 / 0
except Exception as e:
    respuesta = eg.exceptionbox(msg=e)
    print(respuesta)
