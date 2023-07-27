import random

numero = random.randint(1, 10)
intentos = 0

while intentos < 3:
    adivinanza = int(input("Adivina un número entre 1 y 10: "))
    intentos += 1

    if adivinanza == numero:
        print("¡Felicitaciones! Adivinaste el número.")
        break
    elif adivinanza < numero:
        print("Tu adivinanza es demasiado baja. Inténtalo de nuevo.")
    else:
        print("Tu adivinanza es demasiado alta. Inténtalo de nuevo.")

if intentos == 3:
    print(f"Lo siento, te quedaste sin intentos. El número era {numero}.")
