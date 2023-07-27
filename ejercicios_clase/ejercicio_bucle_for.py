# Este programa muestra una tabla de multiplicar para un número especificado por el usuario.

# Solicitamos al usuario que ingrese un valor.
valor = int(input("Ingresa un número para mostrar su tabla de multiplicar: "))

# Mostramos una introducción al programa.
print("Este programa muestra una tabla de multiplicar para un número especificado por el usuario.")

# Mostramos la tabla de multiplicar.
for i in range(0, 11):
    print(f"{valor} X {i} = {valor * i}")

    # Preguntamos al usuario si desea ver otra tabla de multiplicar.
    respuesta = input("¿Quieres ver otra tabla de multiplicar? (s/n) ")

    # Verificamos si el usuario ingresó 's' o 'S'.
    if respuesta.lower() == "s":
        # Solicitamos al usuario que ingrese otro número.
        valor = int(input("Ingresa otro número para mostrar su tabla de multiplicar: "))
        print(f"Tabla de multiplicar para {valor}:")
        for i in range(0, 11):
            print(f"{valor} X {i} = {valor * i}")
    else:
        # Salimos del programa.
        print("¡Adiós!")
