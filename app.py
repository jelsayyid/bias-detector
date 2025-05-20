import streamlit as st
import re
from model_utils import detect_bias
from charged_terms import CHARGED_TERMS
from PIL import Image
import os

# Load and display PDLI banner group photo
img_path = os.path.join("assets", "PDLI.jpg")
if os.path.exists(img_path):
    img = Image.open(img_path)
    st.image(img, caption="A PDLI Project, by Joseph Elsayyid", use_container_width=True)

st.title("📰 AI-Powered Israel-Palestine Bias Detector")

article = st.text_area("Paste a news article:", height=300)

if st.button("Analyze"):
    if article.strip():
        result = detect_bias(article)
        # --- NEW: highlight charged terms ---
        highlighted = article
        for term in CHARGED_TERMS:
            # wrap each occurrence in a yellow span
            highlighted = re.sub(
                rf"\b({re.escape(term)})\b",
                r'<span style="background-color: yellow; font-weight:bold;">\1</span>',
                highlighted,
                flags=re.IGNORECASE
            )

        st.markdown("**Highlighted biased terms:**")
        st.markdown(highlighted, unsafe_allow_html=True)
        # --- end highlight block ---
        st.markdown(f"**Top prediction:** {result['labels'][0]}")
        st.markdown("**Scores:**")
        for label, score in zip(result['labels'], result['scores']):
            st.write(f"- {label}: {score:.2f}")
    else:
        st.warning("Please paste some text above.")

# This is a simple Streamlit app that uses the detect_bias function from model_utils.py
# to analyze the bias in a news article. The user can paste an article into a text area, 
# and when they click the "Analyze" button, the app will display the top prediction and
# the scores for each label. The app also includes a title and a warning message if the
# user tries to analyze an empty article.