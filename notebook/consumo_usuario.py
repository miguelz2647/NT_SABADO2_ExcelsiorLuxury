import requests 
#escribir la url del servicio que quiero consumir
#utilizar el request de python para consumir el servicio
#verificar repuesta del servicio
#veriricar el formato de los datos recibidos
def consumir_api_usuario():
    url="https://localhost:44381/api/usuario/todos"

    response = requests.get(url, verify=False)

    response.raise_for_status()

    data=response.json()
    
    return(data) 