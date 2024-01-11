from tkinter import Tk, ttk
import tkinter.font as tkfont

def cargarFuentes(fuente, size, nombre):
    style = ttk.Style()
    style.configure(nombre, font=tkfont.Font(family=fuente, size=size))

def sumar():
    num1 = float(ipt1.get())
    num2 = float(ipt2.get())
    lbl4.config(text=num1+num2)

def restar():
    num1 = float(ipt1.get())
    num2 = float(ipt2.get())
    lbl4.config(text=num1-num2)

def multiplicar():
    num1 = float(ipt1.get())
    num2 = float(ipt2.get())
    lbl4.config(text=num1*num2)

def dividir():
    num1 = float(ipt1.get())
    num2 = float(ipt2.get())
    lbl4.config(text=num1/num2)

root = Tk(screenName="principal")
root.geometry("600x400")
root.title("calculadora")

style = ttk.Style()
ruta = "../recursos/Tektur/static/Tektur-Black.ttf"
cargarFuentes(ruta, 18, "NuevaFuente.TLabel")

lbl1 = ttk.Label(root, text="numero 1: ", style="NuevaFuente.TLabel")
lbl1.place(x=10, y=10, height=30)

ipt1 = ttk.Entry(root)
ipt1.place(x=160, y=10, height=30, width=200)

lbl2 = ttk.Label(root, text="numero 2: ", style="NuevaFuente.TLabel")
lbl2.place(x=10, y=50, height=30, width=200)

ipt2 = ttk.Entry(root)
ipt2.place(x=160, y=50, height=30, width=200)

lbl3 = ttk.Label(root, text="Resultado: ", style="NuevaFuente.TLabel")
lbl3.place(x=10, y=90, height=30, width=200)

lbl4 = ttk.Label(root, text="", style="NuevaFuente.TLabel")
lbl4.place(x=160, y=90, height=30, width=200)

btn1 = ttk.Button(root, text="sumar", command=sumar)
btn1.place(x=10, y=120, height=30, width=150,anchor="nw")

btn1 = ttk.Button(root, text="restar", command=restar)
btn1.place(x=170, y=120, height=30, width=150,anchor="nw")

btn1 = ttk.Button(root, text="multiplicar", command=multiplicar)
btn1.place(x=10, y=160, height=30, width=150,anchor="nw")

btn1 = ttk.Button(root, text="dividir", command=dividir)
btn1.place(x=170, y=160, height=30, width=150,anchor="nw")

root.mainloop()
