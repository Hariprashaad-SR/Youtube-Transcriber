import streamlit as st
from gemini import GenerateSummary
from transcribe import Transcribe
from logger import logging
from title import get_channel_name
from utils import style, generate_report
from exception import CustomException
import sys

# Page config and input
st.set_page_config(page_title = 'Youtube Transcriber', page_icon = 'YOUTUBE')
st.title('Youtube Transcriber')

st.markdown(style,unsafe_allow_html=True)
st.markdown('<div class="footer"><sub>Application by Hariprashaad-SR</sub></div>', unsafe_allow_html=True)

url = st.text_input('Enter a youtube url')

# Center panel
if url:
    try:
        custom_prompt = None
        transcribe = Transcribe(url = url)
        video_id, transcribe_text = transcribe.InitiateTranscribe()

        with st.container():
            st.sidebar.title('Settings')

            # Custom Prompt
            custom_prompt_check= st.sidebar.checkbox('Custom_Prompt')
            if custom_prompt_check:
                custom_prompt = st.sidebar.text_input('Write your custom prompt here')
            
            st.sidebar.write('---')

            channel_name, title = get_channel_name(url = url)
            st.sidebar.write(f'Channel : {channel_name}')

            st.sidebar.image(f"http://img.youtube.com/vi/{video_id}/0.jpg", use_column_width=True)

            st.sidebar.write(title)
            
            generate = st.button('Generate summary')
        
            if generate:
                with st.spinner('Transcribing your video'):
                    model = GenerateSummary(transcript = transcribe_text, prompt= custom_prompt)
                    summary = model.summarise()

                    st.write(summary)
                    
                    report = generate_report(channel_name = channel_name, title = title, summary = summary, image_url = f"http://img.youtube.com/vi/{video_id}/0.jpg")
                 
                    st.sidebar.download_button(
                        label="Download Report",
                        data=open("Assets/report.pdf", "rb").read(),
                        file_name="report.pdf",
                        mime="application/pdf"
                    )
            

    except Exception as e:
        st.error('Please enter a valid youtube url or check whether the video has enabled the cc')
        raise CustomException(e, sys)