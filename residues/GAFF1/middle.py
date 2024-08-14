from chimerax.core.session import Session
from chimerax.core.commands import run
import csv
import os

#modify it to your own path
os.chdir('/Users/starwingchen/Voelz_Lab/git/peptoid_24summer')

with open('data/codes.csv', mode='r') as file:
    csv_reader = csv.DictReader(file)
    
    # Iterate over each row in the CSV
    for i, row in enumerate(csv_reader):
        smile = row['SMILES']
        clean_smile = smile.replace('*','')
        capped_smile = f"CC(=O){clean_smile}N(C)C"
        short_name = row['short_name']

        #create path 
        mol2_path = f"residues/GAFF/uncapped/unmodified/{short_name}/"
        os.makedirs(os.path.dirname(mol2_path), exist_ok=True)
        
        #run command
        try:
            run(session, f"open smiles:{capped_smile} resName {short_name}")
            #print(f"open smiles:{smiles} resName {code}")
            run(session, f"save {mol2_path}{short_name}.mol2 format mol2")
            #print(f"save residues/{code}.mol2 format mol2")
            run(session, "close all")
        except Exception as e:
            print(f"Error processing {capped_smile}: {e}")
