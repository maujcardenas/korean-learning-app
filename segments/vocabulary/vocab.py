import streamlit as st
import pandas as pd
import os
import tools.utils as ut  

korean_base_url = st.secrets['korean_app_base_url']

df = ut.load_working_vocab_df()

st.title("Vocabulary Explorer")

st.markdown('This app has 658 basic korean words for the following categories and sub-categories:')
unique_categories_df = df[['category', 'sub-category']].drop_duplicates()
st.dataframe(unique_categories_df, use_container_width=False, hide_index=True)

categories = df['category'].unique()
selected_category = st.selectbox("Select Category", categories)

subcategories = df[df['category'] == selected_category]['sub-category'].unique()
selected_subcategory = st.selectbox("Select Subcategory", subcategories)

filtered_df = df[
    (df['category'] == selected_category) & 
    (df['sub-category'] == selected_subcategory)
]

display_df = filtered_df[['word', 'type', 'example']]
st.dataframe(display_df, hide_index=True, use_container_width=False)

st.markdown("---")
st.header("Words in Detail")

for _, row in filtered_df.iterrows():
    word = row['word'].strip()
    word_for_path = word.replace("/","_")
    example_sentence = row['example'].strip()
    subcategory = row['sub-category'].strip()
    
    word_audio = f'{korean_base_url}/korean_audio/{subcategory}-{word_for_path}.mp3'
    example_audio = f'{korean_base_url}/korean_audio/{subcategory}-{word_for_path}-example-sentence.mp3'

    col1, col2 = st.columns([1, 3])
    with col1:
        st.markdown(f'#### {word}')
        st.audio(word_audio)
    with col2:
        st.markdown(f'#### {example_sentence}')
        st.audio(example_audio)