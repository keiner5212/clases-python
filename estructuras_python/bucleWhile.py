# La sintaxis básica de un ciclo while en Python es la siguiente:
# Definimos una variable con un valor inicial
contador = 1

# Utilizamos un ciclo while para repetir un bloque de código mientras la variable contador sea menor o igual a 5
while contador <= 5:
    # Dentro del ciclo, mostramos el valor de la variable contador
    print(contador)
    # Incrementamos el valor de la variable contador en 1
    contador += 1  # Esto es equivalente a contador = contador + 1

# Puedes usar un ciclo while para leer la entrada del usuario hasta que ingrese un valor válido. Por ejemplo:
while True:
    respuesta = input("Ingresa 'sí' o 'no': ")
    if respuesta.lower() == "sí":
        print("Ingresaste 'sí'.")
        break
    elif respuesta.lower() == "no":
        print("Ingresaste 'no'.")
        break
    else:
        print("Entrada inválida. Por favor, inténtalo de nuevo.")

# Puedes usar un ciclo while para implementar un temporizador de cuenta regresiva. Por ejemplo:
import time

segundos = int(input("Ingresa el número de segundos para contar regresivamente: "))

while segundos > 0:
    print(segundos)
    time.sleep(1)
    segundos -= 1

print("¡Se acabó el tiempo!")
