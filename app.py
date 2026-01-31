import streamlit as st
import joblib
import re
from urllib.parse import urlparse
import pandas as pd

# PAGE CONFIG
st.set_page_config(
    page_title="Phishing URL Detector",
    page_icon="🔐",
    layout="centered"
)

st.title("🔐 Phishing URL Detection System")
st.write("Enter a website URL to check whether it is **Phishing** or **Legitimate**.")

# LOAD MODEL (SAFE)
try:
    model = joblib.load("phishing_model.pkl")
except Exception as e:
    st.error("❌ Failed to load model")
    st.code(str(e))
    st.stop()

# FEATURE EXTRACTION FUNCTIONS
def url_length(url):
    try:
        return len(url)
    except:
        return 0

def has_ip(url):
    try:
        return 1 if re.search(r"\d+\.\d+\.\d+\.\d+", url) else 0
    except:
        return 0

def has_at(url):
    try:
        return 1 if "@" in url else 0
    except:
        return 0

def has_hyphen(url):
    try:
        domain = urlparse(url).netloc
        return 1 if "-" in domain else 0
    except:
        return 0

def dot_count(url):
    try:
        return url.count(".")
    except:
        return 0

def has_https(url):
    try:
        return 1 if url.startswith("https") else 0
    except:
        return 0

def has_www(url):
    try:
        return 1 if "www" in url else 0
    except:
        return 0

def digit_count(url):
    try:
        return sum(char.isdigit() for char in url)
    except:
        return 0

# USER INPUT
url = st.text_input("🔗 Enter Website URL")

# PREDICTION
if st.button("Check URL"):
    if url.strip() == "":
        st.warning("⚠️ Please enter a URL")
    else:
        features = {
            "url_length": url_length(url),
            "has_ip": has_ip(url),
            "has_at": has_at(url),
            "has_hyphen": has_hyphen(url),
            "dot_count": dot_count(url),
            "has_https": has_https(url),
            "has_www": has_www(url),
            "digit_count": digit_count(url)
        }

        df = pd.DataFrame([features])

        prediction = model.predict(df)[0]

        if prediction == 1:
            st.error("🚨 PHISHING WEBSITE DETECTED!")
        else:
            st.success("✅ LEGITIMATE WEBSITE")

# FOOTER
st.markdown("---")
st.caption("Second Year Machine Learning Project | Phishing URL Detection")
