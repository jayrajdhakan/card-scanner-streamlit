import streamlit as st
import easyocr
import numpy as np
from PIL import Image
import urllib.parse

st.set_page_config(page_title="Business Card to WhatsApp")

st.title("📇 Business Card Scanner")

# Session state
if "front_key" not in st.session_state:
    st.session_state.front_key = 0

if "back_key" not in st.session_state:
    st.session_state.back_key = 0


reader = easyocr.Reader(['en', 'hi'], gpu=False)

def extract_text(image):
    img = np.array(image)
    result = reader.readtext(img, detail=0)
    return "\n".join(result)


# Upload images
front_image = st.file_uploader(
    "Upload Front Image",
    type=["jpg", "jpeg", "png"],
    key=f"front_{st.session_state.front_key}"
)

back_image = st.file_uploader(
    "Upload Back Image",
    type=["jpg", "jpeg", "png"],
    key=f"back_{st.session_state.back_key}"
)

extracted_text = ""

# Process front image
if front_image:
    img = Image.open(front_image)
    extracted_text += extract_text(img)

# Process back image
if back_image:
    img2 = Image.open(back_image)
    extracted_text += "\n" + extract_text(img2)

# Show extracted text with built-in copy button
if extracted_text:
    st.subheader("Extracted Text")
    st.code(extracted_text, language="text")

    st.subheader("Share")

    encoded_text = urllib.parse.quote(extracted_text)
    whatsapp_link = f"https://wa.me/?text={encoded_text}"

    st.link_button("📲 Share on WhatsApp", whatsapp_link)

