import csv
import re

urls = [
    ("http://paypal-login.com", 1),
    ("https://google.com", 0),
    ("http://192.168.1.1/login", 1),
    ("https://amazon.in", 0),
    ("http://free-offer@win.com", 1)
]

with open("generated_dataset.csv", "w", newline="") as file:

    writer = csv.writer(file)
    writer.writerow(["length","has_ip","has_https","has_at","has_dash","label"])

    for url, label in urls:
        length = len(url)
        has_ip = 1 if re.search(r"\d+\.\d+\.\d+\.\d+", url) else 0
        has_https = 1 if url.startswith("https") else 0
        has_at = 1 if "@" in url else 0
        has_dash = 1 if "-" in url else 0

        writer.writerow([length,has_ip,has_https,has_at,has_dash,label])

print("✅ Dataset created automatically")
