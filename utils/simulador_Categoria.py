import random


def simular_Categorias(num_categorias):
    nombres = ["Deportivo", "Casual", "Hombre", "Mujer", "Niños", "Formal"]
    descripciones = [
        "Calzado y ropa diseñada para actividad física y deporte",
        "Estilo urbano cómodo para el uso diario",
        "Modelos pensados para hombres con ajuste masculino",
        "Diseños femeninos con estilo y confort",
        "Opciones resistentes y cómodas para niños",
        "Calzado elegante y formal para ocasiones especiales"
    ]
    estados = ["Activo", "Inactivo"]

    categorias = []

    for i in range(num_categorias):
        categoria = {
            "Id": i + 1,  # evita duplicados
            "Nombre": random.choice(nombres),
            "Descripcion": random.choice(descripciones),
            "Estado": random.choice(estados),
        }

        probabilidadError = random.random()

        if probabilidadError < 0.2:
            categoria["Id"] = random.choice([None, -1, 0])
            categoria["Nombre"] = None
        elif probabilidadError < 0.4:
            categoria["Descripcion"] = " " + categoria["Descripcion"] + " "
        elif probabilidadError < 0.6:
            categoria["Estado"] = categoria["Estado"].upper()

        categorias.append(categoria)

    return categorias
