import pandas as pd
from utils.simulador_Categoria import simular_Categorias
from notebook.limpieza_categoria import limpiar_datos
from utils.simulador_Usuarios import simular_Usuarios
from utils.simulador_Envios import simular_envios
from notebook.limpieza_Usuarios import limpieza_usuarios
from notebook.descripcion_usuarios import describir_datos_usuario
from notebook.descripcion_envios import describir_datos_envios

Usuarios=simular_Usuarios(5)
Usuarios_ordenados=pd.DataFrame(Usuarios)
Usuarios_ordenados=limpieza_usuarios(Usuarios_ordenados)

Usuarios_ordenados.to_json("Data/Usuarios.json",orient="records",indent=1)

Usuarios_ordenados.to_csv("Data/Usuarios.csv",index=False)

Envios=simular_envios(10)
Envios_ordenados=pd.DataFrame(Envios)

Envios_ordenados.to_json("Data/Envios.json",orient="records",indent=1)

Envios_ordenados.to_csv("Data/Envios.csv",index=False)

print(Envios_ordenados)

Categorias=simular_Categorias(10)
Categorias_Ordenadas=pd.DataFrame(Categorias)
Categorias_Ordenadas=limpiar_datos(Categorias_Ordenadas)

Categorias_Ordenadas.to_json("Data/Categorias.json",orient="records",indent=1)

Categorias_Ordenadas.to_csv("Data/Categorias.csv",index=False)

print(Categorias_Ordenadas)

describir_datos_usuario(Usuarios_ordenados)
describir_datos_envios(Envios_ordenados)
