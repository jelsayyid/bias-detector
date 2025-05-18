import streamlit as st
from model_utils import detect_bias

st.title("📰 Israel-Palestine Bias Detector")

article = st.text_area("Paste a news article:", height=300)

if st.button("Analyze"):
    if article.strip():
        result = detect_bias(article)
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