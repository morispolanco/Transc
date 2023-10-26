import streamlit as st
import asyncio
import aiohttp
from deepgram import Deepgram

# Título de la aplicación
st.title("Transcripción de Audio en Tiempo Real")

# Your Deepgram API Key
DEEPGRAM_API_KEY = '887355a9368a2b55cbb723a9b735af03f618ed6c'

# URL para el audio en tiempo real que deseas transcribir
URL = 'http://stream.live.vc.bbcmedia.co.uk/bbc_world_service'

async def transcribe_audio():
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

        # Escuchar los resultados de la transcripción y mostrarlos en la aplicación
        async for transcript in deepgramLive:
            st.write("Transcripción en tiempo real:")
            st.write(transcript)

        # Indicar que hemos terminado de enviar datos enviando un mensaje de cero bytes al punto final de transmisión de Deepgram y esperar hasta que recibamos el objeto de metadatos final
        await deepgramLive.finish()

    except Exception as e:
        st.write(f'No se pudo abrir el socket: {e}')

# Iniciar la transcripción de audio
if st.button("Iniciar Transcripción de Audio"):
    st.write("Transcripción en tiempo real iniciada. Habla para comenzar.")

    # Iniciar la transcripción en segundo plano
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(transcribe_audio())

    st.write("Transcripción en tiempo real finalizada.")

# Detener la transcripción de audio
if st.button("Detener Transcripción de Audio"):
    st.write("Transcripción en tiempo real detenida.")

# Si ejecutas la aplicación de Streamlit en una celda de Jupyter Notebook, utiliza await main() en lugar de ejecutarla con asyncio.run(main())
