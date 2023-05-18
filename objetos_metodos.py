from typing import Any


class Pokemon:
    def __init__(self, nombre, tipo, edad):
        self.nombreDelPokemon = nombre
        self.tipoDelPokemon = tipo
        self.edadDelPokemon = edad

    # funcion que define el como se va a mostrar un objeto
    # si no se pone esta funcion, cuando intentemos imprimir al objeto entero, se va a
    # imprimir la direccion de memoria del objeto (lo que no nos sirve de mucho)
    def __str__(self):
        return "pokemon: "+self.nombreDelPokemon+" edad: " + str(self.edadDelPokemon)

    # este metodo define como tenemos que sumar 2 objetos de la misma clase, devolviendo, otro
    # objeto de esa clase (valga la redundancia)
    def __add__(self, otroPokemon):
        nuevoNombre = self.nombreDelPokemon + " y " + otroPokemon.nombreDelPokemon
        nuevotipo = self.tipoDelPokemon + " y "+otroPokemon.tipoDelPokemon
        nuevoedad = self.edadDelPokemon+otroPokemon.edadDelPokemon
        return Pokemon(nuevoNombre, nuevotipo, nuevoedad)

    # este metodo define como debe comparar 2 objetos de la clase para saber si
    # son iguales o no
    def __eq__(self, otroPokemon):
        if self.nombreDelPokemon == otroPokemon.nombreDelPokemon:
            if self.tipoDelPokemon == otroPokemon.tipoDelPokemon:
                if self.edadDelPokemon == otroPokemon.edadDelPokemon:
                    return True
        return False
    
    # este metodo es para decirle a python como saber si un objeto de la clase es less than (menor que)
    # otro objeto de la clase
    def __lt__(self,otroPokemon):
        return self.edadDelPokemon < otroPokemon.edadDelPokemon
    
    # este metodo es para decirle a python como saber si un objeto de la clase es 
    # less than or equal (menor o igual) a
    # otro objeto de la clase
    def __lte__(self,otroPokemon):
        return self.edadDelPokemon <= otroPokemon.edadDelPokemon

    # este metodo es para decirle a python como saber si un objeto de la clase es 
    # greater than (mayor que)
    # otro objeto de la clase
    def __gt__(self,otroPokemon):
        return self.edadDelPokemon > otroPokemon.edadDelPokemon

    # este metodo es para decirle a python como saber si un objeto de la clase es 
    # greater than or equal (mayor o igual) a
    # otro objeto de la clase
    def __gte__(self,otroPokemon):
        return self.edadDelPokemon >= otroPokemon.edadDelPokemon

    # este metodo le dice a nuestro programa cono saber la longitud de un objeto de la clase
    def __len__(self):
        return 3
    
    # este metodo le dice a nuestro programa que es lo que tiene que hacer couando se intente llamar 
    # un objeto de esta clase como si fuera una funcion
    def __call__(self,*args):
        print("no puedes llamar a un objeto de la clase Pokemon como si fuera una funcion")

    # este metodo le dice a nuestro programa que es lo que tiene que hacer couando se intente llamar 
    # una posicion del objeto de esta clase como si fuera una coleccion (ej: lista)
    def __getitem__(self,index):
        print("no puedes acceder a posiciones de un objeto de la clase Pokemon como si fuera una coleccion")

    # este metodo le dice a nuestro programa que es lo que tiene que hacer couando se intente asignar 
    # un valor en una posicion del objeto de esta clase como si fuera una coleccion (ej: lista)
    def __setitem__(self,index,x):
        print("no puedes asignar valores a posiciones de un objeto de la clase Pokemon como si fuera una coleccion")







pokemon1 = Pokemon("pikachu", "rayo", 11)

pokemon1()

pokemon1[0]

pokemon1[0]=50

pokemon2 = Pokemon("pikachu", "rayo", 10)

print(len(pokemon1))

if pokemon1 == pokemon2:
    print("son iguales")
else:
    print("no son iguales")

if pokemon1 > pokemon2:
    print("pokemon1 es mayor")
else:
    print("pokemon2 es mayor")

if pokemon1 < pokemon2:
    print("pokemon1 es menor")
else:
    print("pokemon2 es menor")

# setattr(object, name, value) modifica el valor de una variable del objeto
setattr(pokemon1,"a","xd")
# delattr(object, attribute) elimina el atributo del objeto
delattr(pokemon1,"a")
# hasattr(object, attribute) pregunta si el objeto tiene un atributo
print(hasattr(pokemon1,"a"))

print(pokemon1)
