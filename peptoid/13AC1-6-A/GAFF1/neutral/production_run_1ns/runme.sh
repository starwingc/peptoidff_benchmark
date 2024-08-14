#!/bin/bash

# Load GROMACS module
# module load gromacs/2021.2
# replace the name in text file
# sed 's/13AC1-6-A/13AC1-6-A/g' runme.sh > runme_temp.sh && mv runme_temp.sh runme.sh

# make an peptoid.itp file 
cp 13AC1-6-A_GMX.top 13AC1-6-A.itp    
# make sure to command out the [default] and the [systems] [molecules] section

#make a top file 
cat >> 13AC1-6-A.top  <<EOL
; Include force field parameters
#include "/usr/local/gromacs/share/gromacs/top/amber99.ff/forcefield.itp"

; Include Peptoid
#include "./13AC1-6-A.itp"

[ system ]
 13AC1-6-A

[ molecules ]
; Compound        nmols
 13AC1-6-A        1 

EOL


# Add a box
gmx editconf -f 13AC1-6-A_GMX.gro -o 13AC1-6-A_boxed.gro -c -d 1 -bt cubic

# Make an solvated top file
cp 13AC1-6-A.top 13AC1-6-A_sol.top

# Solvate the molecule with water
gmx solvate -cp 13AC1-6-A_boxed.gro -cs chloroform_320_box.gro -o 13AC1-6-A_sol.gro -p 13AC1-6-A_sol.top

# Modify the topology file to add solvent parameters to 13AC1-6-A_sol.top
cat >> 13AC1-6-A_sol.top <<EOL

; Include chloroform model
#include "./chloroform_320_box.itp"

EOL

# adding the following two atomtypes in peptoid.itp:
#cat >> 13AC1-6-A.itp <<EOL

#[atomtypes]


#EOL


# Make an index file for our solvated+neutralized  peptoid
echo "\!17\nname 18 peptoid\nq\n" | gmx make_ndx -f 13AC1-6-A_sol.gro -o index.ndx 
echo "q" | gmx make_ndx -n index.ndx 
#198


# Prepare a EM.tpr file
gmx grompp -f mdp/em.mdp -c 13AC1-6-A_sol.gro -p 13AC1-6-A_sol.top -n index.ndx -o em_sol.tpr -maxwarn 4

#Run the EM 
gmx mdrun -nt 1 -v -s em_sol.tpr -c em_sol.gro -o em_sol.trr
# 7.7511566e+01 on atom 43

# Prepare a NVT.tpr file
gmx grompp -f mdp/nvt.mdp -c em_sol.gro -p 13AC1-6-A_sol.top -n index.ndx -o nvt_sol.tpr -maxwarn 4

#Run the NVT 
gmx mdrun -nt 1 -v -s nvt_sol.tpr -c nvt_sol.gro -o nvt_sol.trr

# Check the run 
echo "16\n0\n" |gmx energy -f ener.edr -o temperature.xvg

# Prepare a NPT.tpr file
#gmx grompp -f mdp/npt.mdp -c nvt_sol.gro -p 13AC1-6-A_sol.top -n index.ndx -t state.cpt -o npt_sol.tpr -maxwarn 4
gmx grompp -f mdp/npt.mdp -c nvt_sol.gro -p 13AC1-6-A_sol.top -n index.ndx  -o npt_sol.tpr -maxwarn 4

#Run the NPT 
gmx mdrun -nt 1 -v -s npt_sol.tpr -c npt_sol.gro -o npt_sol.trr 

# Check the run 
echo "18\n0\n" |gmx energy -f ener.edr -o temperature.xvg

# Prepare for productive run 
# gmx grompp -f mdp/prod_1.mdp -c npt_sol.gro -p 13AC1-6-A_sol.top -o prod_1.tpr -maxwarn 4
gmx grompp -f mdp/prod_2.mdp -c npt_sol.gro -p 13AC1-6-A_sol.top -o prod_2.tpr -maxwarn 4