import streamlit as st
from dotenv import load_dotenv
import os
from google.generativeai import GenerativeModel
from youtube_transcript_api import YouTubeTranscriptApi

# Load environment variables
load_dotenv()

# Configure the Generative AI API key
genai_api_key = os.getenv('Google_api_key')

# Check if the API key is loaded
if genai_api_key is None:
    st.error("Google API key not found. Please check your .env file.")
else:
    GenerativeModel.configure(api_key=genai_api_key)

# Define the prompt for the summarizer
prompt = '''You are a YouTube video summarizer. You will be taking the transcript text
and summarizing the entire video and providing the important summary in points
within 250 words. The transcript text will be appended here: '''

def generate_gemini_content(transcript_text, prompt):
    model = GenerativeModel('gemini-pro')
    response = model.generate_content(prompt + transcript_text)
    return response['text']

def extract_transcript_details(youtube_video_url):
    try:
        video_id = youtube_video_url.split('=')[1]
        transcript_text = YouTubeTranscriptApi.get_transcript(video_id)

        transcript = ''
        for i in transcript_text:
            transcript += ' ' + i['text']

        return transcript
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return None

st.title('YouTube Transcript to Detailed Notes Converter')
youtube_link = st.text_input('Enter YouTube video Link:')

if youtube_link:
    try:
        video_id = youtube_link.split('=')[1]
        st.image(f'http://img.youtube.com/vi/{video_id}/0.jpg', use_column_width=True)
    except IndexError:
        st.error("Invalid YouTube URL format. Please enter a valid URL.")

if st.button('Get Detailed Notes'):
    transcript_text = extract_transcript_details(youtube_link)

    if transcript_text:
        summary = generate_gemini_content(transcript_text, prompt)
        st.markdown('## Detailed Notes:')
        st.write(summary)
    else:
        st.error("Failed to retrieve transcript.")
