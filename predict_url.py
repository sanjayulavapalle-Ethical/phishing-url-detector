import joblib
import re
from urllib.parse import urlparse
import pandas as pd

# Load trained model
model = joblib.load("phishing_model.pkl")

# =========================
# FEATURE FUNCTIONS (SAME AS TRAINING)
# =========================

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

# =========================
# PREDICTION FUNCTION
# =========================

def predict_url(url):
    data = {
        'url_length': url_length(url),
        'has_ip': has_ip(url),
        'has_at': has_at(url),
        'has_hyphen': has_hyphen(url),
        'dot_count': dot_count(url),
        'has_https': has_https(url),
        'has_www': has_www(url),
        'digit_count': digit_count(url)
    }

    df = pd.DataFrame([data])
    prediction = model.predict(df)[0]

    if prediction == 1:
        print("\n🚨 PHISHING WEBSITE DETECTED!")
    else:
        print("\n✅ LEGITIMATE WEBSITE")

# =========================
# USER INPUT
# =========================

url = input("🔗 Enter a URL to check: ")
predict_url(url)
