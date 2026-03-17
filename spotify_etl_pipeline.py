import pandas as pd #Importing pandas for data manipulation and analysis
import os           #Importing os to check for file existence

print("Starting Spotify ETL Pipeline...")

file_path = "Top_Tracks_of_2025_Global.csv" # Load the raw dataset

# Safety check: ensure the file exists before running the rest of the code

if not os.path.exists(file_path):
    print(f"ERROR: Could not find {file_path}. Make sure it is in the same folder as this script.")
    exit()

df = pd.read_csv(file_path) # Load the dataset into a pandas DataFrame
print(f"Raw Data Loaded: {df.shape[0]} rows and {df.shape[1]} columns.") # Print the shape of the DataFrame to confirm successful loading

# Drop useless columns 

print("Cleaning data...")
columns_to_drop = ['Added By', 'Track URI']
df_cleaned = df.drop(columns=columns_to_drop, errors='ignore') # We use errors='ignore' just in case the columns are already dropped

#Handle Missing Genres

if 'Genres' in df_cleaned.columns:
    df_cleaned['Genres'] = df_cleaned['Genres'].fillna('Unknown') #Fill blank genres with 'Unknown' so Power BI doesn't show blank visuals

#Convert Duration from Milliseconds to Minutes

if 'Duration (ms)' in df_cleaned.columns:
    df_cleaned['Duration (mins)'] = round(df_cleaned['Duration (ms)'] / 60000, 2) 
    df_cleaned = df_cleaned.drop(columns=['Duration (ms)']) # Drop the original duration column since we now have it in minutes, which is more user-friendly for Power BI visuals

# Standardize the Date Format

if 'Release Date' in df_cleaned.columns:
    df_cleaned['Release Date'] = pd.to_datetime(df_cleaned['Release Date'], errors='coerce') # Convert to datetime, coercing errors to NaT

# Export the Cleaned Data

output_filename = "Cleaned_Spotify_Data_2025.csv"
df_cleaned.to_csv(output_filename, index=False) # Save the cleaned DataFrame to a new CSV file without the index

print(f"SUCCESS! Data has been cleaned and saved as '{output_filename}'.")