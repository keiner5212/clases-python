# La biblioteca time en Python proporciona varias funciones relacionadas con el tiempo.

import time

# Puedes usar la función time() para obtener la hora actual en segundos desde el Epoch.
hora_actual = time.time()
print(f"La hora actual es {hora_actual} segundos desde el Epoch.")

# Puedes usar la función ctime() para convertir una hora en segundos desde el Epoch en una cadena de caracteres legible por humanos.
hora_legible = time.ctime(hora_actual)
print(f"La hora actual es {hora_legible}.")

# Puedes usar la función sleep() para hacer que tu programa espere un número determinado de segundos antes de continuar.
print("El programa se detendrá durante 5 segundos.")
time.sleep(5)
print("El programa ha reanudado su ejecución.")

# Puedes usar la función strftime() para formatear una hora en una cadena de caracteres personalizada.
hora_actual = time.localtime()
hora_formateada = time.strftime("%Y-%m-%d %H:%M:%S", hora_actual)
print(f"La hora actual es {hora_formateada}.")

# Puedes usar la función strptime() para convertir una cadena de caracteres en una hora.
hora_str = "2023-07-27 14:30:00"
hora_objeto = time.strptime(hora_str, "%Y-%m-%d %H:%M:%S")
print(f"La hora es {hora_objeto.tm_hour}:{hora_objeto.tm_min}:{hora_objeto.tm_sec} el {hora_objeto.tm_mday}/{hora_objeto.tm_mon}/{hora_objeto.tm_year}.")
