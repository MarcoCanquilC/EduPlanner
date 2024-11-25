import requests
from .models import Feriado

def obtener_feriados():
    url = "https://calendarific.com/api/v2/holidays"
    
    parametros = {
        "api_key": "Gl7GhLSWWMgW3yq7mbwCOqkRvLEADGcb", 
        "country": "CL",  
        "year": 2024,  
    }

    respuesta = requests.get(url, params=parametros)

    if respuesta.status_code == 200:
        datos = respuesta.json()
        feriados = datos.get("response", {}).get("holidays", [])
        
      
        for feriado in feriados:
            try:
                nombre = feriado.get("name", "")
                fecha = feriado.get("date", {}).get("iso", "")
                region = feriado.get("region", None)  

              
                if fecha:
                    Feriado.objects.get_or_create(
                        nombre=nombre,
                        fecha=fecha.split("T")[0],  
                        region=region 
                    )
                    
            except Exception as e:
                print(f"Error al guardar el feriado {feriado.get('name')}: {e}")
    else:
        raise Exception(f"Error al obtener feriados: {respuesta.status_code}")