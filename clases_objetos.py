class Calculadora:
    creador = "una persona"

    def sumar(self,a, b):
        return a+b

    def restar(self,a, b):
        return a-b

    def dividir(self,a, b):
        return a/b

    def multiplicar(self,a, b):
        return a*b

    def potencia(self,a, b):
        return a**b

    def raiz(self,a, b):
        return a**(1/b)




calc = Calculadora()

print(calc.potencia(5,9))
