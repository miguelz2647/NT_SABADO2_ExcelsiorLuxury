import pandas as pd

def describir_datos_envios(data_frame_limpio):
    print("descripccion general del dataset")
    print(f"numero de filas del dataset: {data_frame_limpio.shape[0]}")
    print(f"numero de columnas del dataset: {data_frame_limpio.shape[1]}")
    print(f"nombres de las columnas: {list(data_frame_limpio.columns)}")
    print(f"tipos de datos de cada atributo: {data_frame_limpio.dtypes}")

    print("*** Estadísticas Descriptivas ***")
    print(f"{data_frame_limpio[['id_envio','id_usuario']].describe()}")

    print("*** Conteos ***")
    print(f"{data_frame_limpio['direccion'].value_counts()}")
    print(f"{data_frame_limpio['ciudad'].value_counts()}")
    print(f"{data_frame_limpio['estado'].value_counts()}")
    
    print("*** Fechas de Envío ***")
    print(f"{data_frame_limpio['fecha_envio'].min()}")
    print(f"{data_frame_limpio['fecha_envio'].max()}")