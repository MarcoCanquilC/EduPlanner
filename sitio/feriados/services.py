import requests

def obtener_feriados_chile(api_key, year):
    
    url = f"https://calendarific.com/api/v2/holidays"
    
    params = {
        "api_key": api_key,
        "country": "CL",  
        "year": year,
        "type": "national" , 
        "language": "es"  # Configura el idioma en español
    }
   
    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        holidays = data.get("response", {}).get("holidays", [])
        return holidays
    else:
        raise Exception(f"Error al obtener feriados: {response.status_code}")
    

