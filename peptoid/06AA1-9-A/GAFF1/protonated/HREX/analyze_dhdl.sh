mkdir dhdl_files && cd dhdl_files
for i in {0..5};
do
  mkdir state_${i}
  cp ../state_${i}/dhdl*xvg state_${i}/.
done


