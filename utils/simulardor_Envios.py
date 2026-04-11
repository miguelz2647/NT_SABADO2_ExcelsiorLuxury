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

        envios.append(envio)

    return envios