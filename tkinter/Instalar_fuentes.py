import sys

# Agregar el directorio actual al camino de búsqueda para importaciones
sys.path.append("./")

# Importar la función install_font del módulo otros.instalador_fuentes
from otros.instalador_fuentes import install_font

try:
    install_font("./recursos/fuentes/RuslanDisplay-Regular.ttf")
except InterruptedError as e:
    print(e)
