import pandas as pd

from utils.simulador_Categoria import simular_Categorias
from notebook.limpieza_categoria import limpiar_datos
from utils.simulador_Usuarios import simular_Usuarios
from utils.simulador_Envios import simular_envios
from notebook.limpieza_envios import limpiar_envios 


Usuarios = simular_Usuarios(1000)
df_usuarios = pd.DataFrame(Usuarios)

print("Usuarios antes:", len(df_usuarios))

# Limpieza básica
df_usuarios["Nombres"] = df_usuarios["Nombres"].astype("string").str.strip().str.lower()
df_usuarios["Apellidos"] = df_usuarios["Apellidos"].astype("string").str.strip().str.lower()
df_usuarios["Email"] = df_usuarios["Email"].astype("string").str.strip().str.lower()
df_usuarios["Id"] = pd.to_numeric(df_usuarios["Id"], errors="coerce")

df_usuarios = df_usuarios[df_usuarios["Id"] > 0]
df_usuarios = df_usuarios.dropna(subset=["Id", "Nombres", "Email"])
df_usuarios = df_usuarios.drop_duplicates()

print("Usuarios después:", len(df_usuarios))

df_usuarios.to_json("data/Usuarios.json", orient="records", indent=1)
df_usuarios.to_csv("data/Usuarios.csv", index=False)



Categorias = simular_Categorias(1000)
df_categorias = pd.DataFrame(Categorias)

print("Categorias antes:", len(df_categorias))

df_categorias = limpiar_datos(df_categorias)

print("Categorias después:", len(df_categorias))

df_categorias.to_json("data/Categorias.json", orient="records", indent=1)
df_categorias.to_csv("data/Categorias.csv", index=False)


# 🔹 ENVÍOS (ARREGLADO)
envios = simular_envios(1000)
df_envios = pd.DataFrame(envios)

print("Envios antes:", len(df_envios))

df_envios = limpiar_envios(df_envios) 

print("Envios después:", len(df_envios))

df_envios.to_json("data/Envios.json", orient="records", indent=1)
df_envios.to_csv("data/Envios.csv", index=False)