import streamlit as st
import asyncio
import aiohttp
from deepgram import Deepgram

# Título de la aplicación
st.title("Transcripción de Archivo de Audio")

# Your Deepgram API Key
DEEPGRAM_API_KEY = '887355a9368a2b55cbb723a9b735af03f618ed6c'

# Cargar un archivo de audio
uploaded_file = st.file_uploader("Sube un archivo de audio (.m4a, .mp3 o .wav)", type=["m4a", "mp3", "wav"])

async def transcribe_audio(audio_data):
    try:
        # Inicializar el cliente de Deepgram
        deepgram = Deepgram(DEEPGRAM_API_KEY)

        # Crear una conexión WebSocket a Deepgram
        deepgramLive = await deepgram.transcription.live({
            'smart_format': True,
            'interim_results': False,
            'language': 'en-US',
            'model': 'nova',
        })

        # Escuchar el evento de cierre de la conexión
        deepgramLive.registerHandler(deepgramLive.event.CLOSE, lambda c: st.write(f'Conexión cerrada con el código {c}.'))

        # Enviar el archivo de audio a Deepgram
        deepgramLive.start()

        deepgramLive.send(audio_data)

        # Indicar que hemos terminado de enviar datos enviando un mensaje de cero bytes al punto final de transmisión de Deepgram y esperar hasta que recibamos el objeto de metadatos final
        await deepgramLive.finish()

        # Escuchar los resultados de la transcripción y mostrarlos en la aplicación
        async for transcript in deepgramLive:
            st.write("Transcripción del archivo de audio:")
            st.write(transcript)

    except Exception as e:
        st.write(f'Error: {e}')

# Transcribir el archivo cargado
if uploaded_file is not None:
    st.write("Transcribiendo archivo de audio...")

    audio_data = uploaded_file.read()

    # Comprobar si el archivo es compatible con pydub
    try:
        asyncio.run(transcribe_audio(audio_data))
    except Exception as e:
        st.write("Error al procesar el archivo de audio. Asegúrate de que el archivo esté en un formato compatible (m4a, mp3, wav).")

# Reemplaza 'YOUR_DEEPGRAM_API_KEY' con tu clave de API de Deepgram antes de ejecutar la aplicación
