import easygui as eg

# Muestra un cuadro de mensaje con un mensaje y un título.
respuesta = eg.msgbox(msg="Hola, este es un mensaje rápido", title="Mensaje 1",
                      ok_button="De acuerdo", image="./sandia.png")
print(respuesta)

# Muestra un cuadro de diálogo Continuar/Cancelar.
respuesta = eg.ccbox()
print(respuesta)

# Muestra un cuadro de diálogo Sí/No.
respuesta = eg.ynbox(msg="¿Estás seguro?")
print(respuesta)

# Muestra un cuadro de diálogo con opciones personalizadas.
respuesta = eg.boolbox(msg="¿Debo continuar?",
                       choices=("Sí", "No"), title="Boolbox 1")
print(respuesta)

opciones = ("Sí", "No", "Tal vez")
# Muestra un cuadro de diálogo con una lista de opciones para elegir.
respuesta = eg.choicebox(msg="¿Fumas?", choices=opciones, preselect=3)
print(respuesta)

# Muestra un cuadro de diálogo para ingresar información.
respuesta = eg.enterbox(msg="Ingresa tu nombre:", default="", strip=True)
print(respuesta)

# Muestra un cuadro de diálogo para seleccionar múltiples opciones.
respuesta = eg.multchoicebox(msg="Elige varias opciones", choices=opciones)
print(respuesta)

# Muestra un cuadro de diálogo para ingresar información numérica.
respuesta = eg.integerbox(msg="Ingresa un numero")
print(respuesta)

# Muestra un cuadro de diálogo para ingresar múltiples campos de información.
respuesta = eg.multenterbox(msg="Rellena los campos", fields=["Nombre", "Edad"])
print(respuesta)

# Muestra un cuadro de diálogo para ingresar información confidencial.
respuesta = eg.passwordbox(msg="Escribe tu contraseña", image="./sandia.png")
print(respuesta)

# Muestra un cuadro de texto con texto predefinido.
respuesta = eg.textbox(msg="Escribe algo",text="Texto predefinido")
print(respuesta)

# Muestra un cuadro de código con código predefinido.
respuesta = eg.codebox(msg="Código",text="print('xd')")
print(respuesta)

# Muestra un cuadro de diálogo para seleccionar una carpeta.
respuesta = eg.diropenbox(msg="Selecciona una carpeta")
print(respuesta)

# Muestra un cuadro de diálogo para seleccionar uno o varios archivos.
respuesta = eg.fileopenbox(msg="Selecciona un archivo")
print(respuesta)

# Muestra un cuadro de diálogo para guardar un archivo.
respuesta = eg.filesavebox(msg="Guardar")
print(respuesta)

# Muestra un cuadro de excepción con información sobre una excepción.
try:
    x = 1 / 0
except Exception as e:
    respuesta = eg.exceptionbox(msg=e)
    print(respuesta)
