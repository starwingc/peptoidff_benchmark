# Storing all the data processed as .csv or .json 

### Unprocessed Data 

#### peptoids.json: 
data sparcing from 'http://127.0.0.1:5000/api/peptoids'

#### residues.json: 
data sparcing from 'http://127.0.0.1:5000/api/residues'

#### peptoids.csv: 
peptoids info from peptoid data bank

#### residues.csv: 
residues info from peptoid data bank 

### Processed Data
#### sequences.csv: 
NMR Solution peptoids and their full nomenclature name residue 

#### smiles.csv: 
NMR Solution peptoids and the residues uncapped SMILE 

#### capped_smiles.csv: 
replace the * in smile.csv into the 'CC(=O)' and 'N(C)C' caps

#### codes_unedited.csv: 
All resideus in Peptoid Data bank and their short name 

#### codes.csv: 
All residues and their assigned short name artificially 

#### short_name.csv: 
NMR Solution peptoids and their short name residue 
