#toda rutina de analizis debe describir el data set
# es imortante conocer cuantos registros tengo
#es importante conocer cuantos atributos tengo en el dataset
#es importante tener acceso a una lista con los nombres de los atributos
#es util hacer conteso de algunas columnas de interes
#es util conocer la estadisticas descriptivas de los campos numericos
#media-max-min-std-percentiles
#si tengo fechas es util conocer cual es la fecha mas antigua y cual es la fecha mas reciente
import pandas as pd

def describir_datos_usuario(data_frame_limpio):
    print("descripccion general del dataset")
    print(f"numero de filas del dataset: {data_frame_limpio.shape[0]}")
    print(f"numero de columnas del dataset: {data_frame_limpio.shape[1]}")
    print(f"nombres de las columnas: {list(data_frame_limpio.columns)}")
    print(f"tipos de datos de cada atributo: {data_frame_limpio.dtypes}")

    print("*** Estadísticas Descriptivas ***")
    print(f"{data_frame_limpio[['id']].describe()}")

    print("*** Conteos ***")
    print(f"{data_frame_limpio["Nombres"].value_counts}")
    print(f"{data_frame_limpio["Apellidos"].value_counts}")
    print(f"{data_frame_limpio["Email"].value_counts}")
    print(f"{data_frame_limpio["Contraseña"].value_counts}")
