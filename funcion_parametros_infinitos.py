
def saludarGente(*atributos,otro="nada"):
    print(otro)
    for persona in atributos:
        print("hola",persona)


saludarGente("juan", "keiner", "pedro", "javier","ana",otro="este es otro atributo")