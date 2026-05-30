import pandas as pd
from notebook.transformar_categorias import transformar_datos_categoria
from utils.simulador_Categoria import simular_Categorias
from notebook.limpieza_categoria import limpiar_datos
from utils.simulador_Usuarios import simular_Usuarios
from utils.simulador_Envios import simular_envios
from notebook.limpieza_Usuarios import limpieza_usuarios
from notebook.descripcion_usuarios import describir_datos_usuario
from notebook.descripcion_envios import describir_datos_envios
from notebook.limpieza_envios import limpiar_envios
from notebook.descripcion_categorias import describir_datos_categoria
from notebook.consumo_usuario import consumir_api_usuario
from notebook.consumo_categorias import consumir_api_categoria
from notebook.transformar_usuario import transformar_datos_usuario
from notebook.graficas import graficar_lineas, graficar_barras, graficar_torta, graficar_mapa_calor

#llamar api
data_api_usuarios=consumir_api_usuario()
data_api_categoria=consumir_api_categoria()


#ordenar datos
Usuarios_ordenados=pd.DataFrame(data_api_usuarios)
Categorias_Ordenadas=pd.DataFrame(data_api_categoria)
# Envios_ordenados=pd.DataFrame(data_api_envios)

#limpar datos
Usuarios_ordenados=limpieza_usuarios(Usuarios_ordenados)
Categorias_Ordenadas=limpiar_datos(Categorias_Ordenadas)
# Envios_ordenados=limpiar_envios(Envios_ordenados)



# Usuarios=simular_Usuarios(5)
# Categorias=simular_Categorias(10)
# Envios=simular_envios(10)


describir_datos_usuario(Usuarios_ordenados)
describir_datos_categoria(Categorias_Ordenadas)
transformar_datos_usuario(Usuarios_ordenados)
# describir_datos_envios(Envios_ordenados)

agrupaciones_usuarios = transformar_datos_usuario(Usuarios_ordenados)
agrupaciones_categorias = transformar_datos_categoria(Categorias_Ordenadas)

# 1. Usuarios activos por rol
graficar_barras(
    agrupaciones_usuarios["agrupacion1"],
    columna_categorias="rol",
    columna_valores="cantidad_usuarios",
    titulo="Usuarios activos por rol",
    color_barras="#4CAF50",
    nombre_archivo="barras_usuarios_roles.png"
)


# 2. Usuarios agrupados por estado
graficar_torta(
    agrupaciones_usuarios["agrupacion2"],
    columna_etiquetas="activo",
    columna_valores="total_usuarios",
    titulo="Usuarios activos e inactivos",
    nombre_archivo="torta_estados.png"
)


# 3. Cantidad de usuarios por apellido
graficar_barras(
    agrupaciones_usuarios["agrupacion3"],
    columna_categorias="apellidos",
    columna_valores="cantidad",
    titulo="Cantidad de usuarios por apellido",
    color_barras="#FF9800",
    nombre_archivo="barras_apellidos.png"
)


# 4. Teléfonos registrados por rol
graficar_barras(
    agrupaciones_usuarios["agrupacion4"],
    columna_categorias="rol",
    columna_valores="telefonos_registrados",
    titulo="Teléfonos registrados por rol",
    color_barras="#9C27B0",
    nombre_archivo="barras_telefonos_roles.png"
)


# 5. Usuarios registrados por fecha
graficar_lineas(
    agrupaciones_usuarios["agrupacion5"],
    columna_eje_x="fecharegistro",
    columna_eje_y="usuarios_registrados",
    titulo="Usuarios registrados por fecha",
    color_linea="#2196F3",
    nombre_archivo="lineas_registros.png"
)



# 1. Cantidad de categorías registradas
graficar_barras(
    agrupaciones_categorias["agrupacion1"],
    columna_categorias="nombre",
    columna_valores="cantidad",
    titulo="Cantidad de Categorías Registradas",
    color_barras="#4CAF50",
    nombre_archivo="barras_categorias.png"
)


# 2. Categorías agrupadas por inicial
graficar_torta(
    agrupaciones_categorias["agrupacion2"],
    columna_etiquetas="inicial",
    columna_valores="cantidad_categorias",
    titulo="Distribución de Categorías por Inicial",
    nombre_archivo="torta_iniciales_categorias.png"
)


# 3. Categorías por longitud del nombre
graficar_lineas(
    agrupaciones_categorias["agrupacion3"],
    columna_eje_x="longitud_nombre",
    columna_eje_y="cantidad_categorias",
    titulo="Categorías por Longitud del Nombre",
    color_linea="#2196F3",
    nombre_archivo="lineas_longitud_categorias.png"
)