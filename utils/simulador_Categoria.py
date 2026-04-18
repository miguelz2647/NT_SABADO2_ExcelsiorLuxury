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

        probabilodadError=random.random()

        if probabilodadError<0.7:
            categoria["Id"]=random.choice([None,-1,0])
            categoria["Nombre"]=None
        elif probabilodadError<0.3:
            categoria["Descripcion"]=" "+categoria["Descripcion"]+" "
        elif probabilodadError<0.6:
            categoria["Estado"]=categoria["Estado"].upper()

       
       
        categorias.append(categoria)
    return categorias
