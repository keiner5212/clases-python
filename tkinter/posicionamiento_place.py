import tkinter as tk

def place_example():
    root = tk.Tk()
    root.title("Posicionamiento usando place")
    root.geometry("400x200")

    lbl = tk.Label(root, text="Posicionamiento Place", font=("Helvetica", 14))
    
    # Atributos de place:
    # x, y: coordenadas absolutas para la esquina superior izquierda del widget
    # relx, rely: coordenadas relativas al ancho y alto del widget
    # width, height: dimensiones del widget
    # relwidth, relheight: dimensiones relativas al ancho y alto del widget
    # anchor: punto de anclaje dentro del widget para su posición
    lbl = tk.Label(root, text="Posicionamiento Place", font=("Helvetica", 14))
    
    # Usando el método place
    lbl.place(x=200, y=150, anchor="center")
    
    # Ejemplo: Agregar más widgets con diferentes configuraciones
    btn1 = tk.Button(root, text="Botón 1")
    btn1.place(x=100, y=50)
    
    btn2 = tk.Button(root, text="Botón 2")
    btn2.place(x=300, y=50)
    
    root.mainloop()

if __name__ == "__main__":
    place_example()
