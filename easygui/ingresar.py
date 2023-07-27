import easygui as eg

# Muestra un cuadro de diálogo para ingresar información.
respuesta = eg.enterbox(msg="Ingresa tu nombre:", default="", strip=True)
print(respuesta)

# Muestra un cuadro de diálogo para seleccionar múltiples opciones.
opciones = ("Sí", "No", "Tal vez")
respuesta = eg.multchoicebox(msg="Elige varias opciones", choices=opciones)
print(respuesta)

# Muestra un cuadro de diálogo para ingresar información numérica.
respuesta = eg.integerbox(msg="Ingresa un numero")
print(respuesta)

# Muestra un cuadro de diálogo para ingresar múltiples campos de información.
respuesta = eg.multenterbox(
    msg="Rellena los campos", fields=["Nombre", "Edad"])
print(respuesta)

# Muestra un cuadro de diálogo para ingresar información confidencial.
respuesta = eg.passwordbox(msg="Escribe tu contraseña", image="./sandia.png")
print(respuesta)
