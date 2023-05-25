#cuando necesitamos que una funcion reciba parametros pero no sabemos cuantos en especifico, podemos
#hacer que se permita cualquier numero de parametros, esto lo hacemos con el caracter "*" 
# antes de un parametro
def saludarGente(*atributos,otro="nada"):
    #dentro de la funcion todos los parametros que pasamos van a ser recibidos como una tupla
    print(otro)
    for persona in atributos:
        print("hola",persona)

#para enviar a la funcion cualquier otro parametro diferente a el que recibe varios
#tenemos que especificar cual parametro estamos ingresando
saludarGente("juan", "keiner", "pedro", "javier","ana",otro="este es otro atributo")