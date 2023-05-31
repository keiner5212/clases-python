class Pokemon:
    def __init__(self, nombre, tipo, edad):
        self.nombreDelPokemon = nombre
        self.tipoDelPokemon = tipo
        self.edadDelPokemon = edad

    # El método __str__ define cómo se debe representar un objeto como una cadena
    # Si no se define este método, al intentar imprimir el objeto se mostrará su dirección de memoria
    def __str__(self):
        return f"pokemon: {self.nombreDelPokemon} edad: {self.edadDelPokemon}"

    # El método __add__ define cómo se deben sumar dos objetos de la misma clase
    # En este caso, al sumar dos objetos Pokemon se devuelve un nuevo objeto Pokemon
    def __add__(self, otroPokemon):
        nuevoNombre = self.nombreDelPokemon + " y " + otroPokemon.nombreDelPokemon
        nuevotipo = self.tipoDelPokemon + " y "+otroPokemon.tipoDelPokemon
        nuevoedad = self.edadDelPokemon+otroPokemon.edadDelPokemon
        return Pokemon(nuevoNombre, nuevotipo, nuevoedad)

    # El método __eq__ define cómo se deben comparar dos objetos de la misma clase para saber si son iguales
    def __eq__(self, otroPokemon):
        if self.nombreDelPokemon == otroPokemon.nombreDelPokemon:
            if self.tipoDelPokemon == otroPokemon.tipoDelPokemon:
                if self.edadDelPokemon == otroPokemon.edadDelPokemon:
                    return True
        return False

    # El método __lt__ define cómo se debe comparar si un objeto es menor que otro objeto de la misma clase
    def __lt__(self, otroPokemon):
        return self.edadDelPokemon < otroPokemon.edadDelPokemon

    # El método __le__ define cómo se debe comparar si un objeto es menor o igual que otro objeto de la misma clase
    def __le__(self, otroPokemon):
        return self.edadDelPokemon <= otroPokemon.edadDelPokemon

    # El método __gt__ define cómo se debe comparar si un objeto es mayor que otro objeto de la misma clase
    def __gt__(self, otroPokemon):
        return self.edadDelPokemon > otroPokemon.edadDelPokemon

    # El método __ge__ define cómo se debe comparar si un objeto es mayor o igual que otro objeto de la misma clase
    def __ge__(self, otroPokemon):
        return self.edadDelPokemon >= otroPokemon.edadDelPokemon

    # El método __len__ define cómo se debe calcular la longitud de un objeto de la clase
    def __len__(self):
        return 3

    # El método __call__ define qué debe suceder cuando se intenta llamar a un objeto de la clase como si fuera una función
    def __call__(self, *args):
        print("No puedes llamar a un objeto de la clase Pokemon como si fuera una función")

    # El método __getitem__ define qué debe suceder cuando se intenta acceder a una posición del objeto como si fuera una colección (ej: lista)
    def __getitem__(self, index):
        print("No puedes acceder a posiciones de un objeto de la clase Pokemon como si fuera una colección")

    # El método __setitem__ define qué debe suceder cuando se intenta asignar un valor en una posición del objeto como si fuera una colección (ej: lista)
    def __setitem__(self, index, x):
        print("No puedes asignar valores a posiciones de un objeto de la clase Pokemon como si fuera una colección")


# Creamos dos objetos de la clase Pokemon
pokemon1 = Pokemon("pikachu", "rayo", 11)
pokemon2 = Pokemon("pikachu", "rayo", 10)

# Intentamos llamar al objeto pokemon1 como si fuera una función
pokemon1()

# Intentamos acceder a una posición del objeto pokemon1 como si fuera una colección
pokemon1[0]

# Intentamos asignar un valor en una posición del objeto pokemon1 como si fuera una colección
pokemon1[0] = 50

# Obtenemos la longitud del objeto pokemon1 utilizando el método __len__
print(len(pokemon1))

# Comparamos si los objetos pokemon1 y pokemon2 son iguales utilizando el método __eq__
if pokemon1 == pokemon2:
    print("son iguales")
else:
    print("no son iguales")

# Comparamos si el objeto pokemon1 es mayor que el objeto pokemon2 utilizando el método __gt__
if pokemon1 > pokemon2:
    print("pokemon1 es mayor")
else:
    print("pokemon2 es mayor")

# Comparamos si el objeto pokemon1 es menor que el objeto pokemon2 utilizando el método __lt__
if pokemon1 < pokemon2:
    print("pokemon1 es menor")
else:
    print("pokemon2 es menor")

# Utilizamos la función setattr para modificar el valor de una variable del objeto
setattr(pokemon1, "a", "xd")
# Utilizamos la función delattr para eliminar un atributo del objeto
delattr(pokemon1, "a")
# Utilizamos la función hasattr para preguntar si el objeto tiene un atributo
print(hasattr(pokemon1, "a"))

# Imprimimos la representación en cadena del objeto pokemon1 utilizando el método __str__
print(pokemon1)
