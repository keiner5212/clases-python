# Definimos una clase Animal que será nuestra superclase
class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def hacer_sonido(self):
        print("El animal hace un sonido")

# Definimos una clase Perro que será nuestra subclase
class Perro(Animal):
    def __init__(self, nombre, edad, raza):
        # Llamamos al método __init__ de la superclase para inicializar los atributos heredados
        super().__init__(nombre, edad)
        # Agregamos un nuevo atributo a la subclase
        self.raza = raza

    # Sobrescribimos el método hacer_sonido de la superclase
    def hacer_sonido(self):
        print("El perro ladra")

# Creamos un objeto de la clase Animal
animal1 = Animal("Firulais", 5)
# Llamamos al método hacer_sonido del objeto animal1
animal1.hacer_sonido()

# Creamos un objeto de la clase Perro
perro1 = Perro("Toby", 3, "Labrador")
# Llamamos al método hacer_sonido del objeto perro1
perro1.hacer_sonido()