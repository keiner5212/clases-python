import tkinter as tk

def hola():
    # Esta función imprime "Hola" en la consola cuando se llama
    print("Hola")

root = tk.Tk()
root.title("Primer acercamiento")

# Establece el icono de la ventana
root.iconbitmap("./recursos/analizar_128x128_via_10015_io.ico")

# Permite cambiar el tamaño de la ventana solo en ancho, no en alto
root.resizable(width=True, height=False)
# Establece el tamaño inicial de la ventana
root.geometry("700x400")

# Crea una etiqueta con el texto "hola, esto es mi primer label"
etiqueta=tk.Label(root,text="hola, esto es mi primer label")
# Agrega la etiqueta a la ventana
etiqueta.pack()

# Crea un botón con el texto "accion" que llama a la función hola cuando se hace clic en él
boton=tk.Button(root,text="accion",command=hola)
# Agrega el botón a la ventana
boton.pack()

# Crea un campo de entrada de texto
entrada=tk.Entry(root)
# Agrega el campo de entrada a la ventana
entrada.pack()

# Inicia el bucle principal de la interfaz gráfica de usuario
root.mainloop()
