import streamlit as st
import asyncio
import json
from deepgram import Deepgram

# Tu clave API de Deepgram 
DEEPGRAM_API_KEY = '887355a9368a2b55cbb723a9b735af03f618ed6c'  


# Ruta al archivo M4A local
FILE = 'ruta/a/tu/archivo.m4a'  

async def main():

  deepgram = Deepgram(DEEPGRAM_API_KEY)

  # Abrir el archivo en modo bytes para lectura binaria
  with open(FILE, 'rb') as audio: 
    source = {
      'buffer': audio,
      'mimetype': 'audio/mp4' # Mimetype para M4A
    }

  response = await deepgram.transcription.prerecorded(
    source,
    {
      'language': 'es-ES',  
      'sample_rate': 44100, # Estándar para archivos M4A
      'model': 'nova'
    }
  )

  print(json.dumps(response, indent=4))
 
asyncio.run(main())
