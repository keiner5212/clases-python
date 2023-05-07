class Persona:
    def __init__(self,nombre,edad) -> None:
        self.nombre=nombre
        self.edad=edad

    def imprimirPersona(self):
        return (self.nombre+"\n"+str(self.edad))




class Doctor(Persona):
    def __init__(self,nombre,edad,area) -> None:
        self.nombre=nombre
        self.edad=edad
        self.area=area

    def realizarCirugia(self):
        print(self.nombre+" solo los doctores pondemos realizar cirugias")




class Ingeniero(Persona):
    def __init__(self,nombre,edad,especializacion) -> None:
        self.nombre=nombre
        self.edad=edad
        self.especializacion=especializacion

    def mejoreSistemaOrganizacion(self):
        print(self.nombre+" solo los ingenieros pueden mejorar los sistemas de una organizacion")

listaPersonaClase=[
    Persona("keiner",20),
    Doctor("juan",21,"cirujano"),
    Ingeniero("carlos",45,"sistemas")
]



for objeto in listaPersonaClase:
    if(type(objeto)==Persona):
        print(objeto.imprimirPersona())

    elif(type(objeto)==Doctor):
        print(objeto.imprimirPersona())
        objeto.realizarCirugia()

    elif(type(objeto)==Ingeniero):
        print(objeto.imprimirPersona())
        objeto.mejoreSistemaOrganizacion()


