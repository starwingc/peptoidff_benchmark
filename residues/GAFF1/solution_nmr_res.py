import pandas as pd
import subprocess
import os

# Set the working directory
os.chdir('/Users/starwingchen/Voelz_Lab/git/peptoid_24summer/')

# Load the DataFrame from the CSV file
short_name_csv = 'data/short_names.csv'
df_short_name = pd.read_csv(short_name_csv)
print("DataFrame loaded successfully")
print(df_short_name.head())  # Print the first few rows to verify

# Change to the specified directory
os.chdir('/Users/starwingchen/Voelz_Lab/git/peptoid_24summer/residues/GAFF/')
print("Changed directory to /Users/starwingchen/Voelz_Lab/git/peptoid_24summer/residues/GAFF/")

# Initialize an empty set to keep track of encountered short names
encountered = set()

# Iterate over the rows of the DataFrame
for i, r in df_short_name.iterrows():
    # Iterate over the short names in each row
    for short_name in r:
        if short_name not in encountered:
            if short_name is not None:
                encountered.add(short_name)
                command = f"cp -r unmodified/{short_name} modified/{short_name}"
                print(f"Executing command: {command}")
                # Execute the command
                try:
                    subprocess.run(command, shell=True, check=True)
                except subprocess.CalledProcessError as e:
                    print(f"Failed to execute command: {command}")
                    print(e)
                