from datetime import datetime

turnos_mock = [
    {"fecha": "2025-06-03", "hora": "09:00", "id": "7051", "cliente": "Jorge Ariel Alvarenga"},
    {"fecha": "2025-06-02", "hora": "09:00", "id": "7084", "cliente": "José Antonio Iraia Rodas"},
    {"fecha": "2025-05-31", "hora": "09:30", "id": "7028", "cliente": "Yael Evelin Castillo"},
    {"fecha": "2025-05-30", "hora": "09:30", "id": "7067", "cliente": "Carlos Damián Gomez"},
]

def obtener_turnos(fecha, hora):
    fecha_str = fecha.strftime("%Y-%m-%d")
    for turno in turnos_mock:
        if turno["fecha"] == fecha_str and turno["hora"] == hora:
            return turno
    return None
