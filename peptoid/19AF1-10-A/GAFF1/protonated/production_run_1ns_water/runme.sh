#!/bin/bash

# Load GROMACS module
# module load gromacs/2021.2
# replace the name in text file
# sed 's/19AE1-4-A_protonated/19AF1-10-A/g' runme.sh > runme_temp.sh && mv runme_temp.sh runme.sh

# make an peptoid.itp file 
cp 19AF1-10-A_GMX.top 19AF1-10-A.itp    

# Edit the itp file, change the follwing mass of the molecule in itp file :

   287   H     11   NHE   HN1  287     0.231500      1.00800 ; qtot 4.768
   288   H     11   NHE   HN2  288     0.231500      1.00800 ; qtot 5.000

# make an top file   
cat >> 19AF1-10-A.top  <<EOL
; Include force field parameters
#include "/usr/local/gromacs/share/gromacs/top/amber99.ff/forcefield.itp"

; Include Peptoid
#include "./19AF1-10-A.itp"

[ system ]
 19AF1-10-A

[ molecules ]
; Compound        nmols
 19AF1-10-A        1 

EOL


# Add a box
gmx editconf -f 19AF1-10-A_GMX.gro -o 19AF1-10-A_boxed.gro -c -d 1 -bt cubic

# Make an solvated top file
cp 19AF1-10-A.top 19AF1-10-A_sol.top

# Solvate the molecule with water
gmx solvate -cp 19AF1-10-A_boxed.gro -cs spc216.gro -o 19AF1-10-A_sol.gro -p 19AF1-10-A_sol.top

# Modify the topology file to add solvent parameters to 19AF1-10-A_sol.top
cat >> 19AF1-10-A_sol.top <<EOL

; Include TIP3P water model
#include "/usr/local/gromacs/share/gromacs/top/amber99.ff/tip3p.itp"

EOL

#add an ion.mdp file from voelzlab/tutorials/gmx_protein/ion.mdp

# Make an ion top file 
cp 19AF1-10-A_sol.top 19AF1-10-A_ion.top

#Create ion.tpr
gmx grompp -f mdp/ion.mdp -c 19AF1-10-A_sol.gro -p 19AF1-10-A_ion.top -o ion.tpr -maxwarn 2

# Neutralize the molecule
echo 24 | gmx genion -s ion.tpr -o 19AF1-10-A_ion.gro -p 19AF1-10-A_ion.top -pname NA -nname CL -neutral

# Modify the topology file to add solvent parameters to 19AF1-10-A_sol.top
cat >> 19AF1-10-A_ion.top <<EOL

; Include Ion model
#include "/usr/local/gromacs/share/gromacs/top/amber99.ff/ions.itp"

EOL

# Make an index file for our solvated+neutralized  peptoid
echo "\!39\nname 40 peptoid\nq\n" | gmx make_ndx -f 19AF1-10-A_ion.gro -o index.ndx
echo "q" | gmx make_ndx -n index.ndx


# Prepare a EM.tpr file
gmx grompp -f mdp/em.mdp -c 19AF1-10-A_ion.gro -p 19AF1-10-A_ion.top -n index.ndx -o em_ion.tpr -maxwarn 2

#Run the EM 
gmx mdrun -nt 1 -v -s em_ion.tpr -c em_ion.gro -o em_ion.trr
# Maximum force     =  3.0416125e+02 on atom 36

# Prepare a NVT.tpr file
gmx grompp -f mdp/nvt.mdp -c em_ion.gro -p 19AF1-10-A_ion.top -n index.ndx -o nvt_ion.tpr -maxwarn 2

#Run the NVT 
gmx mdrun -nt 1 -v -s nvt_ion.tpr -c nvt_ion.gro -o nvt_ion.trr

# Check the run 
echo "16\n0\n" |gmx energy -f ener.edr -o temperature.xvg

# Prepare a NPT.tpr file
gmx grompp -f mdp/npt.mdp -c nvt_ion.gro -p 19AF1-10-A_ion.top -n index.ndx -t state.cpt -o npt_ion.tpr -maxwarn 2

#Run the NPT 
gmx mdrun -nt 1 -v -s npt_ion.tpr -c npt_ion.gro -o npt_ion.trr 

# Check the run 
echo "18\n0\n" |gmx energy -f ener.edr -o temperature.xvg

# Prepare for productive run 
gmx grompp -f mdp/prod.mdp -c npt_ion.gro -t state.cpt -p 19AF1-10-A_ion.top -o prod.tpr -maxwarn 2

