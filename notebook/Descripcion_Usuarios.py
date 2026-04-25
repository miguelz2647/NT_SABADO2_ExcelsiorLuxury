import pandas as pd

def describir_datos_usuario(data_frame_limpio):
    print("descripccion general del dataset")
    print(f"numero de filas del dataset: {data_frame_limpio.shape[0]}")
    print(f"numero de columnas del dataset: {data_frame_limpio.shape[1]}")
    print(f"nombres de las columnas: {list(data_frame_limpio.columns)}")
    print(f"tipos de datos de cada atributo: {data_frame_limpio.dtypes}")

    print("*** Estadísticas Descriptivas ***")
    print(f"{data_frame_limpio[['Id']].describe()}")

    print("*** Conteos ***")
    print(f"{data_frame_limpio["Nombres"].value_counts}")
    print(f"{data_frame_limpio["Apellidos"].value_counts}")
    print(f"{data_frame_limpio["Email"].value_counts}")
    print(f"{data_frame_limpio["Contraseña"].value_counts}")
