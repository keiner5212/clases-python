import pickle

def obtenerContactos():
    archivo=open("contactos.dat","rb")
    contactos=pickle.load(archivo)
    archivo.close()
    return contactos

def guardarContactos(contactos):
    archivo=open("contactos.dat","wb")
    pickle.dump(contactos,archivo)
    archivo.close()

def pedirDatosContacto():
    contacto = {}
    contacto["nombre"] = input("Dijita el nombre del nuevo contacto: ")
    contacto["apellido"] = input("Dijita el apellido del nuevo contacto: ")
    contacto["numero"] = input("Dijita el telefono del nuevo contacto: ")
    return contacto

def añadirContacto():
    contactos=obtenerContactos()
    contactos.append(pedirDatosContacto())
    guardarContactos(contactos)


def editarContacto():
    contactos=obtenerContactos()
    pos = int(input("Dijita la posicion del contacto que quieres editar: "))
    if (pos >= 0 and pos < len(contactos)):
        edicion = int(input(
            "Que es lo que vas a editar\n1. nombre\n2. apellido\n3. numero\n4. cancelar\nTu eleccion: "))
        if (edicion == 1):
            contactos[pos]["nombre"] = input(
                "Dijita el nuevo nombre del contacto: ")
        elif (edicion == 2):
            contactos[pos]["apellido"] = input(
                "Dijita el nuevo apellido del contacto: ")
        elif (edicion == 3):
            contactos[pos]["numero"] = input(
                "Dijita el nuevo telefono del contacto: ")
        else:
            print("Ingresa una posicion entre 0 y", (len(contactos)-1))
    guardarContactos(contactos)

def eliminarContacto():
    contactos=obtenerContactos()
    pos = int(input("Dijita la posicion del contacto que quieres borrar: "))
    if (pos >= 0 and pos < len(contactos)):
        contactos.remove(contactos[pos])
    else:
        print("Ingresa una posicion entre 0 y", (len(contactos)-1))
    guardarContactos(contactos)

def menu():
    opcion = int(input(
        "MENU\n1. añadir contacto\n2. editar contacto\n3. borrar contacto\n4. mostrar contactos\n5. salir\nTu eleccion: "))
    if (opcion == 1):
        añadirContacto()
    elif (opcion == 2):
        editarContacto()
    elif (opcion == 3):
        eliminarContacto()
    elif (opcion == 4):
        print(obtenerContactos())
    elif (opcion == 5):
        return False
    return True

while True:
    res = menu()
    if (res == False):
        break
