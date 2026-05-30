import pandas as pd

def limpiar_datos(data_frame_sucio):
    data_frame_limpio = data_frame_sucio.copy()

    columnas_texto = ["nombre"]

    for columna in columnas_texto:
        data_frame_limpio[columna] = (
            data_frame_limpio[columna]
            .astype("string")
            .str.strip()
            .str.lower()
        )

    data_frame_limpio["id"] = pd.to_numeric(
        data_frame_limpio["id"],
        errors="coerce"
    )

    data_frame_limpio = data_frame_limpio[
        data_frame_limpio["id"] > 0
    ]

    columnas_obligatorias = ["id", "nombre"]

    data_frame_limpio = data_frame_limpio.dropna(
        subset=columnas_obligatorias
    )

    data_frame_limpio = data_frame_limpio.drop_duplicates()

    return data_frame_limpio