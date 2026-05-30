import pandas as pd

def transformar_datos_categoria(data_frame_limpio):

    # 1. Cantidad de categorías registradas
    filtro1 = data_frame_limpio.query("id > 0")

    agrupacion1 = filtro1.groupby("nombre")["id"] \
        .count() \
        .reset_index(name="cantidad")

    print("\n=== Cantidad de categorías registradas ===")
    print(agrupacion1)


    # 2. Categorías agrupadas por inicial
    filtro2 = data_frame_limpio.query("nombre.notnull()", engine="python")

    filtro2["inicial"] = (
        filtro2["nombre"].str[0].str.upper()
    )

    agrupacion2 = filtro2.groupby("inicial")["id"] \
        .count() \
        .reset_index(name="cantidad_categorias")

    print("\n=== Categorías agrupadas por inicial ===")
    print(agrupacion2)


    # 3. Categorías por longitud del nombre
    filtro3 = data_frame_limpio.query("nombre.notnull()", engine="python")

    filtro3["longitud_nombre"] = (
        filtro3["nombre"].str.len()
    )

    agrupacion3 = filtro3.groupby("longitud_nombre")["id"] \
        .count() \
        .reset_index(name="cantidad_categorias")

    print("\n=== Categorías por longitud del nombre ===")
    print(agrupacion3)


    return {
        "agrupacion1": agrupacion1,
        "agrupacion2": agrupacion2,
        "agrupacion3": agrupacion3
    }