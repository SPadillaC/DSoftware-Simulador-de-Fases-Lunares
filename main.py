import streamlit as st
from datetime import datetime
from src.simulador_fases_lunares.observador import crear_observador
from src.simulador_fases_lunares.datos_lunares import calcular_fase_lunar
from src.simulador_fases_lunares.visualizacion_fase_lunar import mostrar_imagen_fase

def main():
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

    st.title("Simulador de Fases Lunares")

    year = st.slider("Año", 2020, 2030, st.session_state['year'])
    month = st.slider("Mes", 1, 12, st.session_state['month'])
    day = st.slider("Día", 1, 31, st.session_state['day'])
    hour = st.slider("Hora", 0, 23, st.session_state['hour'])
    minute = st.slider("Minutos", 0, 59, st.session_state['minute'])
    second = st.slider("Segundos", 0, 59, st.session_state['second'])

    fecha_hora = datetime(year, month, day, hour, minute, second)
    st.write(f"Fecha y hora seleccionada: {fecha_hora}")

    if st.button("Calcular Fase Lunar"):
        observador = crear_observador(fecha_hora)
        datos_lunares = calcular_fase_lunar(observador)

        # Mostrar la imagen de la fase lunar primero y con tamaño reducido
        mostrar_imagen_fase(datos_lunares['nombre_fase_lunar'], width=300)  # Ajusta el ancho según sea necesario

        st.write(f"Fase Lunar Actual: {datos_lunares['nombre_fase_lunar']}")
        st.write(f"Constelación: {datos_lunares['constelacion']}")
        st.write(f"Magnitud: {datos_lunares['magnitud']}")
        st.write(f"Distancia: {datos_lunares['distancia_km']:.0f} km")
        st.write(f"Siguiente Luna Nueva: {datos_lunares['siguiente_luna_nueva']}")
        st.write(f"Siguiente Luna Llena: {datos_lunares['siguiente_luna_llena']}")

if __name__ == "__main__":
    main()
