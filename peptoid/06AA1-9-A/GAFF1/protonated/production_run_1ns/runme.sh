#!/bin/bash

# Load GROMACS module
# module load gromacs/2021.2
# replace the name in text file
# sed 's/06AA1-9-A/06AA1-9-A/g' runme.sh > runme_temp.sh && mv runme_temp.sh runme.sh

# make an peptoid.itp file 
cp 06AA1-9-A_GMX.top 06AA1-9-A.itp    
# make sure to command out the [default] and the [systems] [molecules] section

#make a new top file 
cat >> 06AA1-9-A.top  <<EOL
; Include force field parameters
#include "/usr/local/gromacs/share/gromacs/top/amber99.ff/forcefield.itp"

; Include Peptoid
#include "./06AA1-9-A.itp"

[ system ]
 06AA1-9-A

[ molecules ]
; Compound        nmols
 06AA1-9-A        1 

EOL


# Add a box
gmx editconf -f 06AA1-9-A_GMX.gro -o 06AA1-9-A_boxed.gro -c -d 1 -bt cubic

# Make an solvated top file
cp 06AA1-9-A.top 06AA1-9-A_sol.top

# Solvate the molecule with acetonitrile
gmx solvate -cp 06AA1-9-A_boxed.gro -cs acetonitrile_320_box.gro -o 06AA1-9-A_sol.gro -p 06AA1-9-A_sol.top

# Modify the topology file to add solvent parameters to 06AA1-9-A_sol.top
cat >> 06AA1-9-A_sol.top <<EOL

; Include chloroform model
#include "./acetonitrile_320_box.itp"

EOL

# modified the acetonitrile_320_box.itp, change the name as UNL:
# commons out the [atomtypes]
cat >> acetonitrile_320_box.itp <<EOL

[ moleculetype ]
;name            nrexcl
 UNL  3
 
EOL

# adding the following two atomtypes of solvent in peptoid.itp, and change the atomic mass:
cat >> 06AA1-9-A.itp <<EOL

[ atomtypes ]
 c1       c1          0.00000  0.00000   A     3.39967e-01   8.78640e-01 ; 1.91  0.2100
 n1       n1          0.00000  0.00000   A     3.25000e-01   7.11280e-01 ; 1.82  0.1700


[ atoms ]
   211    H    10   NHE   HN1  211     0.231500      1.00000 ; qtot 0.768
   212    H    10   NHE   HN2  212     0.231500      1.00000 ; qtot 1.000

 
EOL

# Make an ion top file 
cp 06AA1-9-A_sol.top 06AA1-9-A_ion.top

#Create ion.tpr
gmx grompp -f mdp/ion.mdp -c 06AA1-9-A_sol.gro -p 06AA1-9-A_ion.top -o ion.tpr -maxwarn 2

# Neutralize the molecule
echo 3 | gmx genion -s ion.tpr -o 06AA1-9-A_ion.gro -p 06AA1-9-A_ion.top -pname NA -nname CL -neutral

# Modify the topology file to add solvent parameters to 19AF1-10-A_sol.top
cat >> 06AA1-9-A_ion.top <<EOL

; Include Ion model
#include "/usr/local/gromacs/share/gromacs/top/amber99.ff/ions.itp"

EOL



# Make an index file for our solvated+neutralized  peptoid
echo "\!18&\!19\nname 20 peptoid\nq\n" | gmx make_ndx -f 06AA1-9-A_ion.gro -o index.ndx 
echo "\!20\nq\n" | gmx make_ndx -n index.ndx 
echo "q" | gmx make_ndx -n index.ndx 
#212


# Prepare a EM.tpr file
gmx grompp -f mdp/em.mdp -c 06AA1-9-A_ion.gro -p 06AA1-9-A_ion.top -n index.ndx -o em_ion.tpr -maxwarn 2

#Run the EM 
gmx mdrun -nt 1 -v -s em_ion.tpr -c em_ion.gro -o em_ion.trr
# 3.8528027e+01 on atom 2488

# Prepare a NVT.tpr file
gmx grompp -f mdp/nvt.mdp -c em_ion.gro -p 06AA1-9-A_ion.top -n index.ndx -o nvt_ion.tpr -maxwarn 2

#Run the NVT 
gmx mdrun -nt 1 -v -s nvt_ion.tpr -c nvt_ion.gro -o nvt_ion.trr

# Check the run 
echo "16\n0\n" |gmx energy -f ener.edr -o temperature.xvg

# Prepare a NPT.tpr file
gmx grompp -f mdp/npt.mdp -c nvt_ion.gro -p 06AA1-9-A_ion.top -n index.ndx -o npt_ion.tpr -maxwarn 2

#Run the NPT 
gmx mdrun -nt 1 -v -s npt_ion.tpr -c npt_ion.gro -o npt_ion.trr 

# Check the run 
echo "18\n0\n" |gmx energy -f ener.edr -o temperature.xvg

# Prepare for productive run 
gmx grompp -f mdp/prod.mdp -c npt_ion.gro -p 06AA1-9-A_ion.top -o prod.tpr -maxwarn 2
