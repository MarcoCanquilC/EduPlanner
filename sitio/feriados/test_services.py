from services import obtener_feriados_chile

api_key = "Gl7GhLSWWMgW3yq7mbwCOqkRvLEADGcb"
year = 2024

try:
    feriados = obtener_feriados_chile(api_key, year)
    for feriado in feriados:
        print(f"Nombre: {feriado['name']}, Fecha: {feriado['date']['iso']}")
except Exception as e:
    print(f"Error: {e}")
