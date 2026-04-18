import pandas as pd
from utils.simulador_Categoria import simular_Categorias
from notebook.limpieza_categoria import limpiar_datos
from utils.simulador_Usuarios import simular_Usuarios

Usuarios=simular_Usuarios(5)

Usuarios_ordenados=pd.DataFrame(Usuarios)

Usuarios_ordenados.to_json("Data/Usuarios.json",orient="records",indent=1)

Usuarios_ordenados.to_csv("Data/Usuarios.csv",index=False)

Categorias=simular_Categorias(10)
Categorias_Ordenadas=pd.DataFrame(Categorias)
Categorias_Ordenadas=limpiar_datos(Categorias_Ordenadas)

Categorias_Ordenadas.to_json("Data/Categorias.json",orient="records",indent=1)

Categorias_Ordenadas.to_csv("Data/Categorias.csv",index=False)

print(Categorias_Ordenadas)