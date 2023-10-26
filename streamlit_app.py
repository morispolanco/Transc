import streamlit as st
from deepgram import Deepgram
import asyncio
import aiohttp

st.title('Transcripción de audio en vivo')

# Tu clave API de Deepgram 
DEEPGRAM_API_KEY = '887355a9368a2b55cbb723a9b735af03f618ed6c'
 

# URL del audio en vivo a transcribir
URL = 'http://stream.live.vc.bbcmedia.co.uk/bbc_world_service'  

async def transcribe():
    deepgram = Deepgram(DEEPGRAM_API_KEY)
    
    try:
        deepgram_live = await deepgram.transcription.live({
          'smart_format': True,
          'interim_results': False,
          'language': 'es',
          'model': 'nova',
        })
    except Exception as e:
        st.error(f'Error al abrir socket: {e}')
        return

    deepgram_live.registerHandler(deepgram_live.event.TRANSCRIPT_RECEIVED, show_transcript)
    
    async with aiohttp.ClientSession() as session:
        async with session.get(URL) as audio:
            while True:
                data = await audio.content.readany()
                deepgram_live.send(data)
                
                if not data:
                    break
                    
    await deepgram_live.finish()
    
def show_transcript(transcript):
    st.write(transcript.channel.alternatives[0].transcript)
    
asyncio.run(transcribe())
