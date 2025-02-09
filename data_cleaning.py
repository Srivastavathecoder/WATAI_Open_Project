import pandas as pd

# Load data and skip first row
df = pd.read_csv("stocks.csv", skiprows=1)

# Using first row as column headers instead
df.columns = df.iloc[0]
df = df[2:].reset_index(drop=True)

# Renaming first column to date
df = df.rename(columns = {df.columns[0]: "Date"})

# Deleting rows if they are missing a date
df = df.dropna(subset=["Date"])

# Make sure no extra spaces
df.columns = df.columns.str.strip()

# Identify OHLCV columns
ohlcv_columns = [col for col in df.columns if col not in ["Date"]]

# Convert OHLCV columns to numeric
for col in ohlcv_columns:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Delete any other missing values
df = df.dropna().reset_index(drop=True)

# Save
df.to_csv("cleaned_stocks.csv", index=False)
print("Data cleaning done")