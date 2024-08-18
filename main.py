import streamlit as st
from datetime import datetime
from src.simulador_fases_lunares.observador import crear_observador
from src.simulador_fases_lunares.datos_lunares import calcular_fase_lunar
from src.simulador_fases_lunares.visualizacion_fase_lunar import mostrar_imagen_fase

def main():
    """
    Función principal que gestiona la interfaz de usuario para el simulador de fases lunares.
    
    Esta función inicializa la interfaz de usuario utilizando Streamlit. Permite al usuario seleccionar
    una fecha y hora específica y calcula la fase lunar correspondiente. También muestra una imagen
    representativa de la fase lunar, junto con otros detalles como la constelación, magnitud, distancia a 
    la Tierra y las fechas de las próximas lunas nueva y llena.
    """
    # Inicializa el estado de la sesión con la fecha y hora actuales si no se ha hecho antes
    if 'initialized' not in st.session_state:
        now = datetime.now()
        st.session_state.update({
            'year': now.year,
            'month': now.month,
            'day': now.day,
            'hour': now.hour,
            'minute': now.minute,
            'second': now.second,
            'initialized': True
        })

    # Título de la aplicación
    st.title("Simulador de Fases Lunares")

    # Deslizadores para seleccionar año, mes, día, hora, minuto y segundo
    year = st.slider("Año", 2020, 2030, st.session_state['year'])
    month = st.slider("Mes", 1, 12, st.session_state['month'])
    day = st.slider("Día", 1, 31, st.session_state['day'])
    hour = st.slider("Hora", 0, 23, st.session_state['hour'])
    minute = st.slider("Minutos", 0, 59, st.session_state['minute'])
    second = st.slider("Segundos", 0, 59, st.session_state['second'])

    # Crear un objeto datetime a partir de los valores seleccionados
    fecha_hora = datetime(year, month, day, hour, minute, second)
    st.write(f"Fecha y hora seleccionada: {fecha_hora}")

    # Botón para calcular la fase lunar
    if st.button("Calcular Fase Lunar"):
        # Crear un observador con la fecha y hora seleccionadas
        observador = crear_observador(fecha_hora)
        # Calcular los datos lunares basados en el observador
        datos_lunares = calcular_fase_lunar(observador)

        # Mostrar la imagen de la fase lunar correspondiente
        mostrar_imagen_fase(datos_lunares['nombre_fase_lunar'], width=300)

        # Mostrar los detalles calculados sobre la fase lunar
        st.write(f"Fase Lunar Actual: {datos_lunares['nombre_fase_lunar']}")
        st.write(f"Porcentaje de Luminosidad: {datos_lunares['fase']:.2f}%")
        st.write(f"Constelación: {datos_lunares['constelacion']}")
        st.write(f"Magnitud: {datos_lunares['magnitud']}")
        st.write(f"Distancia: {datos_lunares['distancia_km']:.0f} km")
        st.write(f"Siguiente Luna Nueva: {datos_lunares['siguiente_luna_nueva']}")
        st.write(f"Siguiente Luna Llena: {datos_lunares['siguiente_luna_llena']}")

if __name__ == "__main__":
    main()
