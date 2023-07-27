# Utilizamos un bucle for para iterar sobre los números del 1 al 20
for i in range(1, 21):
    # Verificamos si el número es par
    if i % 2 == 0:
        # Si el número es par, lo imprimimos
        print(i)
    else:
        # Si el número es impar, saltamos al siguiente número sin imprimir nada
        continue

    # Imprimimos "resto del bucle" después de cada número par
    print("resto del bucle")
