import tkinter as tk


def grid_example():
    root = tk.Tk()
    root.title("Posicionamiento usando grid")
    root.geometry("400x200")

    lbl = tk.Label(root, text="Posicionamiento Grid", font=("Helvetica", 14))

    # Atributos de grid:
    # row, column: fila y columna donde se coloca el widget
    # rowspan, columnspan: cantidad de filas y columnas que el widget abarcará
    # grid_info: obtiene información sobre la posición de un widget en la cuadrícula
    # columnconfigure, rowconfigure: configura propiedades de las filas y columnas en la cuadrícula
    lbl = tk.Label(root, text="Posicionamiento Grid", font=("Helvetica", 14))

    # Usando el método grid
    lbl.grid(row=1, column=1, padx=20, pady=20)

    # Ejemplo: Agregar más widgets con diferentes configuraciones
    btn1 = tk.Button(root, text="Botón 1")
    btn1.grid(row=0, column=0, padx=10, pady=10, sticky="w")

    btn2 = tk.Button(root, text="Botón 2")
    btn2.grid(row=0, column=2, padx=10, pady=10, sticky="e")

    # Configuración de filas y columnas
    root.columnconfigure(0, weight=1)
    root.columnconfigure(2, weight=1)
    root.rowconfigure(0, weight=1)
    root.mainloop()


if __name__ == "__main__":
    grid_example()
