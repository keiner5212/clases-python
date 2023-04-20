# crea un programa que permita añadir, editar, borrar un registro de personas en las que
# cada persona tiene nombre, apellido, numero, y correo, debe implementarse con:
# - funciones, listas, diccionarios

def pedirDatosContacto():
    contacto = {}
    contacto["nombre"] = input("Dijita el nombre del nuevo contacto: ")
    contacto["apellido"] = input("Dijita el apellido del nuevo contacto: ")
    contacto["numero"] = input("Dijita el telefono del nuevo contacto: ")
    return contacto


def editarContacto(basededatos):
    pos = int(input("Dijita la posicion del contacto que quieres editar: "))
    if (pos >= 0 and pos < len(basededatos)):
        edicion = int(input(
            "Que es lo que vas a editar\n1. nombre\n2. apellido\n3. numero\n4. cancelar\nTu eleccion: "))
        if (edicion == 1):
            basededatos[pos]["nombre"] = input(
                "Dijita el nuevo nombre del contacto: ")
        elif (edicion == 2):
            basededatos[pos]["apellido"] = input(
                "Dijita el nuevo apellido del contacto: ")
        elif (edicion == 3):
            basededatos[pos]["numero"] = input(
                "Dijita el nuevo telefono del contacto: ")
        else:
            print("Ingresa una posicion entre 0 y", (len(basededatos)-1))


def eliminarContacto(basededatos):
    pos = int(input("Dijita la posicion del contacto que quieres borrar: "))
    if (pos >= 0 and pos < len(basededatos)):
        basededatos.remove(basededatos[pos])
    else:
        print("Ingresa una posicion entre 0 y", (len(basededatos)-1))


def menu(basededatos):
    opcion = int(input(
        "MENU\n1. añadir contacto\n2. editar contacto\n3. borrar contacto\n4. mostrar contactos\n5. salir\nTu eleccion: "))
    if (opcion == 1):
        basededatos.append(pedirDatosContacto())
    elif (opcion == 2):
        editarContacto(basededatos)
    elif (opcion == 3):
        eliminarContacto(basededatos)
    elif (opcion == 4):
        print(basededatos)
    elif (opcion == 5):
        return False
    return True


basededatos = []

while True:
    res=menu(basededatos)
    if (res==False):
        break
