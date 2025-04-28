import pandas as pd

# Load your original data
df = pd.read_csv('combined_tariff_data.csv')

# Define your classes (all lowercase for case-insensitive matching)
classes = {
    'cotton': ['cotton'],
    'wool': ['wool'],
    'rubber': ['rubber'],
    'steel': ['steel'],
    'fibers': ['fiber', 'fibre', 'fibers', 'fibres'],
    'fabrics': ['fabric', 'fabrics'],
    'metal': ['metal'],
    'textile': ['textile'],
    'cheese': ['cheese'],
    'yarn': ['yarn'],
    'silk': ['silk'],
    'leather': ['leather'],
    'sugar': ['sugar'],
    'salts': ['salt', 'salts'],
    'iron': ['iron'],
    'milk': ['milk']
}

# Function to find which class a description belongs to
def find_class(description):
    description = str(description).lower()
    for class_name, keywords in classes.items():
        for keyword in keywords:
            if keyword in description:
                return class_name
    return None

# Apply the classification
df['class'] = df['brief_description'].apply(find_class)

# Keep only rows that were classified
classified_df = df.dropna(subset=['class'])

# Save to new CSV file
classified_df.to_csv('classified_tariff_data.csv', index=False)

# Print summary
print(f"Original rows: {len(df)}")
print(f"Classified rows: {len(classified_df)}")
print("Classification counts:")
print(classified_df['class'].value_counts())