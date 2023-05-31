
class Banco:
    def __init__(self,nombre):
        self.__afiliados=[]
        self.__nombreBanco=nombre

    def agregarAfiliado(self,nuevoAfiliado):
        self.__afiliados.append(nuevoAfiliado)

    def getAfiliados(self):
        res=""
        for afiliado in self.__afiliados:
            res+=afiliado+", "
        return res

    def getNombre(self):
        return self.__nombreBanco
    
    def setNombre(self,nuevoNombre):
        self.__nombreBanco=nuevoNombre


paypal=Banco("paypal")

paypal.agregarAfiliado("keiner")
paypal.agregarAfiliado("keiner")
paypal.agregarAfiliado("keiner")
paypal.agregarAfiliado("keiner")
paypal.agregarAfiliado("keiner")

print(paypal.getAfiliados())
