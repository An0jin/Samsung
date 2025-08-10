import pandas as pd

# Read the Excel file
file_path = 'SamSung.xlsx'
df = pd.read_excel(file_path)

# Check the '전일비' column for duplicates
print("Before processing:")
print(df['전일비'].head())

# Remove consecutive duplicates in the '전일비' column
df['전일비'] = df['전일비'].mask(df['전일비'].shift() == df['전일비'])

# Fill any NaN values with the previous value (only for the first row if it's NaN)
df['전일비'] = df['전일비'].fillna(method='ffill')

print("\nAfter processing:")
print(df['전일비'].head())

# Save the modified data back to Excel
df.to_excel(file_path, index=False)
print(f"\nFile '{file_path}' has been updated successfully.")
