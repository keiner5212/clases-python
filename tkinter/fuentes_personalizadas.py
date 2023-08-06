from tkinter import Tk, ttk, font

# Crear una instancia de la ventana principal de Tkinter
root = Tk()
root.configure(background="gray")

# Configurar estilos de los widgets usando ttk.Style
styles = ttk.Style()
mi_fuente = font.Font(family="Tektur Black", size=12)
styles.configure("NuevaFuente.TLabel", font=mi_fuente,
                 foregroundcolor="#050529")

# Configurar título y dimensiones de la ventana principal
root.title("posicionamientos")
root.geometry("600x400")

# Crear y configurar una etiqueta (label) usando el estilo "NuevaFuente.TLabel"
lbl1 = ttk.Label(root, text="ejemplo", style="NuevaFuente.TLabel")
# Empaquetar la etiqueta en la ventana con espacio en el eje Y
lbl1.pack(pady=50)

# Iniciar el ciclo de eventos de la aplicación Tkinter
root.mainloop()
