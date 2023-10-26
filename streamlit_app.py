import streamlit as st
from deepgram import Deepgram
import json

# Configuración de la API de Deepgram
DEEPGRAM_API_KEY = '887355a9368a2b55cbb723a9b735af03f618ed6c'
dg_client = Deepgram(DEEPGRAM_API_KEY)

# Título de la aplicación
st.title("Transcripción de Voz en Tiempo Real")

# Texto explicativo
st.write("Graba tu voz y obtén una transcripción en tiempo real.")

# Iniciar la grabación de voz
recording = st.radio("Iniciar la grabación de voz", ("Sí", "No"))

if recording == "Sí":
    st.write("¡Grabando! Habla para comenzar la transcripción.")

    # Código para la grabación de voz (debes implementar esto)

    # Después de la grabación, envía el archivo de audio a Deepgram para transcripción
    # Sustituye 'audio_data' con los datos reales de audio grabados
    audio_data = None
    response = dg_client.transcription.sync({
        "content": audio_data,
        "model": "nova",
        "language": "es",
        "smart_format": True,
    })

    # Muestra la transcripción en tiempo real
    st.write("Transcripción en tiempo real:")
    if "text" in response:
        st.write(response["text"])
    else:
        st.write("Transcripción no disponible.")

# Detener la grabación de voz
else:
    st.write("Grabación de voz detenida.")

# Fin de la aplicación
