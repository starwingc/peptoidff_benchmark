from chimerax.core.session import Session
from chimerax.core.commands import run
import csv
import os

os.chdir('/Users/starwingchen/Voelz_Lab/git/peptoid_24summer')

with open('data/codes.csv', mode='r') as file:
    csv_reader = csv.DictReader(file)
    
    # Iterate over each row in the CSV
    for i, row in enumerate(csv_reader):
        smiles = row['Capped_SMILES']
        code = row['Code']

        #run command
        try:
            run(session, f"open smiles:{smiles} resName {code}")
            #print(f"open smiles:{smiles} resName {code}")
            run(session, f"save residues/{code}.mol2 format mol2")
            #print(f"save residues/{code}.mol2 format mol2")
            run(session, "close all")
        except Exception as e:
            print(f"Error processing {smiles}: {e}")
