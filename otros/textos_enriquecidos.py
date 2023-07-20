nombreDelPokemon = "pikachu"
edadDelPokemon = 10

# Texto plano
print("Hola, esto es un texto plano")

# Texto enriquecido con concatenación de variables
# La concatenación de variables se logra utilizando el operador + para unir cadenas
print("El Pokémon " + nombreDelPokemon + " tiene " + str(edadDelPokemon) + " años")

# Texto enriquecido con f-strings (formateo de cadenas)
# Las f-strings son una forma concisa y conveniente de incrustar expresiones dentro de cadenas literales
print(f"El Pokémon {nombreDelPokemon} tiene {edadDelPokemon} años")

# Texto enriquecido con el método format()
# El método format() permite formatear cadenas utilizando marcadores de posición {}
print("El Pokémon {} tiene {} años".format(nombreDelPokemon, edadDelPokemon))

# También puedes utilizar índices numéricos para especificar el orden de los argumentos en el método format()
print("El Pokémon {1} tiene {0} años".format(edadDelPokemon, nombreDelPokemon))

# O puedes utilizar nombres de argumentos para hacer que el código sea más legible
print("El Pokémon {nombre} tiene {edad} años".format(nombre=nombreDelPokemon, edad=edadDelPokemon))