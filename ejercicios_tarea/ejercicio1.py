# diseña un programa en el que tengas que hacer un menu de 
# operaciones manejando listas, tienes que hacer el menu con ciclo 
# for y tambien con while, osea 2 versiones, y el programa 
# debe permitir hacer distintas operaciones entre los numeros en una lista
# por ejemplo, teniendo la lista de abajo debes preguntar por las 
# posiciones que quieres operar
import math
lista=[2,41,4,52,67,47,28,12]

# digamos que quieres operar los 2 primeros numeros, entonces como usuario, 
# debes decir que los numeros que quieres operar son el de la posicion 0 y el de la 1
# entonces debes decirle que elija la operacion y mostrar el resultado


n=int( input("Cuantas veces quieres ejecutar el menu?: ") )

for i in range(0,n):
    print("\n\n1. suma\n2. resta\n3. multiplicacion\n4. division\n5. potencia\n6. raiz\ncualquier otro: salir")
    opcion=int( input("Tu eleccion: ") )
    if(opcion>0 and opcion<7):
        print("tienes que elegir los valores a operar de la lista:",lista)
        a=int(input("ingresa la posicion del primer dato: "))
        b=int(input("ingresa la posicion del segundo dato: "))

    if(opcion==1):
        print("el resultado de la suma de",lista[a],"+",lista[b],"es igual a:",lista[a]+lista[b])
    elif(opcion==2):
        print("el resultado de la resta de",lista[a],"-",lista[b],"es igual a:",lista[a]-lista[b])
    elif(opcion==3):
        print("el resultado de la multiplicacion de",lista[a],"X",lista[b],"es igual a:",lista[a]*lista[b])
    elif(opcion==4):
        print("el resultado de la division de",lista[a],"/",lista[b],"es igual a:",lista[a]/lista[b])
    elif(opcion==5):
        print("el resultado de la potencia de",lista[a],"^",lista[b],"es igual a:",lista[a]**lista[b])
    elif(opcion==6):
        print("el resultado de la raiz de sqrt(",lista[a],",",lista[b],") es igual a:",lista[a]**(1/lista[b]))
    else:
        print("adios")
        break