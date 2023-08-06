from tkinter import Tk, Label, ttk

root = Tk()


styles = ttk.Style()
styles.configure("Redondo.TButton", borderradius=15)
styles.configure("Redondo.TLabel", borderradius=15,
                 foreground="#050529", background="#f7b1b1")


root.title("posicionamientos")
root.geometry("600x400")

# lbl1 = Label(root, text="ejemplo", fg="#050529", bg="#f7b1b1")
# lbl1.pack(side="top",fill="x",expand=True)
# lbl1 = Label(root, text="ejemplo", fg="#050529", bg="#f7b1b1")
# lbl1.pack(side="top",padx=20,pady=20,ipadx=20,ipady=10)

lbl1 = ttk.Label(root, text="ejemplo", style="Redondo.TLabel")
lbl1.place(x=200,y=200,height=50,width=200,anchor="center")

# lbl1 = ttk.Label(root, text="ejemplo", style="Redondo.TLabel")
# lbl1.grid(row=0,column=0)

# lbl1 = ttk.Button(root, text="boton ejemplo", style="Redondo.TButton")
# lbl1.pack(side="top")


root.mainloop()
