import os
import streamlit as st

def obtener_imagen_fase(nombre_fase_lunar: str) -> str:
    imagenes_fases = {
        "Luna Nueva": "luna_nueva.jpg",
        "Creciente Iluminante": "creciente_iluminante.jpg",
        "Cuarto Creciente": "cuarto_creciente.jpg",
        "Gibosa Creciente": "gibosa_creciente.jpg",
        "Luna Llena": "luna_llena.jpg",
        "Gibosa Menguante": "gibosa_menguante.jpg",
        "Cuarto Menguante": "cuarto_menguante.jpg",
        "Creciente Menguante": "creciente_menguante.jpg",
        "Fase Desconocida": "fase_desconocida.jpg"
    }
    return os.path.join("src", "imagenes_fases", imagenes_fases.get(nombre_fase_lunar, "fase_desconocida.jpg"))

def mostrar_imagen_fase(nombre_fase_lunar: str, width: int = 300):
    imagen_fase = obtener_imagen_fase(nombre_fase_lunar)
    
    if not os.path.exists(imagen_fase):
        st.error(f"Error: La imagen para la fase '{nombre_fase_lunar}' no se encontró.")
        imagen_fase = os.path.join("src", "imagenes_fases", "fase_desconocida.jpg")
    
    st.image(imagen_fase, caption=f"Fase Lunar: {nombre_fase_lunar}", width=width)
