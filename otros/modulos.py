# Importar todo el módulo con su nombre completo
import otros.modulo_ejemplo as modulo_ejemplo

print(modulo_ejemplo.ejemplo)
modulo_ejemplo.sayHello()
print(modulo_ejemplo.sumar(2, 5, 6, 7))


# Importar todo el módulo con un alias
import otros.modulo_ejemplo as x

print(x.ejemplo)


# Importar solo una función específica
from otros.modulo_ejemplo import sayHello

sayHello()


# Importar varias funciones específicas
from otros.modulo_ejemplo import sayHello, sumar

sayHello()
print(sumar(2, 5, 6, 7))


# Importar todo el módulo y utilizar las funciones directamente sin el nombre del módulo
from otros.modulo_ejemplo import *

print(ejemplo)
sayHello()
print(sumar(2, 5, 6, 7))
