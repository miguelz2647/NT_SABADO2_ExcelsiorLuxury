import pandas as pd

from utils.simulador_Usuarios import simular_Usuarios

Usuarios=simular_Usuarios(5)

Usuarios_ordenados=pd.DataFrame(Usuarios)

Usuarios_ordenados.to_json("Data/Usuarios.json",orient="records",indent=1)

Usuarios_ordenados.to_csv("Data/Usuarios.csv",index=False)
