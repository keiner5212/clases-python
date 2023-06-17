# Importa la clase Fernet desde el módulo cryptography.fernet
from cryptography.fernet import Fernet

# Genera una clave de encriptación
clave=Fernet.generate_key()
# Crea un objeto Fernet para encriptar información
encriptador=Fernet(clave)

# Abre un archivo en modo escritura binaria
archivo = open("./ejemplo.dat", "wb")
# Define el contenido a escribir en el archivo
contenido = b"hola, esto va a ir en el archivo"
# Encripta el contenido utilizando el objeto Fernet
contenido_encriptado=encriptador.encrypt(contenido)
# Escribe el contenido encriptado en el archivo
archivo.write(contenido_encriptado)
# Cierra el archivo
archivo.close()

# Abre un archivo en modo escritura binaria para guardar la clave de encriptación
archivo = open("./clave.dat", "wb")
# Escribe la clave de encriptación en el archivo
archivo.write(clave)
# Cierra el archivo
archivo.close()

# Importa la clase Fernet desde el módulo cryptography.fernet
from cryptography.fernet import Fernet
# Abre el archivo que contiene la clave de encriptación en modo lectura binaria
archivo = open("./clave.dat", "rb")
# Lee la clave de encriptación desde el archivo
clave_desencriptadora=archivo.read()
# Cierra el archivo
archivo.close()

# Abre el archivo que contiene la información encriptada en modo lectura binaria
archivo = open("./ejemplo.dat", "rb")
# Crea un objeto Fernet para desencriptar información utilizando la clave leída desde el archivo
encriptador=Fernet(clave_desencriptadora)
# Desencripta el contenido del archivo utilizando el objeto Fernet
contenido_desencriptado=encriptador.decrypt(archivo.read())
# Cierra el archivo
archivo.close()

# Imprime el contenido desencriptado
print(contenido_desencriptado)
