"""
pusando una clase llamada "Fracion" 
y sus metodos de __eq__ y __add__ has 
una calculadora de fracciones funcional
"""


class fracciones:

    def __init__(self, a, b):
        self.a = a
        self.b = b

   # def suma(self):  # como mando dos objetos como parametros
     #   frac= (a*d + c*b)/(b*d)

      #  return frac

    def __add__(self, frac2):
        suma = (self.a*frac2.b + frac2.a*self.b)/(self.b*frac2.b)

        return suma


a = int(input("Escriba el numerador de la primera fraccion"))
b = int(input("Escriba el denominador de la primera fraccion"))
c = int(input("Escriba el numerador de la segunda fraccion"))
d = int(input("Escriba el denominador de la segunda fraccion"))

frac1 = fracciones(a, b)
frac2 = fracciones(c, d)
frac3 = frac1+frac2
print("El resultado de sumar las fracciones es", frac3)
