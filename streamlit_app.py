import streamlit as st
from deepgram import Deepgram
import json

st.title('Transcriptor de Audio')

DEEPGRAM_API_KEY = '887355a9368a2b55cbb723a9b735af03f618ed6c'

@st.cache
def get_deepgram_client():
  return Deepgram(DEEPGRAM_API_KEY)

audio_file = st.file_uploader("Sube un archivo M4A", type=['m4a'])

if audio_file is not None:

  dg_client = get_deepgram_client()

  audio_bytes = audio_file.read()

  try:
    response = dg_client.transcription.sync_prerecorded(
      {'buffer': audio_bytes, 'mimetype': audio_file.type},
      {
        'language': 'es-ES',
        'smart_format': True  
      }
    )
  except Exception as e:
    st.error(f"Error al transcribir el audio: {e}")
    st.stop()

  st.write("Transcripción:")
  st.write(response['results']['channels'][0]['alternatives'][0]['transcript'])

  st.json(response)

else:
  st.write("Sube un archivo M4A para comenzar") 
