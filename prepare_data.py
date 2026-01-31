import pandas as pd

# Load dataset
df = pd.read_csv("urldata.csv")

# Drop unwanted column
df = df.drop(columns=["Unnamed: 0"])

# Check again
print(df.head())
print(df['result'].value_counts())

# Save clean dataset
df.to_csv("clean_urldata.csv", index=False)

print("✅ Clean dataset saved as clean_urldata.csv")
