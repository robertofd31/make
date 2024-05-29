import streamlit as st
import requests

# Título de la aplicación
st.title("Enviar Nombre y Apellidos")

# Solicitar el nombre y los apellidos
nombre = st.text_input("Nombre")
apellidos = st.text_input("Apellidos")

# Botón para enviar los datos
if st.button("Enviar"):
    # Crear un diccionario con los datos
    data = {
        "nombre": nombre,
        "apellidos": apellidos
    }

    # Enviar los datos a la URL
    response = requests.post("https://hook.eu2.make.com/yfyrs9qxwa6g1xlrzlx4s1ghcoh5occ0", json=data)

    # Mostrar el resultado de la solicitud
    if response.status_code == 200:
        st.success("Datos enviados correctamente.")
    else:
        st.error("Error al enviar los datos.")
