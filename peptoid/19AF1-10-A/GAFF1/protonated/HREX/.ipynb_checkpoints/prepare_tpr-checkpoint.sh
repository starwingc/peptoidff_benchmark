#!/bin/bash

# Load GROMACS and MPI modules
module load gromacs/2021.2
module load mpi/openmpi

# Number of alchemical intermediate states
n=6

# Define fep-lambdas values
fep_lambdas=(0.00 0.20 0.40 0.60 0.80 1.00)

# Loop over the states
for i in {0..5}
do
  # Create a directory for each state and change into it
  mkdir -p state_${i} && cd state_${i}

  # Copy the necessary input files into the directory
  cp ../19AF1-10-A_fep.gro .
  cp ../19AF1-10-A_fep.top .
  cp ../19AF1-10-A_fep.itp .
  cp ../prod_fep.mdp .
  cp ../index.ndx .  

  # Check if files exist
  if [ ! -f "19AF1-10-A_fep.gro" ] || [ ! -f "19AF1-10-A_fep.top" ] || [ ! -f "prod_fep.mdp" ]|| [ ! -f "index.ndx" ]; then
    echo "Error: One or more input files are missing in state_${i} directory!"
    exit 1
  fi

  # Get the lambda value for the current state
  lambda_value=${fep_lambdas[$i]}

  # Modify the init-lambda-state in the prod_fep.mdp file
  sed -i -e "s/init-lambda-state        = 0/init-lambda-state        = ${i}/g" prod_fep.mdp
  
  # Run the GROMACS preprocessor
  gmx grompp -f prod_fep.mdp -c 19AF1-10-A_fep.gro -p 19AF1-10-A_fep.top -n index.ndx -o HREMD.tpr -maxwarn 2
  
  # Print out the last few lines of the modified prod_fep.mdp file
  echo "Contents of prod_fep.mdp in state_${i}:"
  tail prod_fep.mdp

  # Navigate back to the parent directory
  cd ..
done

