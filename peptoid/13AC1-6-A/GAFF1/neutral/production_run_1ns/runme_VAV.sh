#!/bin/bash

# Make an index file for our solvated+neutralized  peptoid
echo "\!17\nname 18 peptoid\nq\n" | gmx make_ndx -f 13AC1-6-A_sol.gro -o index.ndx 

### VAV:  Had to edit this by hand; pushed the result-- there were repeated lines
### 13AC1-6-A_sol.top 

### It now looks like this:
# ; Include force field parameters
# #include "/usr/local/gromacs/share/gromacs/top/amber99.ff/forcefield.itp"
# 
# ; Include Peptoid
# #include "./13AC1-6-A.itp"
#
# ; Include chloroform model
# #include "./chloroform_320_box.itp"
# 
# 
# [ system ]
# 13AC1-6-A in water
# 
# [ molecules ]
# ; Compound        nmols
# 13AC1-6-A        1 
# UNL              472
#


##########
### VAV: I *also* had to remove the [ defaults ] directive from `./13AC1-6-A.itp` 
###      Since the amberff99.itp is being loaded in first, the defaults were already defined
###
###      Also, moved these lines (at the bottom of the *.itp) to the [ atomtypes ] section:
### [atomtypes]
###  cl       cl          0.00000  0.00000   A     3.46595e-01   1.10374e+00 ; 1.95  0.2638
###  h3       h3          0.00000  0.00000   A     2.06564e-01   8.70272e-02 ; 1.16  0.0208
###
###   ... and the [ system ] and [ molecules ]  lines, which belong in the *.top but NOT the *.itp:


# Prepare a EM.tpr file
gmx grompp -f mdp/em.mdp -c 13AC1-6-A_sol.gro -p 13AC1-6-A_sol.top -n index.ndx -o em_sol.tpr -maxwarn 4

# Run the EM 
gmx mdrun -nt 1 -v -s em_sol.tpr -c em_sol.gro -o em_sol.trr
# 3.6788292e+01 on atom 5972

# Prepare a NVT.tpr file
gmx grompp -f mdp/nvt.mdp -c em_sol.gro -p 13AC1-6-A_sol.top -n index.ndx -o nvt_sol.tpr -maxwarn 4

#Run the NVT 
gmx mdrun -nt 1 -v -s nvt_sol.tpr -c nvt_sol.gro -o nvt_sol.trr

# Check the run 
echo "16\n0\n" |gmx energy -f ener.edr -o temperature.xvg

# Prepare a NPT.tpr file
gmx grompp -f mdp/npt.mdp -c nvt_sol.gro -p 13AC1-6-A_sol.top -n index.ndx  -o npt_sol.tpr -maxwarn 4

#Run the NPT 
gmx mdrun -nt 1 -v -s npt_sol.tpr -c npt_sol.gro -o npt_sol.trr

# Check the run 
echo "18\n0\n" |gmx energy -f ener.edr -o temperature.xvg

# Prepare for productive run 
gmx grompp -f mdp/prod.mdp -c npt_sol.gro -t state.cpt -p 13AC1-6-A_sol.top -o prod.tpr -maxwarn 4
