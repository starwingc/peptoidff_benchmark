
echo "0\n" | gmx editconf -f 13AC1-6-A_GMX.gro -bt cubic -d 10 -c -princ
gmx grompp -f em.mdp -c out.gro -p 13AC1-6-A_GMX.top -o em.tpr -v
gmx mdrun -ntmpi 1 -v -deffnm em
gmx grompp -f md.mdp -c em.gro -p 13AC1-6-A_GMX.top -o md.tpr -r em.gro
gmx mdrun -ntmpi 1 -v -deffnm md
