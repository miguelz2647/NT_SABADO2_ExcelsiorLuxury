import random
from datetime import datetime, timedelta

def simular_envios(n):
    estados = ["Pendiente", "Enviado", "Entregado", "pendiente", "ERROR", None]
    ciudades = ["Medellín", "Bogotá", "Cali", None]
    direcciones = ["Calle 123", "Carrera 45", "", None]

    envios = []

    for _ in range(n):
        envio = {
            "id_envio": random.randint(1, 10),
            "id_usuario": random.choice([1, 2, 3, None]),
            "direccion": random.choice(direcciones),
            "ciudad": random.choice(ciudades),
            "fecha_envio": datetime.now() + timedelta(days=random.randint(-5, 5)),
            "estado": random.choice(estados)
        }

        probabilidadError = random.random()

        if probabilidadError < 0.3:
            envio["id_envio"] = random.choice([None, -1, 0])
            envio["id_usuario"] = None
        elif probabilidadError < 0.6:
            envio["direccion"] = " " + str(envio["direccion"]) + " "
        elif probabilidadError < 0.8:
            envio["estado"] = str(envio["estado"]).upper()
        elif probabilidadError < 0.9:
            envio["fecha_envio"] = "fecha_invalida"

        envios.append(envio)

    return envios