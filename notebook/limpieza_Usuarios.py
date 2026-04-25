import pandas as pd

def limpieza_usuarios(data_frame_sucio):
    data_frame_limpio = data_frame_sucio.copy()

    columnas_texto = ["Nombres", "Apellidos", "Email", "Contraseña"]
    for columna in columnas_texto:
        data_frame_limpio[columna] = data_frame_limpio[columna].astype("string").str.strip().str.lower()

    data_frame_limpio["Id"] = pd.to_numeric(data_frame_limpio["Id"])

    data_frame_limpio = data_frame_limpio[data_frame_limpio["Id"] > 0]

    columnas_obligatorias = ["Id", "Nombres", "Apellidos", "Email", "Contraseña"]
    data_frame_limpio = data_frame_limpio.dropna(subset=columnas_obligatorias)

    data_frame_limpio = data_frame_limpio.drop_duplicates()

    return data_frame_limpio