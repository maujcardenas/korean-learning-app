from gtts import gTTS
import streamlit as st
import os
from io import BytesIO
import pandas as pd

base_url=st.secrets['korean_app_base_url']

def text_to_speech(text, lang='en'):
    tts = gTTS(text=text, lang=lang, slow=False)    
    audio_bytes = BytesIO()
    tts.write_to_fp(audio_bytes)
    audio_bytes.seek(0)
    
    return audio_bytes

def load_working_vocab_df():
    data_url=f'{base_url}/data/korean-vocab.csv'
    df= pd.read_csv(data_url,
                    sep=',', skiprows=1, 
                    names=['category','sub-category', 'word', 'type', 'example'], 
                    encoding="utf-8", engine='python', quotechar='"', doublequote=True)
    return df
