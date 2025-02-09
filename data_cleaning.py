import pandas as pd

# Load data and skip first row
df = pd.read_csv("stocks.csv", skiprows=1, header=None)

# Naming columns
column_names = ["Date", "QQQ_Close", "SPY_Close", "XIU_Close", 
                "QQQ_High", "SPY_High", "XIU_High", 
                "QQQ_Low", "SPY_Low", "XIU_Low", 
                "QQQ_Open", "SPY_Open", "XIU_Open", 
                "QQQ_Volume", "SPY_Volume", "XIU_Volume"]
df.columns = column_names

# Reset index
df = df[1:].reset_index(drop=True)  

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