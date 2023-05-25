
valor=int(input("Ingresa un numero para mostrar su tabla de multiplicar: "))

for i in range(0, 11): # como sabemos el bucle for nos va a ayudar a repetir un bloque de codigo un numero de veces
    print(valor,"X",i,"=",valor*i)
#cuando usamos range es porque le vamos a decir un intervalo en el que va a iterar, en este caso, va de 0 a 11, osea desde 0 hasta 10