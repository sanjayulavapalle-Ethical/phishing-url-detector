import pandas as pd
import re
from urllib.parse import urlparse

# Load dataset
df = pd.read_csv("clean_urldata.csv")

# =========================
# FEATURE FUNCTIONS (SAFE)
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
# APPLY FEATURES
# =========================

df['url_length'] = df['url'].apply(url_length)
df['has_ip'] = df['url'].apply(has_ip)
df['has_at'] = df['url'].apply(has_at)
df['has_hyphen'] = df['url'].apply(has_hyphen)
df['dot_count'] = df['url'].apply(dot_count)
df['has_https'] = df['url'].apply(has_https)
df['has_www'] = df['url'].apply(has_www)
df['digit_count'] = df['url'].apply(digit_count)

# =========================
# FINAL CLEANUP
# =========================

# Keep only numeric features + target
df = df.drop(columns=['url', 'label'])

# Save final dataset
df.to_csv("features.csv", index=False)

print("✅ FEATURE EXTRACTION COMPLETED SUCCESSFULLY")
print(df.head())
