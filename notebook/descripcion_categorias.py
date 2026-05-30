import pandas as pd

def describir_datos_categoria(data_frame_limpio):
    # print("descripccion general del dataset de categorias")
    # print(f"numero de filas del dataset: {data_frame_limpio.shape[0]}")
    # print(f"numero de columnas del dataset: {data_frame_limpio.shape[1]}")
    # print(f"nombres de las columnas: {list(data_frame_limpio.columns)}")
    # print(f"tipos de datos de cada atributo: {data_frame_limpio.dtypes}")

    # print("*** Estadísticas Descriptivas ***")
    # print(f"{data_frame_limpio[['id']].describe()}")

    # print("*** Conteos ***")
    # print(f"{data_frame_limpio['nombre'].value_counts}")


    print("\n*** Tabla de Categorías ***")
    print(data_frame_limpio.to_string(index=False))
