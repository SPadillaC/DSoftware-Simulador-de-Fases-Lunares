import ephem

def crear_observador(fecha_hora: str, lat: str = '-33.59217', lon: str = '-70.6996') -> ephem.Observer:
    """
    Crea un objeto ephem.Observer con la fecha, hora y ubicación especificadas.

    Args:
        fecha_hora (str): La fecha y hora en formato string compatible con ephem.
        lat (str, optional): Latitud del observador en grados decimales como cadena. Por defecto es '-33.59217'.
        lon (str, optional): Longitud del observador en grados decimales como cadena. Por defecto es '-70.6996'.

    Raises:
        ValueError: Si el formato de la fecha es inválido.

    Returns:
        ephem.Observer: Un objeto ephem.Observer configurado con la fecha, hora, latitud, longitud y elevación especificadas.
    """
    # Crear una instancia del objeto Observer de la biblioteca ephem.
    observador = ephem.Observer()
    
    # Intentar asignar la fecha y hora al observador.
    try:
        observador.date = fecha_hora
    except (ValueError, TypeError):
        # Si la fecha es inválida, lanzar un ValueError con un mensaje descriptivo.
        raise ValueError("Formato de fecha inválido")
    
    # Configurar la latitud y longitud del observador.
    observador.lat = lat
    observador.lon = lon
    
    # Establecer la elevación del observador en metros sobre el nivel del mar.
    observador.elevation = 570
    
    return observador
