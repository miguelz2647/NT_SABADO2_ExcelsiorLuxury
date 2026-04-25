import pandas as pd

def limpiar_envios(data_frame_sucio):
    data_frame_limpio = data_frame_sucio.copy()

    columnas_texto = ["direccion", "ciudad", "estado"]
    for columna in columnas_texto:
        data_frame_limpio[columna] = data_frame_limpio[columna].astype("string").str.strip().str.lower()

    valores_validos_estado = ["pendiente", "enviado", "entregado"]
    data_frame_limpio["estado"] = data_frame_limpio["estado"].where(
        data_frame_limpio["estado"].isin(valores_validos_estado),
        pd.NA
    )

    data_frame_limpio["id_envio"] = pd.to_numeric(data_frame_limpio["id_envio"], errors="coerce")
    data_frame_limpio["id_usuario"] = pd.to_numeric(data_frame_limpio["id_usuario"], errors="coerce")

    data_frame_limpio["fecha_envio"] = pd.to_datetime(
        data_frame_limpio["fecha_envio"], errors="coerce"
    )

    data_frame_limpio = data_frame_limpio[data_frame_limpio["id_envio"] > 0]

    columnas_obligatorias = ["id_envio", "id_usuario", "direccion", "estado"]
    data_frame_limpio = data_frame_limpio.dropna(subset=columnas_obligatorias)

    data_frame_limpio = data_frame_limpio.drop_duplicates()

    return data_frame_limpio