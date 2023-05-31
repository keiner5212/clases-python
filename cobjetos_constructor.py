class Persona:
    def __init__(self, nombre, edad):
        # El método __init__ recibe self como primer parámetro, seguido de los parámetros del constructor
        # Dentro del método __init__, podemos utilizar los parámetros para inicializar los atributos del objeto
        self.nombre = nombre
        self.edad = edad

    def presentarse(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")

# Creamos un objeto de la clase Persona utilizando el constructor
persona1 = Persona("Juan", 30)
# Llamamos al método presentarse del objeto persona1
persona1.presentarse()
