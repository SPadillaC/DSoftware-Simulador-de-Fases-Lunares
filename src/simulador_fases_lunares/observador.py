import ephem

def crear_observador(fecha_hora: str, lat: str = '-33.59217', lon: str = '-70.6996') -> ephem.Observer:
    observador = ephem.Observer()
    try:
        observador.date = fecha_hora
    except (ValueError, TypeError):
        raise ValueError("Formato de fecha inválido")
    observador.lat = '-33.59217'
    observador.lon = '-70.6996'
    observador.elevation = 570
    return observador
