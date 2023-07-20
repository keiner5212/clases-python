# Importa el módulo pickle
import pickle
# Importa la clase Persona desde el módulo objetos_constructor
from poo.objetos_constructor import Persona

# Crea un objeto de la clase Persona
persona1 = Persona("Juan", 30)

# Abre un archivo en modo escritura binaria
archivo=open("./recursos/objeto_guardado.dat","wb")
# Utiliza el método dump() de pickle para guardar el objeto en el archivo
pickle.dump(persona1,archivo)
# Cierra el archivo
archivo.close()

# Abre el archivo en modo lectura binaria
archivo=open("./recursos/objeto_guardado.dat","rb")
# Utiliza el método load() de pickle para cargar el objeto desde el archivo
persona=pickle.load(archivo)
# Cierra el archivo
archivo.close()

# Llama al método presentarse() del objeto cargado desde el archivo
persona.presentarse()
