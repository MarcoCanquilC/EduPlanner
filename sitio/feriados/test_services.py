from services import obtener_feriados

year = 2024

try:
    feriados = obtener_feriados( year)
    for feriado in feriados:
        print(f"Nombre: {feriado['name']}, Fecha: {feriado['date']['iso']}")
except Exception as e:
    print(f"Error: {e}")
