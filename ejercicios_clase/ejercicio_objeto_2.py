
class Automovil:
    def __init__(self,marca,color,kmRecorridos):
        self.marca=marca
        self.__color=color  #atributo privado (encapsulamiento) no se podra acceder desde fuera
        self.kmRecorridos=kmRecorridos
    
    def __decirMarca(self): #metodo privado
        print(self.marca)
    
    def diHola(self):
        self.__decirMarca()

    def decirColor(self):
        return(self.__color)

class AutomovilDeportivo(Automovil): #herencia
    def __init__(self,marca,color,kmRecorridos,vMax):
        super().__init__(marca,color,kmRecorridos) #superposion de constructores
        self.vMax=vMax
    


aux=AutomovilDeportivo("marca1","azul",100,260)

print(aux.decirColor())
