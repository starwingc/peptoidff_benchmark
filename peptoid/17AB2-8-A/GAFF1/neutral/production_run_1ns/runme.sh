#!/bin/bash

# Load GROMACS module
# module load gromacs/2021.2
# replace the name in text file
# sed 's/17AB2-8-A/17AB2-8-A/g' runme.sh > runme_temp.sh && mv runme_temp.sh runme.sh

# make an peptoid.itp file 
cp 17AB2-8-A_GMX.top 17AB2-8-A.itp    
# make sure to command out the [default] and the [systems] [molecules] section

#make a top file 
cat >> 17AB2-8-A.top  <<EOL
; Include force field parameters
#include "/usr/local/gromacs/share/gromacs/top/amber99.ff/forcefield.itp"

; Include Peptoid
#include "./17AB2-8-A.itp"

[ system ]
 17AB2-8-A

[ molecules ]
; Compound        nmols
 17AB2-8-A        1 

EOL


# Add a box
gmx editconf -f 17AB2-8-A_GMX.gro -o 17AB2-8-A_boxed.gro -c -d 1 -bt cubic

# Make an solvated top file
cp 17AB2-8-A.top 17AB2-8-A_sol.top

# Solvate the molecule with water
gmx solvate -cp 17AB2-8-A_boxed.gro -cs acetonitrile_320_box.gro -o 17AB2-8-A_sol.gro -p 17AB2-8-A_sol.top

# Modify the topology file to add solvent parameters to 17AB2-8-A_sol.top
cat >> 17AB2-8-A_sol.top <<EOL

; Include acetonitrile model
#include "./acetonitrile_320_box.itp"

EOL

# modified the acetonitrile_320_box.itp, change the name as UNL:
cat >> acetonitrile_320_box.itp <<EOL

[ moleculetype ]
;name            nrexcl
 UNL  3
 
EOL


# Make an index file for our solvated+neutralized  peptoid
echo "\!19\nname 20 peptoid\nq\n" | gmx make_ndx -f 17AB2-8-A_sol.gro -o index.ndx 
echo "q" | gmx make_ndx -n index.ndx 
#198


# Prepare a EM.tpr file
gmx grompp -f mdp/em.mdp -c 17AB2-8-A_sol.gro -p 17AB2-8-A_sol.top -n index.ndx -o em_sol.tpr -maxwarn 4

#Run the EM 
gmx mdrun -nt 1 -v -s em_sol.tpr -c em_sol.gro -o em_sol.trr
# 8.7168610e+01 on atom 3584

# Prepare a NVT.tpr file
gmx grompp -f mdp/nvt.mdp -c em_sol.gro -p 17AB2-8-A_sol.top -n index.ndx -o nvt_sol.tpr -maxwarn 4

#Run the NVT 
gmx mdrun -nt 1 -v -s nvt_sol.tpr -c nvt_sol.gro -o nvt_sol.trr

# Check the run 
echo "16\n0\n" |gmx energy -f ener.edr -o temperature.xvg

# Prepare a NPT.tpr file
gmx grompp -f mdp/npt.mdp -c nvt_sol.gro -p 17AB2-8-A_sol.top -n index.ndx -t state.cpt -o npt_sol.tpr -maxwarn 4

#Run the NPT 
gmx mdrun -nt 1 -v -s npt_sol.tpr -c npt_sol.gro -o npt_sol.trr 

# Check the run 
echo "18\n0\n" |gmx energy -f ener.edr -o temperature.xvg

# Prepare for productive run 
gmx grompp -f mdp/prod.mdp -c npt_sol.gro -p 17AB2-8-A_sol.top -o prod.tpr -maxwarn 4