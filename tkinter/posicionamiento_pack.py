import tkinter as tk


def pack_example():
    root = tk.Tk()
    root.title("Posicionamiento usando pack")
    root.geometry("400x200")

    lbl = tk.Label(root, text="Posicionamiento Pack", font=(
        "Helvetica", 14), fg="#050529", bg="#f7b1b1")

    # Atributos de pack:
    # side: lado donde se agregará el widget (top, bottom, left, right)
    # fill: cómo se expande el widget para llenar el espacio asignado (none, x, y, both)
    # expand: True para expandir el widget si el contenedor se agranda
    # anchor: alineación del widget dentro del espacio asignado (n, ne, e, se, s, sw, w, nw, center)
    # padx, pady: espacio adicional en x e y alrededor del widget
    lbl = tk.Label(root, text="Posicionamiento Pack", font=(
        "Helvetica", 14), fg="#050529", bg="#f7b1b1")

    # Usando el método pack
    lbl.pack(side="top", fill="both", expand=True,
             anchor="center", padx=10, pady=10)

    # Ejemplo: Agregar más widgets con diferentes configuraciones
    btn1 = tk.Button(root, text="Botón 1")
    btn1.pack(side="left", fill="y",expand=True, padx=20, pady=10)

    btn2 = tk.Button(root, text="Botón 2")
    btn2.pack(side="top", fill="x", padx=20, pady=10)

    root.mainloop()


if __name__ == "__main__":
    pack_example()
