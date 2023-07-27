import pandas as pd


def generar_csv_con_pandas(nombre_archivo):
    # Datos a agregar al archivo CSV
    datos = {
        'Nombre': ['Juan', 'María'],
        'Edad': [30, 25]
    }

    # Crear un DataFrame a partir de los datos
    df = pd.DataFrame(datos)

    # Guardar el DataFrame en un archivo CSV
    df.to_csv(nombre_archivo, index=False)
    print(
        f'Se ha generado el archivo "{nombre_archivo}" en formato CSV con éxito.')


# Llama a la función para generar el archivo CSV
nombre_archivo_csv = './recursos/datos_personas.csv'
generar_csv_con_pandas(nombre_archivo_csv)
