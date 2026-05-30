import pandas as p

def transformar_datos_usuario(data_frame_limpio):

    # 1. Usuarios activos por rol
    filtro1 = data_frame_limpio.query("activo == True")

    agrupacion1 = filtro1.groupby("rol")["id"] \
        .count() \
        .reset_index(name="cantidad_usuarios")

    print("\n=== Usuarios activos por rol ===")
    print(agrupacion1)


    # 2. Cantidad de usuarios por estado (activos/inactivos)
    filtro2 = data_frame_limpio.query("id > 0")

    agrupacion2 = filtro2.groupby("activo")["id"] \
        .count() \
        .reset_index(name="total_usuarios")

    print("\n=== Usuarios agrupados por estado ===")
    print(agrupacion2)


    # 3. Usuarios registrados por apellido
    filtro3 = data_frame_limpio.query("apellidos.notnull()", engine="python")

    agrupacion3 = filtro3.groupby("apellidos")["id"] \
        .count() \
        .reset_index(name="cantidad")

    print("\n=== Cantidad de usuarios por apellido ===")
    print(agrupacion3)


    # 4. Usuarios con teléfono registrado por rol
    filtro4 = data_frame_limpio.query("telefono.notnull()", engine="python")

    agrupacion4 = filtro4.groupby("rol")["telefono"] \
        .count() \
        .reset_index(name="telefonos_registrados")

    print("\n=== Teléfonos registrados por rol ===")
    print(agrupacion4)


    # 5. Usuarios registrados por fecha
    filtro5 = data_frame_limpio.query("fecharegistro != '0001-01-01T00:00:00'")

    agrupacion5 = filtro5.groupby("fecharegistro")["id"] \
        .count() \
        .reset_index(name="usuarios_registrados")

    print("\n=== Usuarios registrados por fecha ===")
    print(agrupacion5)

    return {
        "agrupacion1": agrupacion1,
        "agrupacion2": agrupacion2,
        "agrupacion3": agrupacion3,
        "agrupacion4": agrupacion4,
        "agrupacion5": agrupacion5
    }