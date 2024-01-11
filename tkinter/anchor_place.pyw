import tkinter as tk
from tkinter import ttk



root = tk.Tk()
root.resizable(width=True, height=False)
root.geometry("600x400")



labelttk = ttk.Label(root, text="esto si esta estilizado")
labelttk.place(x=100,y=50,anchor="nw")



root.mainloop()