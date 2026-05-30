import pandas as pd

def limpieza_usuarios(data_frame_sucio):
    data_frame_limpio = data_frame_sucio.copy()

    # Normaliza columnas a minúscula
    data_frame_limpio.columns = data_frame_limpio.columns.str.lower()

    # 👇 Elimina columnas con listas (no son comparables)
    columnas_listas = ["direcciones", "ordenes", "opiniones", "carritos"]
    data_frame_limpio = data_frame_limpio.drop(columns=columnas_listas)

    columnas_texto = ["nombres", "apellidos", "email", "contraseña"]
    for columna in columnas_texto:
        data_frame_limpio[columna] = data_frame_limpio[columna].astype("string").str.strip().str.lower()

    data_frame_limpio["id"] = pd.to_numeric(data_frame_limpio["id"])

    data_frame_limpio = data_frame_limpio[data_frame_limpio["id"] > 0]

    columnas_obligatorias = ["id", "nombres", "apellidos", "email", "contraseña"]
    data_frame_limpio = data_frame_limpio.dropna(subset=columnas_obligatorias)

    data_frame_limpio = data_frame_limpio.drop_duplicates()

    return data_frame_limpio