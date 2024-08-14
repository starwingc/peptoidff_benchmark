import csv
import os
from chimerax.core.session import Session
from chimerax.core.commands import run

# Change directory to the specified path
os.chdir('/Users/starwingchen/Voelz_Lab/git/peptoid_24summer')

# Open the CSV file and read its contents
with open('data/codes.csv', mode='r') as file:
    csv_reader = csv.DictReader(file)
    
    # Iterate over each row in the CSV
    for i, row in enumerate(csv_reader):
        smile = row['SMILES']
        clean_smile = smile.replace('*', '')
        n_terminal = f"{clean_smile}N(C)C"
        c_terminal = f"CC(=O){clean_smile}"
        short_name = row['short_name']

        # Create paths
        n_terminal_mol2_path = f"residues/GAFF/N_terminal/unmodified/N{short_name}/"
        c_terminal_mol2_path = f"residues/GAFF/C_terminal/unmodified/C{short_name}/"
        os.makedirs(n_terminal_mol2_path, exist_ok=True)
        os.makedirs(c_terminal_mol2_path, exist_ok=True)

        # Run commands for N-terminal
        try:
            run(session, f"open smiles:{n_terminal} resName {short_name}")
            run(session, f"save {n_terminal_mol2_path}{short_name}.mol2 format mol2")
            run(session, "close all")
        except Exception as e:
            print(f"Error processing N-terminal {n_terminal}: {e}")

        # Run commands for C-terminal
        try:
            run(session, f"open smiles:{c_terminal} resName {short_name}")
            run(session, f"save {c_terminal_mol2_path}{short_name}.mol2 format mol2")
            run(session, "close all")
        except Exception as e:
            print(f"Error processing C-terminal {c_terminal}: {e}")
