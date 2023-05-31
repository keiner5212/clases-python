# crear un clase que funcione como un menu, que le puedas ingresar opciones
# y tambien las funcionalidades

class Menu:
    def __init__(self):
        self.opciones = []

    def agregarOpcion(self, texto, funcion):
        self.opciones.append({"texto": texto, "funcion": funcion})

    def show(self):
        print("Menu")
        cont = 1
        for opcion in self.opciones:
            print(cont, "-", opcion["texto"]+".")
            cont += 1
        print(cont, "-","sair.")
        op = int(input("Ingresa tu opcion: "))
        if op==cont:
            return False
        self.opciones[op-1]["funcion"]()

def hola():
    print("Hola")

def adios():
    print("adios")

x = Menu()

x.agregarOpcion("saludar", hola)
x.agregarOpcion("adios", adios)

while True:
    res=x.show()
    if(res==False):
        break
