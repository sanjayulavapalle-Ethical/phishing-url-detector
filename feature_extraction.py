import re
from urllib.parse import urlparse
import numpy as np

# =========================
# FEATURE FUNCTIONS
# =========================

def url_length(url):
    return len(url)

def has_ip(url):
    return 1 if re.search(r"\d+\.\d+\.\d+\.\d+", url) else 0

def has_at(url):
    return 1 if "@" in url else 0

def has_hyphen(url):
    domain = urlparse(url).netloc
    return 1 if "-" in domain else 0

def dot_count(url):
    return url.count(".")

def has_https(url):
    return 1 if url.startswith("https") else 0

def has_www(url):
    return 1 if "www" in url else 0

def digit_count(url):
    return sum(char.isdigit() for char in url)

# =========================
# MAIN FUNCTION (IMPORTANT)
# =========================

def extract_features(url):
    features = [
        url_length(url),
        has_ip(url),
        has_at(url),
        has_hyphen(url),
        dot_count(url),
        has_https(url),
        has_www(url),
        digit_count(url)
    ]

    return np.array(features).reshape(1, -1)
