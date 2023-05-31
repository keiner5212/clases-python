
archivo=open("ejemplo.txt","r")

listaNumeros=[]
for numero in archivo.read().split(","):
    listaNumeros.append(int(numero))

print(sum(listaNumeros))

archivo.close()
