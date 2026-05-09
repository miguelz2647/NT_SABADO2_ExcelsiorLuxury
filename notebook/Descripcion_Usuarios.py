import pandas as pd

def describir_datos_usuario(data_frame_limpio):
    print("descripcion general del dataset")
    print(f"numero de filas del dataset: {data_frame_limpio.shape[0]}")
    print(f"numero de columnas del dataset: {data_frame_limpio.shape[1]}")
    print(f"nombres de las columnas: {list(data_frame_limpio.columns)}")
    print(f"tipos de datos de cada atributo:\n{data_frame_limpio.dtypes}")

    print("*** Estadísticas Descriptivas ***")
    print(f"{data_frame_limpio[['id']].describe()}")

    print("*** Conteos ***")
    print(data_frame_limpio["nombres"].value_counts())
    print(data_frame_limpio["apellidos"].value_counts())
    print(data_frame_limpio["email"].value_counts())
    print(data_frame_limpio["contraseña"].value_counts())

        # 👇 Muestra los datos como cuadro
    print("\n*** Tabla de Usuarios ***")
    print(data_frame_limpio.to_string(index=False))