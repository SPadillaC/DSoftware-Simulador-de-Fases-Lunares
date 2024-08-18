import ephem
from datetime import datetime

def calcular_fase_lunar(observador: ephem.Observer) -> dict:
    try:
        luna = ephem.Moon(observador)
        fase = luna.phase / 100  # Convertir el porcentaje a decimal para facilitar la comparación
        magnitud = luna.mag
        distancia_km = luna.earth_distance * 149597870.7  # Convertir AU a km
        constelacion = ephem.constellation(luna)[1]
        siguiente_luna_llena = ephem.next_full_moon(observador.date)
        siguiente_luna_nueva = ephem.next_new_moon(observador.date)

        # Verificar si la fecha es manejable por el timestamp Unix
        if observador.date.datetime().year >= 1970:
            fecha_actual_unix = observador.date.datetime().timestamp()
            siguiente_luna_nueva_unix = siguiente_luna_nueva.datetime().timestamp()
            siguiente_luna_llena_unix = siguiente_luna_llena.datetime().timestamp()

            # Determinar si la luna está creciendo o menguando
            luna_creciente = fecha_actual_unix < siguiente_luna_llena_unix if siguiente_luna_llena_unix < siguiente_luna_nueva_unix else fecha_actual_unix < siguiente_luna_nueva_unix
        else:
            # Asumir que la luna está creciendo si la fecha es muy antigua
            luna_creciente = True

        # Obtener el nombre de la fase lunar
        nombre_fase_lunar = obtener_fase_lunar(fase, luna_creciente)
        
    except Exception as e:
        raise ValueError("Error al calcular la fase lunar") from e

    return {
        "constelacion": constelacion,
        "magnitud": magnitud,
        "distancia_km": distancia_km,
        "fase": fase * 100,  # Convertir de vuelta a porcentaje
        "siguiente_luna_nueva": siguiente_luna_nueva,
        "siguiente_luna_llena": siguiente_luna_llena,
        "nombre_fase_lunar": nombre_fase_lunar
    }

def obtener_fase_lunar(fase: float, luna_creciente: bool) -> str:
    if fase < 0 or fase > 1:
        return "Fase Desconocida"
    elif fase < 0.05:
        return "Luna Nueva"
    elif fase < 0.25:
        return "Creciente Iluminante" if luna_creciente else "Creciente Menguante"
    elif fase < 0.50:
        return "Cuarto Creciente" if luna_creciente else "Cuarto Menguante"
    elif fase < 0.75:
        return "Gibosa Creciente" if luna_creciente else "Gibosa Menguante"
    elif fase <= 0.95:
        return "Luna Llena"
    return "Fase Desconocida"  # El else aquí no sería necesario, ya que el retorno final cubre todo