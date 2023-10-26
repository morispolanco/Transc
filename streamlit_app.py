import streamlit as st
import asyncio
import aiohttp
from deepgram import Deepgram
import os

# Título de la aplicación
st.title("Transcripción de Archivo de Audio")

# Your Deepgram API Key
DEEPGRAM_API_KEY = '887355a9368a2b55cbb723a9b735af03f618ed6c'


# URL para la transcripción de Deepgram
DEEPGRAM_URL = 'https://api.deepgram.com/v1/listen'

# Cargar un archivo de audio
uploaded_file = st.file_uploader("Sube un archivo de audio (.m4a, .mp3 o .wav)", type=["m4a", "mp3", "wav"])

def transcribe_audio(audio_data):
    try:
        headers = {
            'Authorization': f'Token {DEEPGRAM_API_KEY}',
        }
        response = requests.post(DEEPGRAM_URL, headers=headers, data=audio_data)

        if response.status_code == 200:
            transcript = response.json()
            st.write("Transcripción del archivo de audio:")
            st.write(transcript)
        else:
            st.write(f"Error al obtener la transcripción: {response.text}")

    except Exception as e:
        st.write(f'Error: {e}')

# Transcribir el archivo cargado
if uploaded_file is not None:
    st.write("Transcribiendo archivo de audio...")

    audio_data = uploaded_file.read()

    try:
        transcribe_audio(audio_data)
    except Exception as e:
        st.write("Error al procesar el archivo de audio. Asegúrate de que el archivo esté en un formato compatible (m4a, mp3, wav).")

# Reemplaza 'YOUR_DEEPGRAM_API_KEY' con tu clave de API de Deepgram antes de ejecutar la aplicación
