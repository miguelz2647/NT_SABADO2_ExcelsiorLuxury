import random
from datetime import datetime, timedelta 

def simular_Usuarios(num_usuarios):
    
    listaNombres = ["Juan", "María", "Carlos", "Ana", "Luis", "Sofía", "Pedro", "Lucía", "Miguel", "Valentina"]
    listaApellidos = ["García", "Rodríguez", "López", "Martínez", "Sánchez", "Pérez", "Gómez", "Díaz", "Fernández", "Vargas"]   
    listaEmails=["miguel@gmail.com", "maria@gmail.com", "carlos@gmail.com", "ana@gmail.com", "luis@gmail.com", "sofia@gmail.com", "pedro@gmail.com", "lucia@gmail.com", "miguel@gmail.com", "valentina@gmail.com"]
    listContraseñas=["password123", "qwerty456", "abcde789", "12345abc", "passw0rd", "letmein123", "welcome456", "admin789", "user12345", "mysecretpassword"]

    usuarios = []
    for _ in range(num_usuarios):
      
      usuario={
         "Id": random.randint(1, 1000),
         "Nombres": random.choice(listaNombres),
         "Apellidos": random.choice(listaApellidos),
         "Email": random.choice(listaEmails),
         "Contraseña": random.choice(listContraseñas),         
      }

      probabilodadError=random.random()

      if probabilodadError<0.1:
            usuario["Id"]=random.choice([None,-1,0])
            usuario["Nombres"]=None
      elif probabilodadError<0.3:
            usuario["Apellidos"]=" "+usuario["Apellidos"]+" "
      elif probabilodadError<0.6:
            usuario["Email"]=usuario["Email"].upper()
      elif probabilodadError<0.9:
            usuario["Contraseña"]=None


      usuarios.append(usuario)
    return usuarios
