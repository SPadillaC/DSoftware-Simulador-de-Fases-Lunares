import ephem

def calcular_fase_lunar(observador):
    try:
        luna = ephem.Moon(observador)
        fase = luna.phase
        magnitud = luna.mag
        distancia_km = luna.earth_distance * 149597870.7  # Convertir AU a km
        constelacion = ephem.constellation(luna)[1]
        siguiente_luna_llena = ephem.next_full_moon(observador.date)
        siguiente_luna_nueva = ephem.next_new_moon(observador.date)
    except Exception as e:
        raise ValueError("Error al calcular la fase lunar") from e
    
    return {
        "constelacion": constelacion,
        "magnitud": magnitud,
        "distancia_km": distancia_km,
        "fase": fase,
        "siguiente_luna_nueva": siguiente_luna_nueva,
        "siguiente_luna_llena": siguiente_luna_llena
    }
