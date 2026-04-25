import pandas as pd

def limpiar_datos(data_frame_sucio):
    data_frame_limpio = data_frame_sucio.copy()

    # Columnas de texto
    columnas_texto = ["Nombre", "Descripcion", "Estado"]
    for columna in columnas_texto:
        data_frame_limpio[columna] = data_frame_limpio[columna].astype("string").str.strip().str.lower()

    # Valores válidos
    valores_validos_estado = ["activo", "inactivo"]
    data_frame_limpio["Estado"] = data_frame_limpio["Estado"].where(
        data_frame_limpio["Estado"].isin(valores_validos_estado),
        pd.NA
    )

    # Convertir a numérico
    data_frame_limpio["Id"] = pd.to_numeric(data_frame_limpio["Id"], errors="coerce")

    # Filtros
    data_frame_limpio = data_frame_limpio[data_frame_limpio["Id"] > 0]

    # Columnas obligatorias
    columnas_obligatorias = ["Id", "Nombre", "Estado"]
    data_frame_limpio = data_frame_limpio.dropna(subset=columnas_obligatorias)

    # Eliminar duplicados
    data_frame_limpio = data_frame_limpio.drop_duplicates()

    return data_frame_limpio