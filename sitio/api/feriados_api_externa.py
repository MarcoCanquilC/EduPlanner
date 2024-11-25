import requests
from .models import Feriado

def obtener_feriados():
    #URL base para acceder a la API de Calendarific.
    url = "https://calendarific.com/api/v2/holidays"
    
    #Parámetros para la solicitud a la API.
    parametros = {
        "api_key": "Gl7GhLSWWMgW3yq7mbwCOqkRvLEADGcb",
        "country": "CL",
        "year": 2024
    }

    #Realiza una solicitud GET a la API con los parámetros definidos.
    respuesta = requests.get(url, params=parametros)

    #Verifica si la solicitud fue exitosa (código de estado HTTP 200).
    if respuesta.status_code == 200:

        #Extraemos la lista de feriados de la respuesta.
        datos = respuesta.json()
        feriados = datos.get("response", {}).get("holidays", [])
        
        #Itera sobre cada feriado obtenido de la API.
        for feriado in feriados:
            try:

                #Obtenemos el nombre y fecha del feriado.
                nombre = feriado.get("name", "")
                fecha = feriado.get("date", {}).get("iso", "")
                 
                #Verifica si la fecha existe, si es así crea o 
                #actualiza un registro de feriado en la base de datos.
                if fecha:
                    Feriado.objects.get_or_create(
                        nombre=nombre,
                        fecha=fecha.split("T")[0]
                    )
                    
            #Muestra un mensaje en caso de error.
            except Exception as e:
                print(f"Error al guardar el feriado {feriado.get("name")}: {e}")
    else:
        #Lanza una excepción si la solicitud a la API no fue exitosa.
        raise Exception(f"Error al obtener feriados: {respuesta.status_code}")
