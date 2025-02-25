# you just need to run the file

import pandas as pd

# Load the CSV
df = pd.read_csv("data.csv")

# Remove unnecessary column
df = df.drop(columns=["Unnamed: 0"], errors='ignore')

# Clean financial values function
def clean_financial_values(value):
    if isinstance(value, str):
        value = value.replace("$", "").replace(",", "").strip()
        if "B" in value:
            return float(value.replace("B", "")) * 1e9  # Convert billions
        elif "M" in value:
            return float(value.replace("M", "")) * 1e6  # Convert millions
    return float(value)

# Apply the cleaning function to financial columns
df["Sales"] = df["Sales"].apply(clean_financial_values)
df["Profit"] = df["Profit"].apply(clean_financial_values)
df["Assets"] = df["Assets"].apply(clean_financial_values)
df["Market Value"] = df["Market Value"].apply(clean_financial_values)

# Deduplicate companies and countries
df = df.drop_duplicates(subset=["Name", "Country"])

# Save the modified DataFrame to a new CSV
df.to_csv("processed_data.csv", index=False)

print("Processed data saved successfully to 'processed_data.csv'!")
