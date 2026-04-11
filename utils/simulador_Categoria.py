import random


def simular_Categorias(num_categorias):
    nombres = ["Deportivo", "Casual", "Hombre", "Mujer", "Niños", "Formal"]
    descripciones = [
        "Calzado y ropa diseñada para actividad física y deporte",
        "Estilo urbano cómodo para el uso diario",
        "Modelos pensados para hombres con ajuste masculine",
        "Diseños femeninos con estilo y confort",
        "Opciones resistentes y cómodas para niños",
        "Calzado elegante y formal para ocasiones especiales"
    ]
    estados = ["Activo", "Inactivo"]

    categorias = []
    for _ in range(num_categorias):
        categoria = {
            "Id": random.randint(1, 1000),
            "Nombre": random.choice(nombres),
            "Descripcion": random.choice(descripciones),
            "Estado": random.choice(estados),
        }
        categorias.append(categoria)

    return categorias
