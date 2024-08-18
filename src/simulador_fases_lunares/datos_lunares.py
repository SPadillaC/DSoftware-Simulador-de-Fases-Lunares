import ephem
from datetime import datetime

def calcular_fase_lunar(observador: ephem.Observer) -> dict:
    """
    Calcula diversos parámetros relacionados con la fase lunar actual para un observador dado.

    Args:
        observador (ephem.Observer): Un objeto ephem.Observer que contiene la fecha, hora y ubicación del observador.

    Raises:
        ValueError: Si ocurre un error al calcular la fase lunar.

    Returns:
        dict: Un diccionario con la siguiente información:
            - "constelacion": La constelación en la que se encuentra la luna.
            - "magnitud": La magnitud aparente de la luna.
            - "distancia_km": La distancia de la luna a la Tierra en kilómetros.
            - "fase": El porcentaje de luminosidad de la luna.
            - "siguiente_luna_nueva": La fecha y hora de la próxima luna nueva.
            - "siguiente_luna_llena": La fecha y hora de la próxima luna llena.
            - "nombre_fase_lunar": El nombre de la fase lunar actual.
    """
    try:
        # Crear un objeto Moon con la información del observador
        luna = ephem.Moon(observador)
        
        # Calcular la fase lunar y convertirla a decimal para facilitar comparaciones
        fase = luna.phase / 100
        magnitud = luna.mag
        
        # Convertir la distancia de UA a kilómetros
        distancia_km = luna.earth_distance * 149597870.7
        
        # Determinar la constelación en la que se encuentra la luna
        constelacion = ephem.constellation(luna)[1]
        
        # Calcular las fechas de la siguiente luna llena y nueva
        siguiente_luna_llena = ephem.next_full_moon(observador.date)
        siguiente_luna_nueva = ephem.next_new_moon(observador.date)

        # Convertir fechas a timestamps Unix para facilitar comparaciones
        fecha_actual_unix = observador.date.datetime().timestamp()
        siguiente_luna_nueva_unix = siguiente_luna_nueva.datetime().timestamp()
        siguiente_luna_llena_unix = siguiente_luna_llena.datetime().timestamp()

        # Determinar si la luna está creciendo o menguando
        luna_creciente = fecha_actual_unix < siguiente_luna_llena_unix if siguiente_luna_llena_unix < siguiente_luna_nueva_unix else fecha_actual_unix < siguiente_luna_nueva_unix

        # Obtener el nombre de la fase lunar basándose en la fase y si está creciendo o menguando
        nombre_fase_lunar = obtener_fase_lunar(fase, luna_creciente)

    except Exception as e:
        # Capturar cualquier error y lanzarlo como un ValueError
        raise ValueError("Error al calcular la fase lunar") from e

    # Devolver un diccionario con toda la información calculada
    return {
        "constelacion": constelacion,
        "magnitud": magnitud,
        "distancia_km": distancia_km,
        "fase": fase * 100,  # Convertir de nuevo a porcentaje
        "siguiente_luna_nueva": siguiente_luna_nueva,
        "siguiente_luna_llena": siguiente_luna_llena,
        "nombre_fase_lunar": nombre_fase_lunar
    }

def obtener_fase_lunar(fase: float, luna_creciente: bool) -> str:
    """
    Determina el nombre de la fase lunar actual basándose en el porcentaje de luminosidad
    y si la luna está creciendo o menguando.

    Args:
        fase (float): El porcentaje de luminosidad de la luna en decimal (0.0 a 1.0).
        luna_creciente (bool): Verdadero si la luna está creciendo, Falso si está menguando.

    Returns:
        str: El nombre de la fase lunar, como "Luna Nueva", "Cuarto Creciente", etc.
    """
    if fase < 0 or fase > 1:
        return "Fase Desconocida"
    if 0 <= fase <= 0.05:
        return "Luna Nueva"
    elif 0.05 < fase <= 0.25:
        return "Creciente Iluminante" if luna_creciente else "Creciente Menguante"
    elif 0.25 < fase <= 0.50:
        return "Cuarto Creciente" if luna_creciente else "Cuarto Menguante"
    elif 0.50 < fase <= 0.75:
        return "Gibosa Creciente" if luna_creciente else "Gibosa Menguante"
    elif 0.75 < fase <= 1.00:
        return "Luna Llena"
    else:
        return "Fase Desconocida"
