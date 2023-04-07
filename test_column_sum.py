import pandas as pd

# Load the Excel file
df = pd.read_excel("SampleWork.xlsx")


# Get the column names
column_names = df.columns

# Print the column names
print(column_names)


# Add a new column with the sum of two columns
df["new_column"] = df["ЭМД, НДШ Дүн"] + df["Татвар ногдуулах орлого"]

# Save the updated Excel file
df.to_excel("SampleWork.xlsx", index=False)