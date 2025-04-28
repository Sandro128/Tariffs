import pandas as pd
import glob
import os
import csv

# Configuration
input_dir = 'data'  
output_file = 'combined_tariff_data.csv'  
file_pattern = os.path.join(input_dir, 'tariff_database_*.txt')

# Get all files sorted by year
files = sorted(glob.glob(file_pattern))

# Columns to keep for your final model
keep_cols = [
    'hts8',
    'brief_description',
    'quantity_1_code',
    'quantity_2_code',
    'mfn_ad_val_rate',
    'mfn_specific_rate',
    'mfn_other_rate',
    'mfn_rate_type_code',
    'wto_binding_code'
]

# Initialize list to store DataFrames
dfs = []

def read_problematic_pipe_file(file_path):
    """Special handler for problematic pipe-delimited files with quote issues"""
    data = []
    with open(file_path, 'r', encoding='latin-1') as f:
        reader = csv.reader(f, delimiter='|', quotechar='"')
        try:
            headers = next(reader)  # Read header row
            for row in reader:
                # Ensure we have the right number of columns
                if len(row) == len(headers):
                    data.append(row)
                elif len(row) > len(headers):
                    # If too many columns, take first n columns matching headers
                    data.append(row[:len(headers)])
                else:
                    # If too few columns, pad with empty strings
                    data.append(row + [''] * (len(headers) - len(row)))
        except Exception as e:
            print(f"Warning: Issue reading {file_path}: {str(e)}")
    
    if data:
        df = pd.DataFrame(data, columns=headers)
        return df
    return None

# Process each file
for file in files:
    try:
        # Extract year from filename
        year = os.path.basename(file).split('_')[2].split('.')[0]
        
        # Check the year and set reading method accordingly
        if int(year) >= 2017:
            # CSV files (2017+)
            try:
                df = pd.read_csv(file, sep=',', encoding='utf-8', dtype=str, engine='python', skip_blank_lines=True)
            except UnicodeDecodeError:
                df = pd.read_csv(file, sep=',', encoding='latin-1', dtype=str, engine='python', skip_blank_lines=True)
        else:
            # Pipe-delimited files (pre-2017)
            # First try standard reading
            try:
                df = pd.read_csv(file, sep='|', encoding='latin-1', dtype=str, engine='python', 
                               quotechar='"', skip_blank_lines=True, error_bad_lines=False)
            except Exception:
                # If standard reading fails, use our special handler
                df = read_problematic_pipe_file(file)
                if df is None:
                    raise ValueError(f"Could not read {file} with either method")
        
        # Keep only the columns that exist in the file
        available_cols = [col for col in keep_cols if col in df.columns]
        df = df[available_cols]
        
        # Drop rows with all NaN values (empty rows)
        df = df.dropna(how='all')
        
        # Add year column
        df['year'] = year
        
        # Check for empty data
        if df.empty:
            print(f"Warning: {file} has no valid data after filtering.")
        else:
            dfs.append(df)
            print(f"Processed {os.path.basename(file)} successfully ({len(df)} rows)")
        
    except Exception as e:
        print(f"Error processing {file}: {str(e)}")
        continue

# Combine all DataFrames
if dfs:
    combined_df = pd.concat(dfs, ignore_index=True)
    
    # Save to CSV
    combined_df.to_csv(output_file, index=False, encoding='utf-8')
    
    # Print summary
    print("\n=== Combination Complete ===")
    print(f"Total files processed: {len(files)}")
    print(f"Total rows in combined file: {len(combined_df)}")
    print(f"Combined data saved to: {output_file}")
    print(f"File size: {os.path.getsize(output_file)/1024/1024:.2f} MB")
else:
    print("No data was processed. Please check your input files.")