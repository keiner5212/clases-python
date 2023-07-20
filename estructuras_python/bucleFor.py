# Solicitamos al usuario que ingrese un valor utilizando la función input
valor = int(input("Ingresa un número para mostrar su tabla de multiplicar: "))

# Utilizamos un bucle for para repetir un bloque de código un número determinado de veces
for i in range(0, 11):
    # Dentro del bucle, mostramos el resultado de la multiplicación del valor ingresado por el usuario por el valor de la variable i
    print(f"{valor} X {i} = {valor * i}")
