import streamlit as st
import joblib
import time
import numpy as np
from feature_extraction import extract_features

# ================= PAGE CONFIG =================
st.set_page_config(
    page_title="Phishing URL Detector",
    page_icon="🔐",
    layout="centered"
)

# ================= CUSTOM STYLE =================
st.markdown("""
<style>
body {background-color: #0f172a;}
.main-title {
    text-align:center;
    font-size:40px;
    font-weight:700;
    color:#22c55e;
}
.sub-text {
    text-align:center;
    color:#94a3b8;
    margin-bottom:25px;
}
.result-safe {
    padding:20px;
    border-radius:12px;
    background-color:#052e16;
    color:#4ade80;
    font-size:22px;
    text-align:center;
}
.result-phish {
    padding:20px;
    border-radius:12px;
    background-color:#3f0000;
    color:#f87171;
    font-size:22px;
    text-align:center;
}
</style>
""", unsafe_allow_html=True)

# ================= TITLE =================
st.markdown('<p class="main-title">🔐 Phishing URL Detection System</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-text">Machine Learning based real‑time website safety analyzer</p>', unsafe_allow_html=True)

# ================= LOAD MODEL =================
@st.cache_resource
def load_model():
    return joblib.load("phishing_model.pkl")

try:
    model = load_model()
except Exception as e:
    st.error("Model loading failed")
    st.code(str(e))
    st.stop()

# ================= INPUT =================
url = st.text_input("🔗 Enter Website URL", placeholder="https://example.com/login")

# ================= ANALYSIS =================
if st.button("Analyze Website"):
    if url.strip() == "":
        st.warning("Please enter a valid URL")
    else:
        with st.spinner("Scanning website using AI model..."):
            time.sleep(1.5)
            features = extract_features(url)
            prediction = model.predict(features)[0]
            prob = model.predict_proba(features)[0][1]

        # Risk meter
        st.subheader("Risk Score")
        st.progress(int(prob * 100))
        st.metric("Phishing Probability", f"{prob*100:.2f}%")

        # Result box
        if prediction == 1:
            st.markdown('<div class="result-phish">🚨 Warning: Phishing Website Detected</div>', unsafe_allow_html=True)
        else:
            st.markdown('<div class="result-safe">✅ This Website Appears Legitimate</div>', unsafe_allow_html=True)

# ================= FOOTER =================
st.markdown("---")
st.caption("Developed by Sanjay | Machine Learning Cybersecurity Project")
