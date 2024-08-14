#!/bin/bash

# Load GROMACS module
# module load gromacs/2021.2
# replace the name in text file
# sed 's/17AB1-5-A/17AB1-5-A/g' runme.sh > runme_temp.sh && mv runme_temp.sh runme.sh

# make an peptoid.itp file 
cp 17AB1-5-A_GMX.top 17AB1-5-A.itp    
# make sure to command out the [default] and the [systems] [molecules] section

#make a top file 
cat >> 17AB1-5-A.top  <<EOL
; Include force field parameters
#include "/usr/local/gromacs/share/gromacs/top/amber99.ff/forcefield.itp"

; Include Peptoid
#include "./17AB1-5-A.itp"

[ system ]
 17AB1-5-A

[ molecules ]
; Compound        nmols
 17AB1-5-A        1 

EOL


# Add a box
gmx editconf -f 17AB1-5-A_GMX.gro -o 17AB1-5-A_boxed.gro -c -d 1 -bt cubic

# Make an solvated top file
cp 17AB1-5-A.top 17AB1-5-A_sol.top

# Solvate the molecule with water
gmx solvate -cp 17AB1-5-A_boxed.gro -cs meoh_320_box.gro -o 17AB1-5-A_sol.gro -p 17AB1-5-A_sol.top

# Modify the topology file to add solvent parameters to 17AB1-5-A_sol.top
cat >> 17AB1-5-A_sol.top <<EOL

; Include meoh model
#include "./meoh_320_box.itp"

EOL


# Make an index file for our solvated+neutralized  peptoid
echo "\!17\nname 18 peptoid\nq\n" | gmx make_ndx -f 17AB1-5-A_sol.gro -o index.ndx 
echo "q" | gmx make_ndx -n index.ndx 
#129


# Prepare a EM.tpr file
gmx grompp -f mdp/em.mdp -c 17AB1-5-A_sol.gro -p 17AB1-5-A_sol.top -n index.ndx -o em_sol.tpr -maxwarn 4

#Run the EM 
gmx mdrun -nt 1 -v -s em_sol.tpr -c em_sol.gro -o em_sol.trr
# 6.0103256e+01 on atom 72

# Prepare a NVT.tpr file
gmx grompp -f mdp/nvt.mdp -c em_sol.gro -p 17AB1-5-A_sol.top -n index.ndx -o nvt_sol.tpr -maxwarn 4

#Run the NVT 
gmx mdrun -nt 1 -v -s nvt_sol.tpr -c nvt_sol.gro -o nvt_sol.trr

# Check the run 
echo "16\n0\n" |gmx energy -f ener.edr -o temperature.xvg

# Prepare a NPT.tpr file
gmx grompp -f mdp/npt.mdp -c nvt_sol.gro -p 17AB1-5-A_sol.top -n index.ndx -t state.cpt -o npt_sol.tpr -maxwarn 4

#Run the NPT 
gmx mdrun -nt 1 -v -s npt_sol.tpr -c npt_sol.gro -o npt_sol.trr 

# Check the run 
echo "18\n0\n" |gmx energy -f ener.edr -o temperature.xvg

# Prepare for productive run 
gmx grompp -f mdp/prod_B.mdp -c npt_sol.gro -p 17AB1-5-A_sol.top -o prod.tpr -maxwarn 4