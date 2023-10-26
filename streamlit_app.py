import streamlit as st
import sounddevice as sd 
from deepgram import Deepgram
import asyncio
import time

st.title('Transcripción de voz en vivo')

# Tu clave API de Deepgram 
DEEPGRAM_API_KEY = '887355a9368a2b55cbb723a9b735af03f618ed6c'  


# ID del micrófono a usar
mic_id = 1  

async def transcribe():
    deepgram = Deepgram(DEEPGRAM_API_KEY)
    
    try:
        deepgram_live = await deepgram.transcription.live({
          'smart_format': True,
          'interim_results': False,
          'language': 'es-ES',
          'sample_rate': 44100,
          'channels': 1,
          'model': 'nova',
        })
    except Exception as e:
        st.error(f'Error al abrir socket: {e}')
        return

    deepgram_live.registerHandler(deepgram_live.event.TRANSCRIPT_RECEIVED, show_transcript)

    with sd.RawInputStream(samplerate=44100, blocksize = 8000, device=mic_id, dtype='int16', 
                        channels=1, callback=get_audio):
        st.write('#' * 80)
        st.write('Habla ahora para transcribir tu voz')
        st.write('#' * 80)

        while True:
            time.sleep(0.1)    

    await deepgram_live.finish()

def get_audio(indata, frames, time, status):
  deepgram_live.send(indata.tobytes())

def show_transcript(transcript):
    try:
        text = transcript['channel']['alternatives'][0]['transcript']
        st.write(text)
    except:
        st.warning('No se pudo acceder al texto transcripto')

asyncio.run(transcribe())  
