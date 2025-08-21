# app.py
import streamlit as st
from transformers import pipeline
from gtts import gTTS
import tempfile
import os

# ------------------------
# Load models (cached)
# ------------------------
@st.cache_resource
def load_models():
    caption_model = pipeline("image-to-text", model="Salesforce/blip-image-captioning-base")
    story_model = pipeline("text2text-generation", model="google/flan-t5-large")
    return caption_model, story_model

caption_model, story_model = load_models()

# ------------------------
# Page config and style
# ------------------------
st.set_page_config(page_title="Image to Story", layout="wide")

st.markdown("""
    <style>
    .main {
        background-color: #F0F8FF; 
        padding: 20px;
    }
    .box {
        background-color: #ffffff; 
        padding: 15px; 
        border-radius: 10px; 
        box-shadow: 2px 2px 10px #d3d3d3;
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🖼️ Image to Story Generator")
st.markdown("Upload an image, generate a story, and listen to it!")

# ------------------------
# Upload Image
# ------------------------
uploaded_file = st.file_uploader("Choose an image", type=["png", "jpg", "jpeg"])

if uploaded_file:
    st.image(uploaded_file, caption="Uploaded Image", use_container_width=True)
    
    # ------------------------
    # Generate Caption
    # ------------------------
    with st.spinner("Generating caption..."):
        caption_result = caption_model(uploaded_file)
        caption_text = caption_result[0]['generated_text']
    st.markdown(f"<div class='box'><b>Caption:</b> {caption_text}</div>", unsafe_allow_html=True)
    
    # ------------------------
    # Generate Story
    # ------------------------
    with st.spinner("Generating story..."):
        story_result = story_model(
            caption_text, 
            max_new_tokens=500, 
            do_sample=True, 
            temperature=0.7
        )
        story_text = story_result[0]['generated_text']
    st.markdown(f"<div class='box'><b>Story:</b> {story_text}</div>", unsafe_allow_html=True)
    
    # ------------------------
    # Convert Story to Audio
    # ------------------------
    tts = gTTS(text=story_text, lang='en')
    tmp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
    tts.save(tmp_file.name)
    
    st.audio(tmp_file.name, format='audio/mp3')
    
    # Optional: delete temp file on exit
    def remove_temp_file(path):
        try:
            os.remove(path)
        except:
            pass
    st.button("Clear Audio", on_click=remove_temp_file, args=(tmp_file.name,))
