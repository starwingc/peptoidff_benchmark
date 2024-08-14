#!/bin/bash

# Load GROMACS module
# module load gromacs/2021.2

# make an peptoid.itp file 
cp 19AE1-4-A_protonated_GMX.top 19AE1-4-A_protonated.itp    

# Edit the itp file, change the follwing mass of the molecule in itp file :

    82    H     5   NHE   HN1   82     0.231500      1.00000 ; qtot 2.769
    83    H     5   NHE   HN2   83     0.231500      1.00000 ; qtot 3.000

# make an top file   
cat >> 19AE1-4-A_protonated.top  <<EOL
; Include force field parameters
#include "/usr/local/gromacs/share/gromacs/top/amber99.ff/forcefield.itp"

; Include Peptoid
#include "./19AE1-4-A_protonated.itp"

[ system ]
 19AE1-4-A_protonated

[ molecules ]
; Compound        nmols
 19AE1-4-A_protonated 1 

EOL


# Add a box
gmx editconf -f 19AE1-4-A_protonated_GMX.gro -o 19AE1-4-A_protonated_boxed.gro -c -d 1 -bt cubic

# Make an solvated top file
cp 19AE1-4-A_protonated.top 19AE1-4-A_protonated_sol.top

# Solvate the molecule with water
gmx solvate -cp 19AE1-4-A_protonated_boxed.gro -cs spc216.gro -o 19AE1-4-A_protonated_sol.gro -p 19AE1-4-A_protonated_sol.top

# Modify the topology file to add solvent parameters to 19AE1-4-A_protonated_sol.top
cat >> 19AE1-4-A_protonated_sol.top <<EOL

; Include TIP3P water model
#include "/usr/local/gromacs/share/gromacs/top/amber99.ff/tip3p.itp"

EOL

#add an ion.mdp file from voelzlab/tutorials/gmx_protein/ion.mdp

# Make an ion top file 
cp 19AE1-4-A_protonated_sol.top 19AE1-4-A_protonated_ion.top

#Create ion.tpr
gmx grompp -f ion.mdp -c 19AE1-4-A_protonated_sol.gro -p 19AE1-4-A_protonated_ion.top -o ion.tpr -maxwarn 3

# Neutralize the molecule
echo 16 | gmx genion -s ion.tpr -o 19AE1-4-A_protonated_ion.gro -p 19AE1-4-A_protonated_ion.top -pname NA -nname CL -neutral

# Modify the topology file to add solvent parameters to 19AE1-4-A_protonated_sol.top
cat >> 19AE1-4-A_protonated_ion.top <<EOL

; Include Ion model
#include "/usr/local/gromacs/share/gromacs/top/amber99.ff/ions.itp"

EOL

# Make an index file for our solvated+neutralized  peptoid
echo "\!23\nname 24 peptoid\nq\n" | gmx make_ndx -f 19AE1-4-A_protonated_ion.gro -o index.ndx
echo "q" | gmx make_ndx -n index.ndx


# Prepare a EM.tpr file
gmx grompp -f em.mdp -c 19AE1-4-A_protonated_ion.gro -p 19AE1-4-A_protonated_ion.top -n index.ndx -o em_ion.tpr -maxwarn 3

#Run the EM 
gmx mdrun -nt 1 -v -s em_ion.tpr -c em_ion.gro -o em_ion.trr


# Prepare a NVT.tpr file
gmx grompp -f nvt.mdp -c em_ion.gro -p 19AE1-4-A_protonated_ion.top -n index.ndx -o nvt_ion.tpr -maxwarn 3

#Run the NVT 
gmx mdrun -nt 1 -v -s nvt_ion.tpr -c nvt_ion.gro -o nvt_ion.trr

# Check the run 
echo "16\n0\n" |gmx energy -f ener.edr -o temperature.xvg

# Prepare a NPT.tpr file
gmx grompp -f npt.mdp -c nvt_ion.gro -p 19AE1-4-A_protonated_ion.top -n index.ndx -t state.cpt -o npt_ion.tpr -maxwarn 3

#Run the NPT 
gmx mdrun -nt 1 -v -s npt_ion.tpr -c npt_ion.gro -o npt_ion.trr 

# Check the run 
echo "18\n0\n" |gmx energy -f ener.edr -o temperature.xvg

# Prepare for productive run 
gmx grompp -f prod.mdp -c npt_ion.gro -t state.cpt -p 19AE1-4-A_protonated_ion.top -o prod.tpr -maxwarn 3

