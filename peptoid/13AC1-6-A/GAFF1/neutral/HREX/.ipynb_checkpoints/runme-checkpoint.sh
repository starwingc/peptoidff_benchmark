# Transfer the file name
# Prepare n state with different FEP lambda value
# vi prepare_tpr.sh
# sed 's/19AF1-10-A/17AB2-8-A/g' prepare_tpr.sh > temp.sh && mv temp.sh prepare_tpr.sh 
# sed 's/19AF1-10-A/17AB2-8-A/g' fep.qsub > temp && mv temp fep.qsub
# clean all the state folder:

rm -r state*

# Activate the prepare_tpr.sh and run
chmod +x prepare_tpr.sh
./prepare_tpr.sh
# The result should be state_n/ include all the file and tpr for later running

# Submit the qsub job
qsub fep.qsub  

# Copy all the dhdl use for analyze
chmod +x analyze_dhdl.sh
./analyze_dhdl.sh

# if only record the peptoid as output, need to make a new gro file that delete all the solvent and ion

gmx editconf -f HREMD.part0001.gro -n index.ndx -o HREMD_withoutwater.part0001.gro

