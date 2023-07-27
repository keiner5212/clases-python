import easygui as eg

# Muestra un cuadro de mensaje con un mensaje y un título.
respuesta = eg.msgbox(msg="Hola, este es un mensaje rápido", title="Mensaje 1",
                      ok_button="De acuerdo", image="./sandia.png")
print(respuesta)

# Muestra un cuadro de diálogo Continuar/Cancelar.
respuesta = eg.ccbox(msg="¿Deseas continuar?", title="Continuar/Cancelar")
print(respuesta)

# Muestra un cuadro de diálogo Sí/No.
respuesta = eg.ynbox(msg="¿Estás seguro?", title="Sí/No")
print(respuesta)

# Muestra un cuadro de diálogo con opciones personalizadas.
respuesta = eg.boolbox(msg="¿Debo continuar?",
                       choices=("Sí", "No"), title="Boolbox 1")
print(respuesta)

opciones = ("Sí", "No", "Tal vez")
# Muestra un cuadro de diálogo con una lista de opciones para elegir.
respuesta = eg.choicebox(msg="¿Fumas?", choices=opciones, preselect=3)
print(respuesta)
