# Solicitamos al usuario que ingrese un valor utilizando la función input
valor = int(input("Ingresa un número para mostrar su tabla de multiplicar: "))

# Utilizamos un bucle for para repetir un bloque de código un número determinado de veces
for i in range(0, 11):
    # Dentro del bucle, mostramos el resultado de la multiplicación del valor ingresado por el usuario por el valor de la variable i
    print(f"{valor} X {i} = {valor * i}")

# Puedes usar la función `enumerate()` para obtener tanto el índice como el valor de cada elemento en una lista. Por ejemplo:
fruits = ["apple", "banana", "cherry"]
for i, fruit in enumerate(fruits):
    print(i, fruit)  # Esto imprimirá: 0 apple, 1 banana, 2 cherry

# Puedes usar el guión bajo (`_`) como nombre de variable para ignorar el valor de una variable. Por ejemplo:
fruits = ["apple", "banana", "cherry"]
for _ in fruits:
    # Esto imprimirá: ¡Me encanta la fruta! ¡Me encanta la fruta! ¡Me encanta la fruta!
    print("¡Me encanta la fruta!")

# Puedes usar la función `zip()` para iterar sobre dos o más listas al mismo tiempo. Por ejemplo:
fruits = ["apple", "banana", "cherry"]
colors = ["red", "yellow", "pink"]
for fruit, color in zip(fruits, colors):
    # Esto imprimirá: La apple es red. La banana es yellow. La cherry es pink.
    print(f"La {fruit} es {color}.")
