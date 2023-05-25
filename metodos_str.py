# split
informacion = "hola, como estas?"
infoSeparada = informacion.split("a")
print(infoSeparada)


# rstrip
informacion = "         \nhola, como estas???????????????"
print([informacion])
infoSinSaltosDeLinea = [informacion.rstrip("?")]
print(infoSinSaltosDeLinea)

# lstrip
informacion = "         \nhola, como estas???????????????"
print([informacion])
infoSinSaltosDeLinea = [informacion.lstrip(" ")]
print(infoSinSaltosDeLinea)

# strip
informacion = "         \nhola, como estas                    "
print([informacion])
infoSinSaltosDeLinea = [informacion.strip(" ")]
print(infoSinSaltosDeLinea)

# replace
informacion = "         \nhola, como estas                    "
print([informacion])
infoSinSaltosDeLinea = [informacion.replace("o","")]
print(infoSinSaltosDeLinea)


#join
lista=["2","5","6","7","8"]
print("-".join(lista))