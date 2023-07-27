import pandas as pd


def generar_excel_con_pandas(nombre_archivo):
    # Datos a agregar al archivo Excel
    datos = {
        'Nombre': ['Juan', 'María'],
        'Edad': [30, 25]
    }

    # Crear un DataFrame a partir de los datos
    df = pd.DataFrame(datos)

    # Crear un escritor Excel usando pandas
    escritor = pd.ExcelWriter(nombre_archivo, engine='xlsxwriter')

    # Convertir el DataFrame a una hoja de Excel
    df.to_excel(escritor, sheet_name='Hoja1', index=False)

    # Cerrar el escritor para guardar el archivo Excel
    escritor._save()
    print(f'Se ha generado el archivo "{nombre_archivo}" con éxito.')


# Llama a la función para generar el archivo Excel
nombre_archivo_excel = './recursos/datos_personas_pandas.xlsx'
generar_excel_con_pandas(nombre_archivo_excel)
