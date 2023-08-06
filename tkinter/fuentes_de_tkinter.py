import tkinter as tk
from tkinter import font
import os

def mostrar_fuente_seleccionada():
    fuente_seleccionada = fuente_var.get()
    label.config(font=(fuente_seleccionada, 12))

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Ejemplo de Fuentes con Tkinter")
ventana.geometry("600x400")

# Obtener una lista de las fuentes disponibles en el sistema
fuentes_disponibles = font.families()

# Si has instalado una fuente personalizada, agrégala a la lista
fuente_personalizada = "Tektur Black"
if fuente_personalizada not in fuentes_disponibles:
    fuentes_disponibles = (*fuentes_disponibles, fuente_personalizada)

# Variable para almacenar la fuente seleccionada
fuente_var = tk.StringVar(ventana)
fuente_var.set(fuentes_disponibles[0])  # Establecer una fuente predeterminada

# Crear una etiqueta para mostrar texto con la fuente seleccionada
label = tk.Label(ventana, text="Hola, Mundo!", font=(fuente_var.get(), 12))
label.pack(pady=20)

# Crear una lista desplegable con las fuentes disponibles
opcion_fuente = tk.OptionMenu(ventana, fuente_var, *fuentes_disponibles)
opcion_fuente.pack()

# Botón para aplicar la fuente seleccionada
boton_aplicar = tk.Button(ventana, text="Aplicar Fuente", command=mostrar_fuente_seleccionada)
boton_aplicar.pack()

# Iniciar el bucle de la aplicación
ventana.mainloop()
