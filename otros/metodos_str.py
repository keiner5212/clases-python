# El método split divide una cadena en una lista de subcadenas utilizando un separador especificado
informacion = "hola, como estas?"
infoSeparada = informacion.split("a")
print(infoSeparada)

# El método rstrip elimina los caracteres especificados del lado derecho de una cadena
informacion = "         \nhola, como estas???????????????"
print([informacion])
infoSinSaltosDeLinea = [informacion.rstrip("?")]
print(infoSinSaltosDeLinea)

# El método lstrip elimina los caracteres especificados del lado izquierdo de una cadena
informacion = "         \nhola, como estas???????????????"
print([informacion])
infoSinSaltosDeLinea = [informacion.lstrip(" ")]
print(infoSinSaltosDeLinea)

# El método strip elimina los caracteres especificados de ambos lados de una cadena
informacion = "         \nhola, como estas                    "
print([informacion])
infoSinSaltosDeLinea = [informacion.strip(" ")]
print(infoSinSaltosDeLinea)

# El método replace reemplaza todas las ocurrencias de una subcadena por otra subcadena en una cadena
informacion = "         \nhola, como estas                    "
print([informacion])
infoSinSaltosDeLinea = [informacion.replace("o", "")]
print(infoSinSaltosDeLinea)

# El método join une una lista de cadenas utilizando un separador especificado
lista = ["2", "5", "6", "7", "8"]
print("-".join(lista))

# El método upper convierte todos los caracteres de una cadena a mayúsculas
informacion = "hola, como estas?"
infoEnMayusculas = informacion.upper()
print(infoEnMayusculas)

# El método lower convierte todos los caracteres de una cadena a minúsculas
informacion = "HOLA, COMO ESTAS?"
infoEnMinusculas = informacion.lower()
print(infoEnMinusculas)

# El método title convierte la primera letra de cada palabra en una cadena a mayúsculas
informacion = "hola, como estas?"
infoConTitulo = informacion.title()
print(infoConTitulo)

# El método find busca la primera ocurrencia de una subcadena en una cadena y devuelve su posición
informacion = "hola, como estas?"
posicionSubcadena = informacion.find("como")
print(posicionSubcadena)

# El método capitalize convierte el primer carácter de una cadena a mayúsculas y el resto a minúsculas
informacion = "hola, como estas?"
infoCapitalizada = informacion.capitalize()
print(infoCapitalizada)

# El método count cuenta el número de veces que una subcadena aparece en una cadena
informacion = "hola, como estas?"
cuentaSubcadena = informacion.count("o")
print(cuentaSubcadena)

# El método endswith devuelve True si una cadena termina con el sufijo especificado, de lo contrario devuelve False
informacion = "hola, como estas?"
terminaCon = informacion.endswith("?")
print(terminaCon)

# El método startswith devuelve True si una cadena comienza con el prefijo especificado, de lo contrario devuelve False
informacion = "hola, como estas?"
comienzaCon = informacion.startswith("h")
print(comienzaCon)

# El método isalnum devuelve True si todos los caracteres de una cadena son alfanuméricos (letras o números), de lo contrario devuelve False
informacion = "hola123"
esAlfanumerica = informacion.isalnum()
print(esAlfanumerica)

# El método isalpha devuelve True si todos los caracteres de una cadena son letras, de lo contrario devuelve False
informacion = "hola"
esAlfabetica = informacion.isalpha()
print(esAlfabetica)

# El método isdigit devuelve True si todos los caracteres de una cadena son dígitos, de lo contrario devuelve False
informacion = "123"
esDigito = informacion.isdigit()
print(esDigito)

# El método islower devuelve True si todos los caracteres alfabéticos de una cadena están en minúsculas, de lo contrario devuelve False
informacion = "hola"
esMinuscula = informacion.islower()
print(esMinuscula)

# El método isupper devuelve True si todos los caracteres alfabéticos de una cadena están en mayúsculas, de lo contrario devuelve False
informacion = "HOLA"
esMayuscula = informacion.isupper()
print(esMayuscula)

# El método isspace devuelve True si todos los caracteres de una cadena son espacios en blanco, de lo contrario devuelve False
informacion = "   "
esEspacioBlanco = informacion.isspace()
print(esEspacioBlanco)

# El método swapcase intercambia mayúsculas por minúsculas y viceversa en una cadena
informacion = "HoLa"
infoIntercambiada = informacion.swapcase()
print(infoIntercambiada)
