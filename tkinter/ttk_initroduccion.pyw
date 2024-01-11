import tkinter as tk
from tkinter import ttk

root = tk.Tk()

style = ttk.Style()

# default clam alt classic
style.theme_use("default")

style.configure("TButton", padding=5, background="#716ff1",
                foreground="#050529", font=["Forte", 20],
                bordercolor="#0000"
                )

style.map("TButton", background=[("active", "#2c30a0")])

root.resizable(width=True, height=False)
root.geometry("600x400")

labeltk = tk.Label(root, text="esto no esta estilizado")
labeltk.pack()

botontk = tk.Button(root, text="este boton es de tk")
botontk.pack()


labelttk = ttk.Label(root, text="esto si esta estilizado")
labelttk.pack()

botonttk = ttk.Button(root, text="este boton es de ttk")
botonttk.pack()


root.mainloop()
