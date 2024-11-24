import requests

def obtener_feriados(year):
    
    url = f"https://calendarific.com/api/v2/holidays"
    
    params = {
        "api_key": None,
        "country": "CL",  
        "year": year,
        "type": "national" , 
        "language": "es"
    }
   
    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        holidays = data.get("response", {}).get("holidays", [])
        return holidays
    else:
        raise Exception(f"Error al obtener feriados: {response.status_code}")
    

