# Transfer the file name
# Prepare n state with different FEP lambda value
#i prepare_tpr.sh
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
