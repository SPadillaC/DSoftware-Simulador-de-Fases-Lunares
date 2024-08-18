import os
import streamlit as st

def obtener_imagen_fase(nombre_fase_lunar: str) -> str:
    """
    Obtiene la ruta de la imagen correspondiente a la fase lunar dada.

    Args:
        nombre_fase_lunar (str): El nombre de la fase lunar.

    Returns:
        str: La ruta del archivo de imagen correspondiente a la fase lunar.
    """
    # Diccionario que asocia el nombre de la fase lunar con el nombre del archivo de imagen correspondiente.
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
    
    # Construye la ruta completa de la imagen correspondiente a la fase lunar dada.
    return os.path.join("src", "imagenes_fases", imagenes_fases.get(nombre_fase_lunar, "fase_desconocida.jpg"))

def mostrar_imagen_fase(nombre_fase_lunar: str, width: int = 300):
    """
    Muestra la imagen de la fase lunar en la interfaz de usuario.

    Si la imagen de la fase lunar no se encuentra en la ruta especificada, 
    muestra un mensaje de error y carga una imagen por defecto.

    Args:
        nombre_fase_lunar (str): El nombre de la fase lunar.
        width (int, optional): El ancho de la imagen a mostrar. Por defecto es 300.
    """
    # Obtiene la ruta de la imagen correspondiente a la fase lunar.
    imagen_fase = obtener_imagen_fase(nombre_fase_lunar)
    
    # Verifica si la imagen existe en la ruta especificada.
    if not os.path.exists(imagen_fase):
        # Muestra un mensaje de error si la imagen no se encuentra.
        st.error(f"Error: La imagen para la fase '{nombre_fase_lunar}' no se encontró.")
        # Carga la imagen por defecto si no se encuentra la específica.
        imagen_fase = os.path.join("src", "imagenes_fases", "fase_desconocida.jpg")
    
    # Muestra la imagen con el título y el ancho especificado.
    st.image(imagen_fase, caption=f"Fase Lunar: {nombre_fase_lunar}", width=width)
